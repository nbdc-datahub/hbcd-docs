import re
from pathlib import Path
import pandas as pd


ROOT_DIR = "/Users/lucifer/vscode_Luci_scripts/HBCD-DOCS/2.1/hbcd-docs/docs/instruments"

results = []

for md_file in Path(ROOT_DIR).rglob("*.md"):

    text = md_file.read_text(encoding="utf-8")

    # ------------------------------------------------------------------
    # Extract instrument title from first H1
    # ------------------------------------------------------------------

    title_match = re.search(
        r"^#\s+(.+)$",
        text,
        re.MULTILINE
    )

    instrument = (
        title_match.group(1).strip()
        if title_match
        else md_file.stem
    )

    # ------------------------------------------------------------------
    # Extract warning banner content
    # ------------------------------------------------------------------

    warning_match = re.search(
        r"\{\{\s*warning_banner_macro\(\)\s*\}\}\s*"
        r'<div class="collapsible-content">(.*?)</div>',
        text,
        re.DOTALL,
    )

    if not warning_match:
        continue

    warning_html = warning_match.group(1).strip()

    # scoring_match = re.search(
    #     r"\{\{\s*scoring_banner_macro\(\)\s*\}\}\s*"
    #     r'<div class="collapsible-content">(.*?)</div>',
    #     text,
    #     re.DOTALL,
    # )

    # if not scoring_match:
    #     continue

    # scoring_html = scoring_match.group(1).strip()

    # ------------------------------------------------------------------
    # Preserve useful HTML while cleaning container tags
    # ------------------------------------------------------------------

    # Convert paragraph boundaries to blank lines
    warning_html = re.sub(
        r"</p>\s*<p>",
        "\n\n",
        warning_html,
        flags=re.IGNORECASE,
    )

    # scoring_html = re.sub(
    #     r"</p>\s*<p>",
    #     "\n\n",
    #     scoring_html,
    #     flags=re.IGNORECASE,
    # )

    # Remove opening/closing paragraph tags
    warning_html = re.sub(
        r"</?p>",
        "",
        warning_html,
        flags=re.IGNORECASE,
    )

    # scoring_html = re.sub(
    #     r"</?p>",
    #     "",
    #     scoring_html,
    #     flags=re.IGNORECASE,
    # )

    # Remove any div wrappers
    warning_html = re.sub(
        r"</?div[^>]*>",
        "",
        warning_html,
        flags=re.IGNORECASE,
    )

    # scoring_html = re.sub(
    #     r"</?div[^>]*>",
    #     "",
    #     scoring_html,
    #     flags=re.IGNORECASE,
    # )

    warning_html = warning_html.strip()
    # scoring_html = scoring_html.strip()


    results.append(
        {
            "instrument": instrument,
            # "file": str(md_file),
            "warning": warning_html
            # "scoring": scoring_html,
        }
    )

# ----------------------------------------------------------------------
# Export CSV
# ----------------------------------------------------------------------

df = pd.DataFrame(results)

df.to_csv(
    "instrument_warnings.csv",
    index=False,
)

print(f"Found {len(df)} warnings")
print("Saved: instrument_warnings.csv")