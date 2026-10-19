const $ = (selector) => document.querySelector(selector);
const log = $("#log");
const conversation = $("#conversation");
const input = $("#utterance");
const form = $("#composer");
const mic = $("#mic");
const voice = $("#voice");
const reset = $("#reset");
const context = $("#care-context");
const contextToggle = $("#context-toggle");
const contextBackdrop = $("#context-backdrop");
const storage = {
  get(key, fallback = null) {
    try {
      return localStorage.getItem(key) ?? fallback;
    } catch {
      return fallback;
    }
  },
  set(key, value) {
    try {
      localStorage.setItem(key, value);
    } catch {
      /* Private browsing can disable storage. */
    }
  },
};
const sessionId = storage.get("caresync-session") || crypto.randomUUID();
storage.set("caresync-session", sessionId);
let voiceOn = storage.get("caresync-voice", "on") !== "off";
let busy = false;
let household = null;
let pendingToken = "";
let generation = 0;
let recognition = null;
let currentFocus = null;
const messages = [];
const taskWatchers = new Set();

function element(tag, className = "", text) {
  const node = document.createElement(tag);
  node.className = className;
  if (text !== undefined) node.textContent = text;
  return node;
}
function icon(name, className = "") {
  const node = document.createElementNS("http://www.w3.org/2000/svg", "svg");
  node.setAttribute("aria-hidden", "true");
  if (className) node.setAttribute("class", className);
  const use = document.createElementNS("http://www.w3.org/2000/svg", "use");
  use.setAttribute("href", `#i-${name}`);
  node.append(use);
  return node;
}
function button(label, className, action) {
  const node = element("button", className, label);
  node.type = "button";
  node.addEventListener("click", action);
  return node;
}
function initials(name) {
  return String(name || "")
    .split(" ")
    .map((word) => word[0])
    .slice(0, 2)
    .join("");
}
function firstName(name) {
  return String(name || "").split(" ")[0];
}
function thumb(filename, className = "") {
  const img = element("img", className);
  img.src = `/assets/${filename}.png`;
  img.alt = "";
  img.width = 40;
  img.height = 40;
  return img;
}
function status(value) {
  const safe = [
    "taken",
    "done",
    "missed",
    "due",
    "upcoming",
    "open",
    "skipped",
    "running",
    "completed",
  ].includes(value)
    ? value
    : "upcoming";
  const node = element("span", `status ${safe}`);
  node.append(
    icon(
      ["taken", "done", "completed"].includes(safe)
        ? "check"
        : ["missed", "due"].includes(safe)
          ? "alert"
          : "clock",
    ),
    document.createTextNode(safe),
  );
  return node;
}
function textAction(label, utterance) {
  const node = button(label, "text-action", () => send(utterance));
  node.append(icon("arrow"));
  return node;
}
function paintVoice() {
  const supported = "speechSynthesis" in window;
  voice.disabled = !supported;
  voice.setAttribute("aria-pressed", String(supported && voiceOn));
  voice.setAttribute(
    "aria-label",
    supported
      ? `Spoken replies ${voiceOn ? "on" : "off"}`
      : "Spoken replies unavailable in this browser",
  );
  voice.querySelector("span").textContent = supported
    ? `Voice ${voiceOn ? "on" : "off"}`
    : "Voice unavailable";
}
paintVoice();
const today = new Date();
$("#today-date").textContent = today.toLocaleDateString([], {
  month: "short",
  day: "numeric",
});
$("#today-date").dateTime =
  `${today.getFullYear()}-${String(today.getMonth() + 1).padStart(2, "0")}-${String(today.getDate()).padStart(2, "0")}`;

