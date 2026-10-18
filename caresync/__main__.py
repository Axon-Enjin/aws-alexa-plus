"""python -m caresync"""

from __future__ import annotations

import os

import uvicorn

from caresync.mcp_server import build_app


def main() -> None:
    port = int(os.environ.get("CARESYNC_PORT", "8080"))
    uvicorn.run(build_app(port), host="127.0.0.1", port=port, log_level="info")


if __name__ == "__main__":
    main()
