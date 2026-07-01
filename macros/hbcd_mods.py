from .utils import is_present, table_row

def build_hbcd_mods(inst):

    hbcd_mods_sections = ""

    hbcd_mods_nums = sorted(
        int(k.replace("hbcd_mods", ""))
        for k in inst.keys()
        if k.startswith("hbcd_mods")
        and k.replace("hbcd_mods", "").isdigit()
    )

    for i in hbcd_mods_nums:
        title = inst.get(f"hbcd_mods{i}_title")
        text = inst.get(f"hbcd_mods{i}")
        
        if not title and not text:
            continue

        # Preserve line breaks in text
        if text:
            text = text.replace("\n", "<br>")

        title_html = f"""
<div class="info-section-title">
    {title}
</div>
""" if title else ""

        hbcd_mods_sections += f"""
<div class="info-section">
{title_html}
<p>
    {text or ""}
</p>
</div>
"""

    if not hbcd_mods_sections:
        return ""

    return f"""
<div id="hbcd_mods" class="banner" onclick="toggleCollapse(this)">
<span class="emoji">
     <i class="fa fa-gear"></i>
</span>
<span class="text-with-link">
    <span class="text">HBCD Modifications</span>
    <a class="anchor-link" href="#hbcd_mods" title="Copy link">
    <i class="fa-solid fa-link"></i>
    </a>
</span>
<span class="arrow">▸</span>
</div>
<div class="collapsible-content">

{hbcd_mods_sections}

</div>
"""