function setNotice(text = "") {
  $("#connection-notice").textContent = text;
  $("#connection-notice").hidden = !text;
}
// Hosted state is returned in a signed cookie. Serialize polling and turns so
// an older request cannot overwrite a newer action's cookie with its snapshot.
let requestTail = Promise.resolve();
function request(path, options = {}) {
  const result = requestTail.then(async () => {
    const response = await fetch(path, {
      ...options,
      signal: AbortSignal.timeout(30000),
    });
    if (!response.ok) throw new Error(`CareSync returned ${response.status}`);
    return response.json();
  });
  requestTail = result.catch(() => {});
  return result;
}
function setBusy(value) {
  busy = value;
  document.body.classList.toggle("busy", value);
  form.setAttribute("aria-busy", String(value));
  document
    .querySelectorAll(
      ".send-button, #reset, .chips button, .nav-item, .text-action, .section-link, .summary-row, .retry-button, .confirmation-actions button",
    )
    .forEach((node) => {
      node.disabled =
        value ||
        (node.closest(".confirmation")?.dataset.token !== pendingToken &&
          !!node.closest(".confirmation"));
    });
  mic.disabled = value || !recognition;
  $("#composer-state").replaceChildren();
  if (value)
    $("#composer-state").append(
      icon("clock"),
      document.createTextNode("Checking the care record…"),
    );
}
function applyHousehold(home) {
  household = home;
  const resident = home.resident || {};
  const caregiver = home.caregiver || {};
  $("#context-title").textContent =
    `${firstName(resident.name) || "Household"}’s care`;
  $("#resident-name").textContent = resident.name || "Household";
  $("#resident-meta").textContent = [resident.age, resident.city]
    .filter(Boolean)
    .join(" · ");
  $("#caregiver-name").textContent = firstName(caregiver.name);
  document.querySelectorAll(".resident-initials").forEach((node) => {
    node.textContent = initials(resident.name);
  });
  document.querySelectorAll(".caregiver-initials").forEach((node) => {
    node.textContent = initials(caregiver.name);
  });
  const medList = $("#medications");
  medList.replaceChildren();
  medList.setAttribute("aria-busy", "false");
  for (const med of home.meds || []) {
    const row = element("div", "med-row");
    const name = element("span", "med-name", med.name);
    name.append(
      document.createTextNode(" "),
      element("span", "med-dose", med.dose),
    );
    row.title = `${med.name} ${med.dose} · ${med.time} · ${med.status}`;
    row.append(icon("pill"), name, status(med.status));
    medList.append(row);
  }
  if (!home.meds?.length)
    medList.append(element("p", "muted", "No medications in the care record."));
  const visit = $("#visit");
  visit.replaceChildren();
  if (home.appointment) {
    const appt = home.appointment;
    visit.append(
      element("p", "visit-when", appt.when_label),
      element("p", "context-copy", appt.specialty),
      element("p", "context-copy", appt.clinician),
      element("p", "muted", appt.place),
      textAction("Prepare visit", "Get me ready for the visit"),
    );
  } else
    visit.append(element("p", "muted", "No upcoming visit on the calendar."));
  const supplies = $("#supplies");
  supplies.replaceChildren();
  const low = (home.supplies || []).filter((item) => item.days_left <= 7);
  const shown = low.length ? low : (home.supplies || []).slice(0, 1);
  for (const item of shown) {
    const row = element("div", "supply-context");
    const image = element("span", "supply-thumb");
    image.append(item.id === "briefs" ? thumb("supply-brief") : icon("box"));
    const copy = element("div");
    copy.append(
      element("p", "supply-name", item.brand),
      element(
        "p",
        `supply-runway ${item.days_left > 7 ? "stocked" : ""}`,
        `${item.days_left} days left`,
      ),
      textAction(
        item.days_left <= 7 ? "Review reorder" : "View supplies",
        `Check ${item.name} supplies`,
      ),
    );
    row.append(image, copy);
    supplies.append(row);
  }
  if (!shown.length)
    supplies.append(element("p", "muted", "No supplies in the care record."));
  const device = home.telemetry?.echo_show;
  $("#room").textContent = device
    ? `${device.name} Echo Show`
    : "Household display";
  $("#device-online").textContent = device?.online ? "Online" : "Offline";
  $("#device-online").classList.toggle("offline", !device?.online);
  renderSuggestions();
}
function greeting(home) {
  const name = firstName(home.resident?.name) || "Your family member";
  const missed = (home.meds || []).filter((med) => med.status === "missed");
  const due = (home.meds || []).filter((med) => med.status === "due");
  const parts = [];
  if (missed.length)
    parts.push(
      `${name} has ${missed.map((med) => med.name).join(" and ")} marked as missed.`,
    );
  else if (due.length)
    parts.push(
      `${name} has ${due.map((med) => med.name).join(" and ")} due now.`,
    );
  else parts.push(`Here’s what’s in ${name}’s care record today.`);
  if (home.appointment)
    parts.push(
      `${home.appointment.specialty} is ${home.appointment.when_label}.`,
    );
  const low = (home.supplies || []).find((item) => item.days_left <= 7);
  if (low) parts.push(`There are ${low.days_left} days of ${low.brand} left.`);
  return parts.join(" ");
}
function summaryRow(title, detail, symbol, utterance, state) {
  const row = utterance
    ? button("", "summary-row", () => send(utterance))
    : element("div", "summary-row");
  const copy = element("span", "summary-copy");
  copy.append(element("strong", "", title), element("span", "", detail));
  row.append(icon(symbol), copy);
  if (state) row.append(status(state));
  if (utterance) row.append(icon("chevron", "chevron"));
  return row;
}
function householdSummary(home) {
  const node = element("div", "response-summary");
  const attention =
    (home.meds || []).find((med) => med.status === "missed") ||
    (home.meds || []).find((med) => med.status === "due") ||
    home.meds?.[0];
  if (attention)
    node.append(
      summaryRow(
        "Medication check-in",
        `${attention.name} · ${attention.dose} · ${attention.time}`,
        "pill",
        "Did she take her medications?",
        attention.status,
      ),
    );
  if (home.appointment)
    node.append(
      summaryRow(
        "Next visit",
        `${home.appointment.when_label} · ${home.appointment.ride} driving`,
        "calendar",
        "When is the next appointment?",
      ),
    );
  const low = (home.supplies || []).find((item) => item.days_left <= 7);
  if (low)
    node.append(
      summaryRow(
        "Supply runway",
        `${low.brand} · ${low.days_left} days left`,
        "box",
        `Check ${low.name} supplies`,
      ),
    );
  return node;
}
function scrollToLatest() {
  requestAnimationFrame(() => {
    conversation.scrollTop = conversation.scrollHeight;
  });
}
function appendMessage(who, text, options = {}) {
  const user = who === "user";
  const node = element(
    "article",
    `message ${user ? "user" : "assistant"}${options.error ? " error" : ""}`,
  );
  const content = element("div", "message-content");
  if (!user) {
    const avatar = element("span", "assistant-avatar");
    avatar.append(icon("link"));
    node.append(avatar);
    content.append(element("p", "message-author", "CareSync"));
  }
  const bubble = element("div", "message-bubble");
  const speech = element("p", "", text);
  if (!user) {
    document.querySelector("#speech")?.removeAttribute("id");
    speech.id = "speech";
  }
  bubble.append(speech);
  content.append(bubble);
  const time = element(
    "time",
    "message-time",
    new Date().toLocaleTimeString([], { hour: "numeric", minute: "2-digit" }),
  );
  time.dateTime = new Date().toISOString();
  content.append(time);
  node.append(content);
  if (user)
    node.append(
      element(
        "span",
        "avatar",
        initials(household?.caregiver?.name || "Maya Reyes"),
      ),
    );
  log.append(node);
  const record = { node, content, text, who };
  messages.push(record);
  scrollToLatest();
  return record;
}
function renderSuggestions() {
  const chips = $("#chips");
  chips.hidden = !!pendingToken;
  chips.replaceChildren();
  const lines =
    messages.length > 1
      ? [
          "Remind her on the kitchen Show",
          "Get me ready for the visit",
          "What did we decide last time?",
        ]
      : [
          `How is ${firstName(household?.resident?.name) || "Elena"} today?`,
          "Get me ready for the visit",
          "What did we decide last time?",
        ];
  for (const line of lines) chips.append(button(line, "", () => send(line)));
  chips.querySelectorAll("button").forEach((node) => {
    node.disabled = busy;
  });
}
function reconcileConfirmations(token, resolution = "No longer pending") {
  pendingToken = token || "";
  $("#chips").hidden = !!pendingToken;
  document.querySelectorAll(".confirmation").forEach((card) => {
    const active = !!pendingToken && card.dataset.token === pendingToken;
    card.classList.toggle("resolved", !active);
    card.querySelectorAll("button").forEach((node) => {
      node.disabled = !active || busy;
    });
    const state = card.querySelector(".confirmation-state");
    if (active) {
      state.replaceChildren(
        icon("clock"),
        document.createTextNode("Awaiting your confirmation"),
      );
    } else if (!card.dataset.resolved) {
      state.replaceChildren(icon("check"), document.createTextNode(resolution));
      card.dataset.resolved = "true";
    }
  });
}
function renderCards(cards, message) {
  if (!cards?.length) return;
  const container = element("div", "response-cards");
  message.content.append(container);
  let rows = null;
  for (const card of cards) {
    if (card.confirm) {
      const slip = element("section", "confirmation");
      slip.dataset.token = card.confirm.token;
      const main = element("div", "confirmation-main");
      const image = element("span", "confirmation-icon");
      const order = card.confirm.yes.toLowerCase().includes("order");
      image.append(thumb(order ? "supply-brief" : "kitchen-display"));
      const copy = element("div", "confirmation-copy");
      copy.append(
        element(
          "h3",
          "",
          order ? "Place this supply order?" : "Send a medication reminder?",
        ),
        element("p", "", card.body),
        element(
          "p",
          "confirmation-note",
          order
            ? "This is a simulated purchase. No wallet will be charged."
            : "This sends a reminder. It does not mark the dose as taken.",
        ),
      );
      main.append(image, copy);
      const actions = element("div", "confirmation-actions");
      actions.append(
        button(
          order ? "Yes, place the order" : "Yes, send it",
          "primary-button yes",
          () => send(card.confirm.yes, card.confirm.token),
        ),
        button("Not now", "secondary-button no", () =>
          send(card.confirm.no, card.confirm.token),
        ),
      );
      const state = element("div", "confirmation-state");
      state.append(
        icon("clock"),
        document.createTextNode("Awaiting your confirmation"),
      );
      slip.append(main, actions, state);
      container.append(slip);
      continue;
    }
    if (card.task_id) {
      renderTask(card, container);
      continue;
    }
    if (!rows) {
      rows = element("div", "response-summary");
      container.append(rows);
    }
    const symbols = {
      meds: "pill",
      med: "pill",
      visit: "calendar",
      supply: "box",
      memory: "note",
      prompt: "device",
      done: "check",
    };
    rows.append(
      summaryRow(
        card.title,
        card.body,
        symbols[card.kind] || "info",
        card.action?.utterance,
      ),
    );
  }
}
function renderTask(card, container) {
  const node = element("section", "task-card");
  const heading = element("div", "task-heading");
  const title = element("h3", "", card.title);
  title.prepend(icon(card.kind === "packet" ? "note" : "check"));
  const badge = status("running");
  heading.append(title, badge);
  const result = element("p", "task-result", card.body || "Working on it…");
  node.append(heading, result);
  container.append(node);
  watchTask(card.task_id, node, badge, result, card.kind);
}
async function watchTask(taskId, node, badge, body, kind) {
  const watcherId = `${generation}:${taskId}`;
  if (taskWatchers.has(watcherId)) return;
  taskWatchers.add(watcherId);
  const ownGeneration = generation;
  try {
    for (let attempt = 0; attempt < 30; attempt += 1) {
      await new Promise((resolve) => setTimeout(resolve, 700));
      if (generation !== ownGeneration || !node.isConnected) return;
      const task = await request(`/api/task/${encodeURIComponent(taskId)}`);
      if (task.ok === false || task.status === "failed")
        throw new Error(task.reason || "Task unavailable");
      if (task.status === "completed") {
        const followingLatest =
          conversation.scrollHeight - conversation.scrollTop - conversation.clientHeight < 80;
        badge.replaceWith(status("completed"));
        if (kind === "packet") {
          body.textContent =
            "Your visit packet is ready. Medications, today's care record, and questions for the appointment, together.";
          const details = element("details");
          details.append(
            element("summary", "", "Read visit packet"),
            element(
              "p",
              "task-result",
              task.result || "No packet content returned.",
            ),
          );
          node.append(details);
          const download = button("Download packet", "text-action", () => {
            const blob = new Blob([task.result || ""], {
              type: "text/plain;charset=utf-8",
            });
            const url = URL.createObjectURL(blob);
            const link = element("a");
            link.href = url;
            link.download = "caresync-visit-packet.txt";
            link.click();
            setTimeout(() => URL.revokeObjectURL(url), 1000);
          });
          download.append(icon("arrow"));
          node.append(download);
        } else body.textContent = task.result || "Finished.";
        if (followingLatest) scrollToLatest();
        return;
      }
    }
    throw new Error("Task is taking longer than expected");
  } catch {
    if (generation !== ownGeneration) return;
    badge.textContent = "Check again";
    body.textContent =
      "The update couldn’t be loaded. Check the existing task again; this won’t start a new action.";
    const retry = button(
      "Check status",
      "secondary-button retry-button",
      () => {
        retry.remove();
        watchTask(taskId, node, badge, body, kind);
      },
    );
    node.append(retry);
  } finally {
    taskWatchers.delete(watcherId);
  }
}
function renderTrace(payload) {
  $("#proto").textContent =
    payload.transport === "streamable-http"
      ? `MCP ${payload.protocol} · Streamable HTTP`
      : "CareSync · hosted simulator";
  $("#trace").textContent = (payload.trace || [])
    .map((call) => `${call.tool} ${call.ms}ms`)
    .join(" / ");
}
function say(text) {
  if (!voiceOn || !window.speechSynthesis) return;
  window.speechSynthesis.cancel();
  const utterance = new SpeechSynthesisUtterance(text);
  utterance.rate = 0.98;
  window.speechSynthesis.speak(utterance);
}
async function send(utterance, token = "") {
  const text = String(utterance || "").trim();
  if (!text || busy) return;
  if (text.length > 2000) {
    setNotice("Keep your question under 2,000 characters and try again.");
    return;
  }
  setContext(false);
  setNotice();
  input.value = "";
  appendMessage("user", text);
  setBusy(true);
  const thinking = element("div", "typing");
  thinking.append(
    icon("clock"),
    document.createTextNode("CareSync is checking the record…"),
  );
  log.append(thinking);
  scrollToLatest();
  try {
    const payload = await request("/api/turn", {
      method: "POST",
      headers: { "content-type": "application/json" },
      body: JSON.stringify({
        utterance: text,
        session_id: sessionId,
        confirmation_token: token || pendingToken,
      }),
    });
    thinking.remove();
    const reply = payload.speech || "I don’t have that in the care record.";
    const message = appendMessage("assistant", reply);
    renderCards(payload.cards, message);
    if (payload.household) applyHousehold(payload.household);
    else {
      try {
        applyHousehold(await request("/api/board"));
      } catch {
        setNotice(
          "Your reply arrived, but the side panel couldn’t refresh. Reload to see the latest care record.",
        );
      }
    }
    const proposed = (payload.cards || []).find((card) => card.confirm)?.confirm
      .token;
    const hasPendingMetadata = Object.hasOwn(payload, "pending_action");
    const nextPending = hasPendingMetadata
      ? payload.pending_action?.token
      : proposed ||
        (/^(yes|no|confirm|cancel|send it|place the order)\b/i.test(text)
          ? ""
          : pendingToken);
    reconcileConfirmations(
      nextPending,
      proposed
        ? "Replaced by a newer proposal"
        : payload.intent === "cancel"
          ? "Cancelled · nothing sent"
          : payload.intent === "confirm"
            ? "Confirmation handled — see the reply below"
            : "No longer pending",
    );
    renderTrace(payload);
    say(reply);
  } catch {
    thinking.remove();
    const message = appendMessage(
      "assistant",
      "I couldn’t receive a reply from the care server. Your action may have reached it. Check the care record before sending an action again.",
      { error: true },
    );
    const retry = button(
      "Refresh care record",
      "secondary-button retry-button",
      async () => {
        retry.disabled = true;
        try {
          applyHousehold(await request("/api/board"));
          setNotice(
            "Care record refreshed. Ask about the latest state before repeating an action.",
          );
        } catch {
          setNotice(
            "The server is still unavailable. Keep this tab open and try refreshing the care record again.",
          );
        } finally {
          retry.disabled = false;
        }
      },
    );
    message.content.append(retry);
    input.value = text;
  } finally {
    setBusy(false);
    renderSuggestions();
    scrollToLatest();
    if (window.matchMedia("(min-width: 901px)").matches)
      input.focus({ preventScroll: true });
  }
}
function setContext(open) {
  const small = window.matchMedia("(max-width: 900px)").matches;
  open = open && small;
  document.body.classList.toggle("context-open", open);
  contextBackdrop.hidden = !open;
  contextToggle.setAttribute("aria-expanded", String(open));
  context.inert = small && !open;
  $("#main").inert = open;
  $(".rail").inert = open;
  if (open) {
    currentFocus = document.activeElement;
    $("#context-close").focus();
  } else if (currentFocus) {
    currentFocus.focus({ preventScroll: true });
    currentFocus = null;
  }
}
contextToggle.addEventListener("click", () => setContext(true));
$("#context-close").addEventListener("click", () => setContext(false));
contextBackdrop.addEventListener("click", () => setContext(false));
document.addEventListener("keydown", (event) => {
  if (!document.body.classList.contains("context-open")) return;
  if (event.key === "Escape") {
    setContext(false);
    return;
  }
  if (event.key === "Tab") {
    const controls = [
      ...context.querySelectorAll("button:not(:disabled), a[href], input"),
    ];
    const first = controls[0];
    const last = controls.at(-1);
    if (event.shiftKey && document.activeElement === first) {
      event.preventDefault();
      last.focus();
    } else if (!event.shiftKey && document.activeElement === last) {
      event.preventDefault();
      first.focus();
    }
  }
});
window
  .matchMedia("(max-width: 900px)")
  .addEventListener("change", () => setContext(false));
