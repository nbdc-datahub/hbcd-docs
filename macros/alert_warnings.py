from .utils import is_present, table_row

def build_alert_warning(inst):

    alert = inst.get("alert", "").replace("\n", "<br>")

    return f"""
<div id="alert" class="banner alert" onclick="toggleCollapse(this)">
<span class="emoji">
    <i class="fas fa-exclamation-circle"></i>
</span>
<span class="text-with-link">
    <span class="text">Responsible Use Warning</span>
    <a class="anchor-link" href="#alert" title="Copy link">
    <i class="fa-solid fa-link"></i>
    </a>
</span>
<span class="arrow">▸</span>
</div>

<div class="collapsible-content">
    {alert}
</div>
"""

