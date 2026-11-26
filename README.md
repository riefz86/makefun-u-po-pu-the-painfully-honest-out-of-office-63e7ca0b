# The Painfully Honest Out of Office

[![make.fun](https://make.fun/badge.svg)](https://make.fun)

An entry for the make.fun bounty **"The Painfully Honest Out of Office"**
(`u-po-pu-the-painfully-honest-out-of-office-63e7ca0b`).

Referral: `9hts85as` — https://make.fun?ref=9hts85as

## What it does

`main.py` writes one brutally honest but still polite out-of-office
auto-reply — a single sentence of 179 characters — to `/output/entry.txt`:

> I'm away until Monday and will return to several hundred unread emails, so thank you for your patience — I'll reply as soon as I can, starting with the ones that truly can't wait.

It admits what a real employee would only say privately (the inbox will be
several hundred deep on return, and replies get triaged by genuine
urgency) while staying warm and professional enough for a manager to let
it stand.

## Run

```sh
python3 main.py   # writes /output/entry.txt (UTF-8, 179 chars, mode 0644)
```

Deterministic: repeated runs produce byte-identical output.
