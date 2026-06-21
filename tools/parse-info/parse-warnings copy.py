import re
from pathlib import Path
import pandas as pd


ROOT_DIR = "/Users/lucifer/vscode_Luci_scripts/HBCD-DOCS/2.1/hbcd-docs/docs/instruments"  # change to your root folder

results = []

for md_file in Path(ROOT_DIR).rglob("*.md"):

    text = md_file.read_text(encoding="utf-8")

    # Extract instrument title from first H1
    title_match = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
    instrument = title_match.group(1).strip() if title_match else md_file.stem

    # Find warning banner followed by collapsible content
    warning_match = re.search(
        r"\{\{\s*scoring_banner_macro\(\)\s*\}\}.*?"
        r'<div class="collapsible-content">(.*?)</div>',
        text,
        re.DOTALL,
    )

    if warning_match:
        warning_html = warning_match.group(1).strip()

        # Remove paragraph tags and other simple HTML
        warning_text = re.sub(r"<[^>]+>", "", warning_html)
        warning_text = re.sub(r"\s+", " ", warning_text).strip()

        results.append(
            {
                "instrument": instrument,
                "file": str(md_file),
                "warning": warning_text,
            }
        )

# Print results
# for item in results:
#     print("=" * 80)
#     print(item["instrument"])
#     print(item["file"])
#     print()
#     print(item["warning"])
#     print()

pd.DataFrame(results).to_csv(
    "instrument_scoring.csv",
    index=False
)