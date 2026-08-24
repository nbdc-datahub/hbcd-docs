from markdown import markdown
from .utils import (
    is_present,
    table_row,
    optional_table_row,
    format_text,
)

def define_env(env):

    # RESPONSIBLE USE WARNINGS
    @env.macro
    def alert_warning(inst):
        alert_sections = ""

        alert_nums = sorted(
            int(k.replace("alert", ""))
            for k in inst.keys()
            if k.startswith("alert")
            and k.replace("alert", "").isdigit()
        )

        for i in alert_nums:
            title = inst.get(f"alert{i}_title")
            text = inst.get(f"alert{i}")
            text = format_text(text, html=True)

            if not title and not text:
                continue

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
    <i class="fas fa-exclamation-circle"></i>
</span>
<span class="text-with-link">
    <span class="text">Responsible Use Warning</span>
    <a class="anchor-link" href="#data-alert" title="Copy link">
    <i class="fa-solid fa-link"></i>
    </a>
</span>
<span class="arrow">▸</span>
</div>
<div class="collapsible-content" style="background-color: #f9f2f3;">

{alert_sections}

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
<span class="text">See <a href="https://docs.hbcdstudy.org/latest/changelog/issues-updates/">Known Issues & Pending Updates</a> for issues that may affect data use.</span>
</div>
"""

    # DATA WARNINGS
    @env.macro
    def data_warning(inst):
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
            text = format_text(text, html=True)

            if not title and not text:
                continue

            title_html = f"""
<div class="info-section-title">{title}</div>
""" if title else ""

            warning_sections += f"""
<div class="info-section">
{title_html}
{text or ""}
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
<div class="collapsible-content" style="background-color: #fcfaed;">

{warning_sections}

</div>
"""

    # README TABLE
    @env.macro
    def readme_summary(inst):

        if inst.get("primary_data_type") == "Concatenated data":
            file_name_header = "Concatenated Data"
        else:
            file_name_header = "Table Name"

        versions = format_text(inst.get("versions"), html=True)
        visits = format_text(inst.get("visits"), html=True)
        construct = format_text(inst.get("construct"), html=True)
        qc = format_text(inst.get("qc"), html=True)

        full_name = inst.get("full_name")
        acronym = inst.get("acronym")

        if is_present(acronym):
            full_name = f"{full_name} ({acronym})"

        full_name = format_text(full_name, html=True)

        assessment_type = inst.get("assessment_type")
        mode = inst.get("administration")
        resp = inst.get("respondent_category")
        duration = inst.get("duration")

        base = assessment_type if is_present(assessment_type) else None

        details = []

        if is_present(resp):
            details.append(resp)

        if is_present(duration):
            details.append(str(duration))

        if details:
            detail_text = "; ".join(details)

            if base:
                base = f"{base} ({detail_text})"
            else:
                base = f"({detail_text})"

        if is_present(mode) and base:
            administration_summary = f"{mode} {base}"
        elif is_present(mode):
            administration_summary = mode
        else:
            administration_summary = base

        return f"""
<table class="table-no-vertical-lines readme-intro">
<tbody>
{optional_table_row("Name", full_name)}
{optional_table_row("Versions", versions)}
{optional_table_row(file_name_header, inst.get("table_name"), code=True)}
{optional_table_row("Construct", construct)}
{optional_table_row("Study Visits", visits)}
{optional_table_row("Type", administration_summary)}
{optional_table_row("Quality Control", qc)}
</tbody>
</table>
"""
    # INSTRUMENT DESCRIPTION
    @env.macro
    def instrument_description(inst):
        description=inst.get("description")
        return description

    @env.macro
    def suppx(inst, item):
        supplemental = inst.get(f"supp{item}_text")
        supplemental = format_text(supplemental)
        return supplemental

    @env.macro
    def qc(inst):
        qc = inst.get("qc")
        return qc

    @env.macro
    def resources(inst):
        resources=inst.get("resources")
        resources = format_text(resources, html=True)
        return resources

    @env.macro
    def scoring_contents(inst):
        scoring=inst.get("scoring")
        scoring = format_text(scoring, html=True)
        return scoring

    @env.macro
    def references(inst):
        references = inst.get("references", "")

        if not is_present(references):
            return ""

        # One reference per line
        refs = [
            markdown(ref.strip())
            for ref in references.splitlines()
            if ref.strip()
        ]

        refs_html = "\n".join(f"<p>{ref}</p>" for ref in refs)

        return f"""
<div id="references" class="banner" onclick="toggleCollapse(this)">
<span class="emoji">
    <i class="fa-solid fa-book-open"></i>
</span>
<span class="text-with-link">
    <span class="text">References</span>
    <a class="anchor-link" href="#references" title="Copy link">
        <i class="fa-solid fa-link"></i>
    </a>
</span>
<span class="arrow">▸</span>
</div>

<div class="collapsible-content">
<div class="references">
{refs_html}
</div>
</div>
"""

    # HBCD MODS
    @env.macro
    def hbcd_mods(inst):

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
            text = format_text(text, html=True)
            
            if not title and not text:
                continue
            
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

    # SCORING
    @env.macro
    def scoring(inst):
        scoring = inst.get("scoring")
        if not is_present(scoring):
            return ""
        scoring = format_text(scoring, html=True)

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
<div class="collapsible-content" markdown="1">
{scoring}
</div>
"""