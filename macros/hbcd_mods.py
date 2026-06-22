from .utils import is_present, table_row

def build_hbcd_mods(inst):

    hbcd_mods = inst.get("hbcd_mods", "")

    if not hbcd_mods:
        return ""
    
    else:
        hbcd_mods = hbcd_mods.replace("\n", "<br>")  # Preserve line breaks in text
        return f"""
<div id="hbcd-mods" class="banner" onclick="toggleCollapse(this)">
<span class="emoji">
    <i class="fa fa-gear"></i>
</span>
<span class="text-with-link">
    <span class="text">HBCD Modifications</span>
    <a class="anchor-link" href="#hbcd-mods" title="Copy link">
    <i class="fa-solid fa-link"></i>
    </a>
</span>
<span class="arrow">▸</span>
</div>

<div class="collapsible-content">
<p>
    {hbcd_mods}
</p>
</div>
"""