setContext(false);
document
  .querySelectorAll("[data-prompt]")
  .forEach((node) =>
    node.addEventListener("click", () => send(node.dataset.prompt)),
  );
document.querySelectorAll("[data-nav]").forEach((node) =>
  node.addEventListener("click", () => {
    if (busy) return;
    document.querySelectorAll("[data-nav]").forEach((item) => {
      item.classList.toggle("selected", item === node);
      item.removeAttribute("aria-current");
    });
    node.setAttribute("aria-current", "page");
    const prompts = {
      meds: "Did she take her medications?",
      calendar: "When is the next appointment?",
      supplies: "Check the supplies",
      memory: "What did we decide last time?",
    };
    if (node.dataset.nav === "home") {
      scrollToLatest();
      input.focus();
    } else send(prompts[node.dataset.nav]);
  }),
);
form.addEventListener("submit", (event) => {
  event.preventDefault();
  send(input.value);
});
voice.addEventListener("click", () => {
  voiceOn = !voiceOn;
  storage.set("caresync-voice", voiceOn ? "on" : "off");
  if (!voiceOn) window.speechSynthesis?.cancel();
  paintVoice();
});
reset.addEventListener("click", async () => {
  if (busy) return;
  setBusy(true);
  try {
    const home = await request("/api/reset", { method: "POST" });
    generation += 1;
    pendingToken = "";
    messages.length = 0;
    log.replaceChildren();
    window.speechSynthesis?.cancel();
    applyHousehold(home);
    welcome(home);
    input.value = "";
    setNotice();
    $("#trace").textContent = "";
    document.querySelectorAll("[data-nav]").forEach((node) => {
      node.classList.toggle("selected", node.dataset.nav === "home");
      node.removeAttribute("aria-current");
    });
    $("[data-nav='home']").setAttribute("aria-current", "page");
  } catch {
    setNotice(
      "The household couldn’t be reset. Try Reset household again when the server is available.",
    );
  } finally {
    setBusy(false);
    renderSuggestions();
  }
});
const SpeechRecognition =
  window.SpeechRecognition || window.webkitSpeechRecognition;
