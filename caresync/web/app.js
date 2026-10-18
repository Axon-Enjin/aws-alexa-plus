const speechEl = document.querySelector("#speech");
const cardsEl = document.querySelector("#cards");
const boardEl = document.querySelector("#board");
const traceEl = document.querySelector("#trace");
const protoEl = document.querySelector("#proto");
const clockEl = document.querySelector("#clock");
const form = document.querySelector("#composer");
const input = document.querySelector("#utterance");
const micBtn = document.querySelector("#mic");
const voiceBtn = document.querySelector("#voice");
const resetBtn = document.querySelector("#reset");
const chipsEl = document.querySelector("#chips");

const SUGGESTIONS = [
  "What’s going on with Mom today?",
  "Remind her on the kitchen Show",
  "When is cardiology?",
  "Order the usual briefs",
  "What did we decide yesterday?",
];

const sessionId = localStorage.getItem("caresync-session") || crypto.randomUUID();
localStorage.setItem("caresync-session", sessionId);

let voiceOn = localStorage.getItem("caresync-voice") !== "off";
let pendingToken = "";
let recognition = null;

function paintClock() {
  const now = new Date();
  clockEl.textContent = now.toLocaleTimeString([], { hour: "numeric", minute: "2-digit" });
}
paintClock();
setInterval(paintClock, 15000);

function paintVoice() {
  voiceBtn.textContent = voiceOn ? "Voice on" : "Voice off";
}
paintVoice();

function chips() {
  chipsEl.replaceChildren();
  for (const text of SUGGESTIONS) {
    const button = document.createElement("button");
    button.type = "button";
    button.textContent = text;
    button.addEventListener("click", () => send(text));
    chipsEl.appendChild(button);
  }
}
chips();

function say(text) {
  if (!voiceOn || !window.speechSynthesis) return;
  window.speechSynthesis.cancel();
  const utterance = new SpeechSynthesisUtterance(text);
  utterance.rate = 0.98;
  window.speechSynthesis.speak(utterance);
}

function renderCards(cards) {
  cardsEl.replaceChildren();
  pendingToken = "";
  for (const card of cards || []) {
    const node = document.createElement("article");
    node.className = `card ${card.tone || "info"}`;
    const title = document.createElement("h3");
    title.textContent = card.title || "CareSync";
    const body = document.createElement("p");
    body.textContent = card.body || "";
    node.append(title, body);
    if (card.confirm) {
      pendingToken = card.confirm.token || "";
      const row = document.createElement("div");
      row.className = "row";
      row.append(
        choice(card.confirm.yes, "yes", card.confirm.token),
        choice(card.confirm.no, "no", card.confirm.token),
      );
      node.append(row);
    } else if (card.action) {
      const row = document.createElement("div");
      row.className = "row";
      const button = document.createElement("button");
      button.type = "button";
      button.textContent = card.action.label;
      button.addEventListener("click", () => send(card.action.utterance));
      row.append(button);
      node.append(row);
    }
    if (card.task_id) watchTask(card.task_id, body);
    cardsEl.append(node);
  }
}

function choice(label, kind, token) {
  const button = document.createElement("button");
  button.type = "button";
  button.className = kind;
  button.textContent = label;
  button.addEventListener("click", () => send(label, token));
  return button;
}

async function watchTask(taskId, body) {
  const started = body.textContent;
  for (let i = 0; i < 8; i += 1) {
    await new Promise((resolve) => setTimeout(resolve, 700));
    const response = await fetch(`/api/task/${encodeURIComponent(taskId)}`);
    const task = await response.json();
    if (task.status === "completed") {
      body.textContent = `${started}\n${task.result || "Finished."}`;
      return;
    }
    body.textContent = `${started}\nSending…`;
  }
}

