from .utils import is_present, table_row

def build_scoring(inst):

    scoring = inst.get("scoring", "")

    if not scoring:
        return ""
    
    else:
        scoring = scoring.replace("\n", "<br>")  # Preserve line breaks in text
        return f"""
<div id="scoring" class="banner" onclick="toggleCollapse(this)">
<span class="emoji">
    <i class="fa fa-calculator"></i>
</span>
<span class="text-with-link">
    <span class="text">Scoring Procedures</span>
    <a class="anchor-link" href="#scoring" title="Copy link">
    <i class="fa-solid fa-link"></i>
    </a>
</span>
<span class="arrow">▸</span>
</div>

<div class="collapsible-content">
<p>
    {scoring}
</p>
</div>
"""

