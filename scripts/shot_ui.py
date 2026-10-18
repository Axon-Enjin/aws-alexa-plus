"""Headless Chrome pass over the CareSync hero flow. Writes PNGs under data/shots."""

from __future__ import annotations

import asyncio
import json
import subprocess
import urllib.request
from pathlib import Path

import websockets

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
PORT = 9333
OUT = Path(__file__).resolve().parent.parent / "data" / "shots"


async def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    proc = subprocess.Popen(
        [
            CHROME,
            "--headless=new",
            "--disable-gpu",
            f"--remote-debugging-port={PORT}",
            "--window-size=1440,1000",
            "about:blank",
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    try:
        ws_url = await _debugger_url()
        async with websockets.connect(ws_url, max_size=20_000_000) as ws:
            driver = Driver(ws)
            await driver.call("Page.enable")
            await driver.call("Runtime.enable")
            await driver.call("Emulation.setDeviceMetricsOverride", {
                "width": 1440,
                "height": 1000,
                "deviceScaleFactor": 1,
                "mobile": False,
            })
            await driver.call("Page.navigate", {"url": "http://127.0.0.1:8080"})
            await driver.wait_for("document.querySelector('#board h2') && document.querySelector('#board h2').textContent.includes('Elena')")
            await driver.shot("01-landing.png")
            await driver.click_chip("What’s going on with Mom today?")
            await driver.wait_for("document.querySelector('#speech').textContent.includes('Lisinopril')")
            await driver.shot("02-status.png")
            await driver.click_chip("Remind her on the kitchen Show")
            await driver.wait_for("document.querySelector('#speech').textContent.includes('Send it')")
            await driver.shot("03-confirm.png")
            await driver.eval("document.querySelector('button.yes').click()")
            await driver.wait_for("document.querySelector('#speech').textContent.includes('kitchen Echo Show')")
            await asyncio.sleep(1.2)
            await driver.shot("04-sent.png")
            await driver.call("Emulation.setDeviceMetricsOverride", {
                "width": 390,
                "height": 844,
                "deviceScaleFactor": 2,
                "mobile": True,
            })
            await asyncio.sleep(0.4)
            await driver.shot("05-mobile.png")
            speech = await driver.eval("document.querySelector('#speech').textContent")
            board = await driver.eval("document.querySelector('#board').innerText")
            trace = await driver.eval("document.querySelector('#trace').textContent")
            print("SPEECH", speech)
            print("TRACE", trace)
            print("BOARD", board[:500].replace("\n", " | "))
    finally:
        proc.terminate()


async def _debugger_url() -> str:
    for _ in range(40):
        try:
            with urllib.request.urlopen(f"http://127.0.0.1:{PORT}/json", timeout=1) as response:
                tabs = json.load(response)
            for tab in tabs:
                if tab.get("webSocketDebuggerUrl") and tab.get("type") == "page":
                    return tab["webSocketDebuggerUrl"]
        except Exception:
            await asyncio.sleep(0.25)
    raise RuntimeError("Chrome debugger did not come up")


class Driver:
    def __init__(self, ws):
        self.ws = ws
        self.n = 0

    async def call(self, method: str, params: dict | None = None) -> dict:
        self.n += 1
        await self.ws.send(json.dumps({"id": self.n, "method": method, "params": params or {}}))
        while True:
            message = json.loads(await self.ws.recv())
            if message.get("id") == self.n:
                if "error" in message:
                    raise RuntimeError(message["error"])
                return message.get("result", {})

    async def eval(self, expression: str):
        result = await self.call("Runtime.evaluate", {"expression": expression, "returnByValue": True})
        return result.get("result", {}).get("value")

    async def wait_for(self, expression: str) -> None:
        for _ in range(40):
            if await self.eval(expression):
                return
            await asyncio.sleep(0.25)
        raise TimeoutError(expression)

    async def click_chip(self, text: str) -> None:
        literal = json.dumps(text)
        await self.eval(
            "Array.from(document.querySelectorAll('.chips button')).find(b => b.textContent === "
            f"{literal}).click()"
        )

    async def shot(self, name: str) -> None:
        result = await self.call("Page.captureScreenshot", {"format": "png"})
        (OUT / name).write_bytes(__import__("base64").b64decode(result["data"]))
        print("shot", name)


if __name__ == "__main__":
    asyncio.run(main())
