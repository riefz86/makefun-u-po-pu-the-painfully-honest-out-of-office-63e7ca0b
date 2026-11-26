#!/usr/bin/env python3
"""The Painfully Honest Out of Office.

Writes one brutally honest but still polite out-of-office auto-reply
(a single sentence, at most 200 characters) to /output/entry.txt.

The reply admits what a real employee would only say privately: the
inbox will be several hundred deep on return, and replies will be
triaged by genuine urgency. It stays warm and professional, thanks
the sender, and promises a reply as soon as possible.
"""
import os

ENTRY = (
    "I'm away until Monday and will return to several hundred unread "
    "emails, so thank you for your patience \u2014 I'll reply as soon "
    "as I can, starting with the ones that truly can't wait."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
