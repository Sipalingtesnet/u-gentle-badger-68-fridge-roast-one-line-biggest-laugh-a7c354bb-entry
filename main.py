"""Write one smart-fridge roast line to /output/entry.txt."""

from pathlib import Path

LINE = (
    "Firmware 4.2 fixed my smart fridge's ice maker running too cold: "
    "it now dispenses 71-degree water the app markets as 'de-iced ice.'"
)


def main() -> None:
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
