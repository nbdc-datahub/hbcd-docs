import re
import unicodedata

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

# Don't render rows without values and define css classes where needed (i.e. for visits list)
def table_row(label, value, code=False):
    if not is_present(value):
        return ""
    if code:
        value = f"<code>{value}</code>"
    return f"<tr><td>{label}</td><td>{value}</td></tr>"