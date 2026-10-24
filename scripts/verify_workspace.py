"""Bounded desktop/mobile capture and browser exercise of the caregiver workspace.

Start an isolated preview on 8081 before running. All writes target that demo.
"""

from __future__ import annotations

import asyncio
import base64
import json
import subprocess
import tempfile
import urllib.request
from pathlib import Path

import websockets

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
PORT = 9346
OUT = Path(__file__).resolve().parent.parent / ".impeccable" / "review"


class Browser:
    def __init__(self, ws):
        self.ws = ws
        self.sequence = 0
        self.errors = []

    async def call(self, method, params=None):
        self.sequence += 1
        await self.ws.send(json.dumps({"id": self.sequence, "method": method, "params": params or {}}))
        while True:
            message = json.loads(await self.ws.recv())
            if message.get("method") == "Runtime.exceptionThrown":
                self.errors.append(message["params"])
            if message.get("id") == self.sequence:
                if "error" in message:
                    raise RuntimeError(message["error"])
                return message.get("result", {})

    async def evaluate(self, expression):
        result = await self.call("Runtime.evaluate", {"expression": expression, "returnByValue": True, "awaitPromise": True})
        if "exceptionDetails" in result:
            raise RuntimeError(result["exceptionDetails"])
        return result.get("result", {}).get("value")

    async def wait(self, expression):
        for _ in range(120):
            if await self.evaluate(f"Boolean({expression})"):
                return
            await asyncio.sleep(.15)
        print("FAILED STATE", await self.evaluate("({speech:document.querySelector('#speech')?.textContent,text:document.querySelector('#log')?.innerText})"), self.errors)
        await self.shot("failed-state.png")
        raise TimeoutError(expression)

    async def viewport(self, width, height):
        await self.call("Emulation.setDeviceMetricsOverride", {"width": width, "height": height, "deviceScaleFactor": 1, "mobile": width < 600})
        await asyncio.sleep(.3)
        await self.evaluate("(() => { const pane = document.querySelector('#conversation'); if (pane) pane.scrollTop = pane.scrollHeight; })()")
        await asyncio.sleep(.3)

    async def shot(self, name):
        await asyncio.sleep(.3)
        result = await self.call("Page.captureScreenshot", {"format": "png", "captureBeyondViewport": True})
        (OUT / name).write_bytes(base64.b64decode(result["data"]))
        print("Captured", name)

    async def send(self, text):
        count = await self.evaluate("document.querySelectorAll('.message').length")
        await self.evaluate(f"document.querySelector('#utterance').value = {json.dumps(text)}; document.querySelector('#composer').requestSubmit()")
        await self.wait(f"!document.body.classList.contains('busy') && document.querySelectorAll('.message').length > {count}")

    async def click(self, selector):
        await self.evaluate(f"document.querySelector({json.dumps(selector)}).click()")
        await self.wait("!document.body.classList.contains('busy')")

    async def no_overflow(self):
        assert await self.evaluate("document.documentElement.scrollWidth <= innerWidth"), "Horizontal page overflow"
        assert await self.evaluate("document.querySelector('.composer').getBoundingClientRect().bottom <= innerHeight"), "Composer below viewport"


