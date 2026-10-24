"""Exercise real routes and category actions against an isolated demo on 8081."""

import asyncio
import json
import subprocess
import tempfile
import urllib.request

import websockets

from verify_workspace import Browser, CHROME


async def main():
    with tempfile.TemporaryDirectory(prefix="caresync-views-", ignore_cleanup_errors=True) as profile:
        process = subprocess.Popen([CHROME, "--headless=new", "--disable-gpu", "--remote-debugging-port=9347", f"--user-data-dir={profile}", "about:blank"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        try:
            for _ in range(40):
                try:
                    with urllib.request.urlopen("http://127.0.0.1:9347/json", timeout=1) as response:
                        tabs = json.load(response)
                    break
                except OSError:
                    await asyncio.sleep(.2)
            ws_url = next(tab["webSocketDebuggerUrl"] for tab in tabs if tab["type"] == "page")
            async with websockets.connect(ws_url, max_size=30_000_000) as ws:
                browser = Browser(ws)
                await browser.call("Page.enable")
                await browser.call("Runtime.enable")
                await browser.viewport(1440, 1000)
                await browser.call("Page.navigate", {"url": "http://127.0.0.1:8081/#/medications"})
                await browser.wait("document.querySelector('.medication-table') && !document.body.classList.contains('busy')")
                if await browser.evaluate("document.querySelector('#voice').getAttribute('aria-pressed') === 'true'"):
                    await browser.click("#voice")
                await browser.click("#reset")
                assert await browser.evaluate("location.hash === '#/medications'")
                initial_count = await browser.evaluate("document.querySelectorAll('.message').length")

                async def route(name):
                    rail_key = "meds" if name == "medications" else name
                    await browser.evaluate(f"(() => {{ const node = matchMedia('(max-width: 600px)').matches ? document.querySelector('.view-navigation [data-route={name}]') : document.querySelector('[data-nav={rail_key}]'); node.click(); }})()")
                    await browser.wait(f"document.querySelector('.header-title h1').textContent === {json.dumps({'medications':'Medications','calendar':'Calendar','supplies':'Supplies','memory':'Memory','home':'Care assistant'}[name])}")

                for name in ("medications", "calendar", "supplies", "memory"):
                    await route(name)
                    await browser.no_overflow()
                    await browser.shot(f"views-{name}-desktop.png")
                assert await browser.evaluate(f"document.querySelectorAll('.message').length === {initial_count}"), "Navigation sent a message"
                await browser.evaluate("document.querySelector('#utterance').value='keep this draft'")
                await route("medications")
                await route("calendar")
                await browser.evaluate("history.back()")
                await browser.wait("location.hash === '#/medications' && document.querySelector('.medication-table')")
                await browser.evaluate("history.forward()")
                await browser.wait("location.hash === '#/calendar' && document.querySelector('#reschedule-form')")
                assert await browser.evaluate("document.querySelector('#utterance').value === 'keep this draft'")
                await route("medications")
                await browser.evaluate("document.querySelector('#medication-filter').value='attention';document.querySelector('#medication-filter').dispatchEvent(new Event('change'))")
                assert await browser.evaluate("document.querySelectorAll('.medication-table tbody tr').length === 1 && document.querySelector('.medication-table').textContent.includes('Lisinopril')")
                await route("supplies")
                await browser.click("[data-supply-id='strips'] .route-action")
                await browser.wait("document.querySelector('.confirmation:not(.resolved)')")
                assert await browser.evaluate("document.querySelector('#speech').textContent.includes('$18.99')")
                assert await browser.evaluate("location.hash === '#/supplies'")
                await browser.click(".confirmation:not(.resolved) .yes")
                await browser.wait("document.querySelector('[data-supply-id=strips]').textContent.includes('48 days')")
                assert await browser.evaluate("document.querySelector('[data-supply-id=briefs]').textContent.includes('4 days')")
                await route("calendar")
                await browser.evaluate("document.querySelector('[name=weekday]').value='Thursday';document.querySelector('[name=time]').value='09:15';document.querySelector('#reschedule-form').requestSubmit()")
                await browser.wait("!document.body.classList.contains('busy') && document.querySelector('.appointment-time').textContent.includes('9:15 AM')")
                await route("memory")
                assert await browser.evaluate("document.querySelector('.memory-list').textContent.includes('Thursday, 9:15 AM')")
                await browser.call("Page.reload")
                await browser.wait("document.querySelector('.memory-list') && !document.body.classList.contains('busy')")
                assert await browser.evaluate("location.hash === '#/memory' && document.querySelector('.memory-list').textContent.includes('9:15 AM')")
                await browser.viewport(390, 844)
                for name in ("medications", "calendar", "supplies", "memory"):
                    await route(name)
                    assert await browser.evaluate("document.querySelector('#route-view').getBoundingClientRect().width > 0")
                    await browser.no_overflow()
                    await browser.shot(f"views-{name}-mobile.png")
                await route("medications")
                await browser.click("#route-view .route-action")
                await browser.wait("document.querySelector('.confirmation:not(.resolved)')")
                assert await browser.evaluate("document.activeElement === document.querySelector('.assistant-panel-title')"), "Opening the assistant lost keyboard focus"
                await browser.shot("views-assistant-mobile.png")
                assert await browser.evaluate("document.querySelector('#assistant-panel').getBoundingClientRect().width > 0")
                count = await browser.evaluate("document.querySelectorAll('.message').length")
                await browser.click("#assistant-toggle")
                await route("supplies")
                assert await browser.evaluate(f"document.querySelectorAll('.message').length === {count} && !!document.querySelector('.confirmation:not(.resolved)')"), "Tab navigation lost pending confirmation or added messages"
                await browser.click("#assistant-toggle")
                await browser.click(".confirmation:not(.resolved) .no")
                await browser.wait("document.querySelector('.confirmation.resolved')")
                for width in (320, 600, 900, 1024, 1299, 1300, 1536):
                    await browser.viewport(width, 844)
                    await route("calendar")
                    assert await browser.evaluate("document.documentElement.scrollWidth <= innerWidth"), f"Overflow at {width}"
                await browser.evaluate("location.hash='/unknown-route'")
                await browser.wait("location.hash === '#/home'")
                await browser.click("#reset")
                assert not browser.errors, browser.errors
                print("PASS: real views; no chat on navigation; deep link and refresh; Back/Forward; draft and pending preservation; filters; item-specific order; reschedule and memory; mobile assistant; responsive widths; invalid route fallback; reset.")
                await browser.call("Browser.close")
        finally:
            if process.poll() is None:
                process.terminate()
            process.wait(timeout=10)


if __name__ == "__main__":
    asyncio.run(main())
