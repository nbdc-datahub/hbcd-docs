from .utils import is_present, table_row

## REFERENCES BANNER
def ref_banner(
        banner_id="references",
        text="References",
        icon="fa-solid fa-book-open"
    ):
        return f"""
<div id="{banner_id}" class="banner" onclick="toggleCollapse(this)">
<span class="emoji">
    <i class="{icon}"></i>
</span>
<span class="text-with-link">
    <span class="text">{text}</span>
    <a class="anchor-link" href="#{banner_id}" title="Copy link">
    <i class="fa-solid fa-link"></i>
    </a>
</span>
<span class="arrow">▸</span>
</div>
"""

# GENERAL WARNING BANNER HEADER

def warning_banner(
        banner_id="data-warning",
        text="Data Warning",
        icon="fas fa-exclamation-triangle"
    ):
        return f"""
<div id="{banner_id}" class="banner {banner_id}" onclick="toggleCollapse(this)">
<span class="emoji">
    <i class="{icon}"></i>
</span>

<span class="text-with-link">
    <span class="text">{text}</span>

    <a class="anchor-link" href="#{banner_id}" title="Copy link">
    <i class="fa-solid fa-link"></i>
    </a>
</span>

<span class="arrow">▸</span>
</div>
"""

## GENERAL ALERT BANNER HEADER
def alert_banner(
        banner_id="alert",
        text="Responsible Use Warning",
        icon="fas fa-exclamation-circle"
    ):
        return f"""
<div id="{banner_id}" class="banner {banner_id}" onclick="toggleCollapse(this)">
<span class="emoji">
    <i class="{icon}"></i>
</span>

<span class="text-with-link">
    <span class="text">{text}</span>

    <a class="anchor-link" href="#{banner_id}" title="Copy link">
    <i class="fa-solid fa-link"></i>
    </a>
</span>

<span class="arrow">▸</span>
</div>
"""
    
## ISSUES BANNER
def issues_banner(
        icon="fas fa-bug"
    ):
        return f"""
<div class="banner">
<span class="emoji"><i class="{icon}"></i></span>
<span class="text">See <a href="/changelog/issues-updates/" target="_blank">Known Issues & Pending Updates</a> for issues that may affect data use.</span>
</div>
"""

## HBCD MODIFICATIONS BANNER
def mods_banner(
        banner_id="hbcd-mod",
        text="HBCD Modifications",
        icon="fa fa-gear"
    ):
        return f"""
<div id="{banner_id}" class="banner" onclick="toggleCollapse(this)">
<span class="emoji">
    <i class="{icon}"></i>
</span>
<span class="text-with-link">
    <span class="text">{text}</span>
    <a class="anchor-link" href="#{banner_id}" title="Copy link">
    <i class="fa-solid fa-link"></i>
    </a>
</span>
<span class="arrow">▸</span>
</div>
"""
    
## SCORING BANNER
def scoring_banner(
        banner_id="scoring",
        text="Scoring Procedures",
        icon="fa fa-calculator"
    ):
        return f"""
<div id="{banner_id}" class="banner" onclick="toggleCollapse(this)">
<span class="emoji">
    <i class="{icon}"></i>
</span>
<span class="text-with-link">
    <span class="text">{text}</span>
    <a class="anchor-link" href="#{banner_id}" title="Copy link">
    <i class="fa-solid fa-link"></i>
    </a>
</span>
<span class="arrow">▸</span>
</div>
"""
