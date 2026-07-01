from .utils import is_present, table_row

def build_data_warning_multi(instruments, instrument_ids):
    all_warning_sections = ""

    for inst_id in instrument_ids:
        inst = instruments.get(inst_id)
        if not inst:
            continue

        title = inst.get("warning1_title")
        text = inst.get("warning1")

        # Skip completely empty warnings
        if not title and not text:
            continue

        # Clean text only if present
        if text:
            text = text.replace("\n", "<br>")
        else:
            text = ""

        # Optional: avoid showing "None" as title
        if not title:
            title = ""

        inst_html = f"""
<div class="info-section-title">{title}</div>
<div class="info-section">{text}</div>
"""
        all_warning_sections += inst_html

    if not all_warning_sections:
        return ""

    return f"""
<div id="data-warning" class="banner data-warning" onclick="toggleCollapse(this)">
<span class="emoji">
    <i class="fas fa-exclamation-triangle"></i>
</span>
<span class="text-with-link">
    <span class="text">Data Warning</span>
    <a class="anchor-link" href="#data-warning" title="Copy link">
        <i class="fa-solid fa-link"></i>
    </a>
</span>
<span class="arrow">▸</span>
</div>

<div class="collapsible-content">
{all_warning_sections}
</div>
"""