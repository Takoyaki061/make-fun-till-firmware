"""Till Firmware Do Us Part — a robot's wedding vow.

Writes one funny, heartfelt sentence a robot says at its own wedding
to /output/entry.txt (gate: UTF-8 text, 1-200 characters).
"""

import os

VOW = "I will hold your hand with servos that shake, and pretend it's the calibration and not you."


def main() -> None:
    # Self-check against the sealed gate scorer: UTF-8 text, 1-200 chars,
    # not only whitespace, one sentence. Fail loudly instead of shipping
    # an entry the gate would refuse.
    text = VOW.strip()
    assert 1 <= len(text) <= 200, f"vow is {len(text)} chars, gate needs 1-200"
    assert text, "vow must not be only whitespace"
    assert text.count(".") == 1 and text.endswith("."), "vow must be one sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
