from .utils import is_present, table_row

def build_data_warning_multi(instruments, instrument_ids):
    all_warning_sections = ""

    for inst_id in instrument_ids:
        inst = instruments.get(inst_id)
        if not inst:
            continue

        warning_sections = ""

        warning_nums = sorted(
            int(k.replace("warning", ""))
            for k in inst.keys()
            if k.startswith("warning")
            and k.replace("warning", "").isdigit()
        )

        for i in warning_nums:
            title = inst.get(f"warning{i}_title")
            text = inst.get(f"warning{i}")

            if not title and not text:
                continue

            if text:
                text = text.replace("\n", "<br>")

            title_html = f"""
<div class="info-section-title">
    {title}
</div>
""" if title else ""

            warning_sections += f"""
<div class="info-section">
{title_html}
<p>{text or ""}</p>
</div>
"""
        if warning_sections:
            all_warning_sections += f"""
<div class="instrument-warning-group">
{warning_sections}
</div>
"""

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