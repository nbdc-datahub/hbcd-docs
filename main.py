import yaml
import os
import textwrap

def define_env(env):

    # Path to YAML file & make available in templates
    data_path = os.path.join(env.project_dir, "docs", "data", "instruments.yml")

    with open(data_path, "r") as f:
        instruments = yaml.safe_load(f)

    env.variables["instruments"] = instruments

    # CHECK IF VALUE IS PRESENT (not empty)
    def is_present(val):
        return val is not None and str(val).strip() != ""

    # Don't render rows without values and define css classes where needed (i.e. for visits list)
    def row(label, value, code=False, value_class=None):
        if not is_present(value):
            return ""
        if code:
            value = f"<code>{value}</code>"
        class_attr = f' class="{value_class}"' if value_class else ""
        return f"<tr><td>{label}</td><td{class_attr}>{value}</td></tr>"

## INSTRUMENT OVERVIEW TABLES AT TOP OF README PAGES
    @env.macro
    def overview_table(inst):

        return f"""
<table class="table-no-vertical-lines readme-intro">
<tbody>

{row("Table Name", inst.get("table_name"), code=True)}
{row("Concatenated Data", inst.get('file_tree'), code=True)}
{row("Construct", inst.get("construct"))}
{row("Type", inst.get("administration"))}
{row("Study Visits", inst.get("visits"), value_class="visit-list")}
{row("Quality Control", inst.get("qc"))}

</tbody>
</table>
"""
    
## WARNING BANNER - INSTRUMENT-SPECIFIC
    @env.macro
    def warning_banner_FULL(inst):
        return f"""
<div id="warn" class="banner data-warning" onclick="toggleCollapse(this)">
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

<div class="info-section">
<div class="info-section-title">
    {inst.get("warning1")}
</div>
<p>
  {inst.get("warning1_text")}
</p>
</div>

<div class="info-section">
<div class="info-section-title">
    {inst.get("warning2")}
</div>
<p>
  {inst.get("warning2_text")}
</p>
</div>

<div class="info-section">
<div class="info-section-title">
    {inst.get("warning3")}
</div>
<p>
  {inst.get("warning3_text")}
</p>
</div>

<div class="info-section">
<div class="info-section-title">
    {inst.get("warning4")}
</div>
<p>
  {inst.get("warning4_text")}
</p>
</div>

</div>
"""
        

## DATA WARNING BANNER - GENERAL
    @env.macro
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
    
## ALERT BANNER
    @env.macro
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
    
## HBCD MODIFICATIONS BANNER
    @env.macro
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
    
## HBCD MODIFICATIONS BANNER
    @env.macro
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
    
## ISSUES BANNER
    @env.macro
    def issues_banner(
        icon="fas fa-bug"
    ):
        return f"""
<div class="banner">
<span class="emoji"><i class="{icon}"></i></span>
<span class="text">See <a href="/changelog/issues-updates/" target="_blank">Known Issues & Pending Updates</a> for issues that may affect data use.</span>
</div>
"""
    

   