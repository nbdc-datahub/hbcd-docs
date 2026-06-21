from .utils import is_present, table_row

def build_alert_warning(inst):

    alert_sections = ""

    alert_nums = sorted(
        int(k.replace("alert", ""))
        for k in inst.keys()
        if k.startswith("alert")
        and k.replace("alert", "").isdigit()
    )

    for i in alert_nums:
        title = inst.get(f"alert{i}")
        text = inst.get(f"alert{i}_text")
        text = text.replace("\n", "<br>") 

        if not title and not text:
            continue

        # Preserve line breaks within single alerts
        # if text:
        #     text = text.replace("\n", "<br>") 

        title_html = f"""
<div class="info-section-title">
    {title}
</div>
""" if title else ""

        alert_sections += f"""
<div class="info-section">
{title_html}
<p>
    {text or ""}
</p>
</div>
"""

    if not alert_sections:
        return ""

    return f"""
<div id="data-alert" class="banner alert" onclick="toggleCollapse(this)">
<span class="emoji">
    <i class="fas fa-exclamation-triangle"></i>
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

{alert_sections}

</div>
"""