function renderBoard(home) {
  const meds = (home.meds || [])
    .map((med) => `<li><span>${med.name} ${med.dose}</span><span class="${med.status}">${med.status}</span></li>`)
    .join("");
  const visit = home.appointment || {};
  const briefs = (home.supplies || []).find((item) => item.id === "briefs");
  const notes = (home.memories || []).slice(0, 2).map((note) => `<p class="note">${escapeHtml(note.body)}</p>`).join("");
  const show = home.telemetry?.echo_show;
  boardEl.innerHTML = `
    <p class="sub">Care board</p>
    <h2>${escapeHtml(home.resident.name)}</h2>
    <p class="sub">${home.resident.age} · ${escapeHtml(home.resident.city)} · ${escapeHtml(home.resident.conditions)}</p>
    <h3>Medicines</h3>
    <ul>${meds}</ul>
    <h3>Next visit</h3>
    <p class="note">${escapeHtml(visit.when_label || "")} · ${escapeHtml(visit.clinician || "")}<br>${escapeHtml(visit.place || "")}<br>Ride: ${escapeHtml(visit.ride || "")}. ${escapeHtml(visit.note || "")}</p>
    <h3>Supplies</h3>
    <p class="note">${briefs ? `${escapeHtml(briefs.brand)} · ${briefs.days_left} days · ${escapeHtml(briefs.price)}` : ""}</p>
    <h3>Show</h3>
    <p class="note">${show ? `${escapeHtml(show.name)} is ${show.online ? "online" : "offline"}` : ""}</p>
    <h3>Already noted</h3>
    ${notes}
  `;
}

function escapeHtml(value) {
  return String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;");
}

function renderTrace(payload) {
  const calls = (payload.trace || []).map((item) => `${item.tool} ${item.ms}ms`).join(" · ");
  if (payload.transport === "streamable-http") {
    const protocol = `MCP ${payload.protocol || "2025-11-25"}`;
    protoEl.textContent = `${protocol} · Streamable HTTP`;
    traceEl.textContent = calls ? `${protocol} · ${calls}` : protocol;
    return;
  }
  protoEl.textContent = "CareSync on Vercel";
  traceEl.textContent = calls;
}

async function loadBoard() {
  const response = await fetch("/api/board");
  renderBoard(await response.json());
}

async function send(utterance, token = "") {
  const text = utterance.trim();
  if (!text) return;
  input.value = "";
  document.body.classList.add("busy");
  speechEl.textContent = "Checking the care record…";
  try {
    const response = await fetch("/api/turn", {
      method: "POST",
      headers: { "content-type": "application/json" },
      body: JSON.stringify({
        utterance: text,
        session_id: sessionId,
        confirmation_token: token || pendingToken || "",
      }),
    });
    const payload = await response.json();
    speechEl.textContent = payload.speech || "I don’t have an answer for that.";
    renderCards(payload.cards);
    renderTrace(payload);
    say(payload.speech || "");
    await loadBoard();
  } catch (error) {
    speechEl.textContent = "The care server didn’t answer. Leave this tab open and try the question again.";
    traceEl.textContent = String(error);
  } finally {
    document.body.classList.remove("busy");
  }
}

form.addEventListener("submit", (event) => {
  event.preventDefault();
  send(input.value);
});

voiceBtn.addEventListener("click", () => {
  voiceOn = !voiceOn;
  localStorage.setItem("caresync-voice", voiceOn ? "on" : "off");
  if (!voiceOn && window.speechSynthesis) window.speechSynthesis.cancel();
  paintVoice();
});

resetBtn.addEventListener("click", async () => {
  pendingToken = "";
  await fetch("/api/reset", { method: "POST" });
  speechEl.textContent = "Household reset. Ask what’s going on with Mom today.";
  cardsEl.replaceChildren();
  traceEl.textContent = "";
  await loadBoard();
});

const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
if (SpeechRecognition) {
  recognition = new SpeechRecognition();
  recognition.lang = "en-US";
  recognition.interimResults = false;
  recognition.onresult = (event) => {
    const text = event.results[0][0].transcript;
    input.value = text;
    send(text, pendingToken);
  };
  recognition.onend = () => document.body.classList.remove("listening");
  micBtn.addEventListener("click", () => {
    document.body.classList.add("listening");
    recognition.start();
  });
} else {
  micBtn.disabled = true;
  micBtn.title = "This browser has no speech recognition. Type instead.";
}

loadBoard();
