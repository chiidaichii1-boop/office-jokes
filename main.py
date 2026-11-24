"""Office-jokes entry: writes one one-line office joke to /output/entry.txt."""

import os

JOKE = "I blocked focus time on my calendar, then someone booked a meeting over it titled 'Quick sync about your focus time.'"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
