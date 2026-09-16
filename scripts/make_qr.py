"""Regenerate the QR code shown on the closing slide.

Usage: python scripts/make_qr.py [url]
"""

import sys
from pathlib import Path

import qrcode

DEFAULT_URL = "https://samclark2015.github.io/conf-talk-2026/"
OUTPUT = Path(__file__).resolve().parent.parent / "assets" / "qr-slides.png"


def main(url: str = DEFAULT_URL) -> None:
    qr = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=12,
        border=2,
    )
    qr.add_data(url)
    qr.make(fit=True)
    qr.make_image(fill_color="black", back_color="white").save(OUTPUT)
    print(f"Wrote {OUTPUT} -> {url}")


if __name__ == "__main__":
    main(*sys.argv[1:])
