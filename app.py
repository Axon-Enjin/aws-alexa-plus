"""Vercel loads this module and serves `app`."""

import os

os.environ.setdefault("VERCEL", "1")

from caresync.web_app import app  # noqa: E402