async def main():
    OUT.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="caresync-ui-", ignore_cleanup_errors=True) as profile:
        process = subprocess.Popen([CHROME, "--headless=new", "--disable-gpu", f"--remote-debugging-port={PORT}", f"--user-data-dir={profile}", "about:blank"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        try:
            tabs = []
            for _ in range(40):
                try:
                    with urllib.request.urlopen(f"http://127.0.0.1:{PORT}/json", timeout=1) as response:
                        tabs = json.load(response)
                    if tabs:
                        break
                except OSError:
                    await asyncio.sleep(.2)
            ws_url = next(tab["webSocketDebuggerUrl"] for tab in tabs if tab["type"] == "page")
            async with websockets.connect(ws_url, max_size=30_000_000) as ws:
                browser = Browser(ws)
                await browser.call("Page.enable")
                await browser.call("Runtime.enable")
                await browser.viewport(1536, 1024)
                await browser.call("Page.navigate", {"url": "http://127.0.0.1:8081"})
                await browser.wait("document.querySelector('#speech') && !document.body.classList.contains('busy')")
                await browser.evaluate("localStorage.setItem('caresync-voice','off')")
                if await browser.evaluate("document.querySelector('#voice').getAttribute('aria-pressed') === 'true'"):
                    await browser.click("#voice")
                await browser.click("#reset")
                await browser.shot("initial.png")
                await browser.send("Remind her on the kitchen Show")
                await browser.wait("document.querySelector('.confirmation:not(.resolved) .yes')")
                await browser.no_overflow()
                await browser.shot("comp-size.png")
                await browser.viewport(1440, 1000)
                await browser.no_overflow()
                await browser.shot("desktop.png")
                await browser.viewport(390, 844)
                await browser.no_overflow()
                await browser.shot("mobile.png")
                await browser.click("#context-toggle")
                assert await browser.evaluate("document.querySelector('#main').inert && document.querySelector('#context-toggle').getAttribute('aria-expanded') === 'true'")
                await browser.shot("mobile-context.png")
                await browser.call("Input.dispatchKeyEvent", {"type": "keyDown", "key": "Escape", "code": "Escape"})
                await browser.wait("!document.body.classList.contains('context-open')")
                await browser.click(".confirmation:not(.resolved) .no")
                assert await browser.evaluate("document.querySelector('.confirmation').classList.contains('resolved')")
                await browser.send("Order the usual briefs")
                await browser.wait("document.querySelector('.confirmation:not(.resolved) .yes')")
                await browser.click(".confirmation:not(.resolved) .yes")
                await browser.wait("document.querySelector('#supplies').textContent.includes('34 days')")
                await browser.send("Mom's cardiologist moved to Thursday at 2")
                assert await browser.evaluate("document.querySelector('#visit').textContent.includes('Thursday, 2:00 PM')")
                await browser.send("Get me ready for Thursday")
                await browser.wait("document.querySelector('.task-card details')")
                assert await browser.evaluate("Array.from(document.querySelectorAll('.task-card button')).some(n => n.textContent.includes('Download packet'))")
                await browser.shot("mobile-packet.png")
                assert await browser.evaluate("(() => { const pane=document.querySelector('#conversation'); return pane.scrollHeight-pane.scrollTop-pane.clientHeight < 3; })()"), "Completed packet actions did not follow latest messages"
                await browser.click(".task-card details summary")
                assert await browser.evaluate("Array.from(document.querySelectorAll('.task-result')).some(n => n.textContent.includes('Questions') && n.textContent.includes('Lisinopril'))")
                await browser.no_overflow()
                await browser.send("Get me ready for Thursday")
                await asyncio.sleep(.35)
                await browser.evaluate("document.querySelector('#conversation').scrollTo({top:0,behavior:'instant'})")
                await browser.wait("document.querySelectorAll('.task-card details').length === 2")
                assert await browser.evaluate("document.querySelector('#conversation').scrollTop === 0"), "Packet completion interrupted history reading"
                await browser.viewport(1024, 768)
                await browser.no_overflow()
                await browser.viewport(320, 640)
                await browser.no_overflow()
                await browser.evaluate("window.originalFetch=window.fetch;window.fetch=(url,options)=>url==='/api/turn'?Promise.resolve(new Response('{}',{status:503})):window.originalFetch(url,options)")
                await browser.send("How is Elena today?")
                assert await browser.evaluate("document.querySelector('#utterance').value === 'How is Elena today?' && !!document.querySelector('.message.error .retry-button')")
                await browser.evaluate("window.fetch=window.originalFetch")
                await browser.click("#reset")
                assert await browser.evaluate("document.querySelectorAll('.message').length === 1 && document.querySelector('#supplies').textContent.includes('4 days')")
                assert not browser.errors, browser.errors
                print("PASS: reminder cancel; order confirm; appointment update; packet completion; download control; reset; network failure recovery; mobile drawer; 320/390/1024/1440/1536 widths; no JavaScript exceptions.")
                await browser.call("Browser.close")
        finally:
            process.terminate()
            process.wait(timeout=10)
            await asyncio.sleep(.5)


if __name__ == "__main__":
    asyncio.run(main())
