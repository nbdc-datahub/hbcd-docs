from .utils import is_present, table_row

def build_data_warning(inst):

    warning_sections = ""

    warning_nums = sorted(
        int(k.replace("warning", ""))
        for k in inst.keys()
        if k.startswith("warning")
        and k.replace("warning", "").isdigit()
    )

    for i in warning_nums:
        title = inst.get(f"warning{i}")
        text = inst.get(f"warning{i}_text")

        if not title and not text:
            continue

        warning_sections += f"""
<div class="info-section">
<div class="info-section-title">
    {title or ""}
</div>
<p>
    {text or ""}
</p>
</div>
"""

    if not warning_sections:
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

{warning_sections}

</div>
"""