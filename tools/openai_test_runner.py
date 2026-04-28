"""Simple test runner for OpenAI backend (no API key included).

Usage:
    python -m tools.openai_test_runner

This will attempt to initialize LMStudioChat and call start() and a dummy send(),
using OPENAI_API_KEY from environment or config.toml.
"""
from pathlib import Path
import os

from ai_chat import LMStudioChat


def main():
    print("OpenAI test runner")
    chat = LMStudioChat()
    try:
        backend = chat.init_backend()
        print("Initialized backend:", backend)
    except Exception as e:
        print("Backend init failed:", e)
        return
    print("start():", chat.start()[:120])
    try:
        reply = chat.send("請用一句話介紹職位：軟體工程師")
        print("reply:", reply[:300])
    except Exception as e:
        print("send failed:", e)


if __name__ == '__main__':
    main()