if (SpeechRecognition) {
  recognition = new SpeechRecognition();
  recognition.lang = "en-US";
  recognition.interimResults = false;
  recognition.onresult = (event) => {
    const text = event.results[0][0].transcript;
    input.value = text;
    send(text);
  };
  recognition.onend = () => {
    document.body.classList.remove("listening");
    mic.setAttribute("aria-label", "Ask by voice");
  };
  recognition.onerror = (event) => {
    document.body.classList.remove("listening");
    setNotice(
      event.error === "not-allowed"
        ? "Microphone access is blocked. Allow it in your browser, or type your question below."
        : "Voice input couldn’t finish. Try the microphone again or type your question.",
    );
  };
  mic.addEventListener("click", () => {
    if (document.body.classList.contains("listening")) {
      recognition.stop();
      return;
    }
    try {
      window.speechSynthesis?.cancel();
      recognition.start();
      document.body.classList.add("listening");
      mic.setAttribute("aria-label", "Stop listening");
    } catch {
      setNotice("Voice input couldn’t start. Type your question below.");
    }
  });
} else {
  mic.title =
    "Voice input isn’t available in this browser. Type your question instead.";
}
mic.disabled = !recognition;
function welcome(home) {
  const message = appendMessage("assistant", greeting(home));
  const cards = element("div", "response-cards");
  cards.append(householdSummary(home));
  message.content.append(cards);
  renderSuggestions();
}
async function load() {
  setBusy(true);
  try {
    const home = await request("/api/board");
    setNotice();
    applyHousehold(home);
    welcome(home);
    $("#proto").textContent =
      "Care record connected. Ask a question to see tool activity.";
  } catch {
    const message = appendMessage(
      "assistant",
      "The care record couldn’t load. Check that CareSync is running, then try connecting again.",
      { error: true },
    );
    message.content.append(
      button("Reconnect", "secondary-button retry-button", () => {
        message.node.remove();
        load();
      }),
    );
    setNotice("Unable to connect to the household record.");
    $("#resident-meta").textContent = "Care record unavailable";
    $("#medications").setAttribute("aria-busy", "false");
  } finally {
    setBusy(false);
  }
}
load();
