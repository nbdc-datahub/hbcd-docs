import re
import unicodedata
import markdown

def slugify_heading(text):
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"\s+", "-", text.strip())
    text = re.sub(r"-+", "-", text)
    return text

# CHECK IF VALUE IS PRESENT (not empty)
def is_present(value):
    return value is not None and str(value).strip() != ""

# Only include table row if value present
def optional_table_row(label, value, code=False):
    """Return a table row only when the value is present."""
    if not is_present(value):
        return ""

    return table_row(label, value, code=code)

# Don't render rows without values and define css classes where needed (i.e. for visits list)
def table_row(label, value, code=False):
    if not is_present(value):
        return ""
    if code:
        value = f"<code>{value}</code>"
    return f"<tr><td>{label}</td><td>{value}</td></tr>"


def format_text(value, html=False):
    if not is_present(value):
        return None

    value = str(value).strip()

    if not value:
        return None

    if html:
        return markdown.markdown(
            value,
            extensions=[
                "sane_lists",
                "nl2br",
            ],
        )

    return value