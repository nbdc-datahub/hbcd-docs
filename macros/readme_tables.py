from .utils import is_present, table_row

def build_readme(inst):

    # Multiple versions - check for multiple versions by checking for presence of value in version1 cell
    version1 = inst.get("version1")

    if version1:
        version2 = inst.get("version2")
        version1_table = inst.get("table_version1")
        version2_table = inst.get("table_version2")

        table_name = (
            f"{version1}: <code>{version1_table}</code><br>"
            f"{version2}: <code>{version2_table}</code>"
        )
                
        visits_version1 = inst.get("visits_version1")
        visits_version2 = inst.get("visits_version2")

        visits  = f"""
        {version1}: {visits_version1}
        <br>
        {version2}: {visits_version2}
        """
    else:
        raw_table = inst.get("table_name")
        table_name = f"<code>{raw_table}</code>"
        visits = inst.get("visits")
         
    # for QC info, convert to list if there are multiple lines
    qc = inst.get("qc")
    if isinstance(qc, list):
        qc = "<ul>" + "".join(
            f"<li>{item}</li>"
            for item in qc
        ) + "</ul>"

    full_name_value = inst.get("full_name")

    # In rare instances where multiple instruments listed (separated by line breaks), convert to list (for IBQ-R and ECBQ)
    if isinstance(full_name_value, list):
        full_name_value = "<ul>" + "".join(
            f"<li>{item}</li>"
            for item in full_name_value
        ) + "</ul>"

    # Preserve line breaks for full_name column in rare instances (e.g. IBQ-R)
    # full_name_value = full_name_value.replace("\n", "<br>")
    
    acronym = inst.get("acronym")
    if acronym:
        full_name_value = f"{full_name_value} ({acronym})"

    # Type field summary
    assessment_type = inst.get("assessment_type") # Questionnaire, interview, etc.
    mode = inst.get("administration") # remote or in-person
    resp = inst.get("respondent_category") # Parent on Child, Parent on Self, etc.
    duration = inst.get("duration") # X min 

    # Build base: Type
    parts = []
    if assessment_type:
        base = assessment_type
    else:
        base = None

    # Add respondent info 
    details = []
    if resp:
        details.append(resp)
    if duration:
        details.append(f"{duration}")
    if details:
        base = f"{base} ({'; '.join(details)})" if base else f"({'; '.join(details)})"
    
    # Add mode as prefix
    if mode and base:
        administration_summary = f"{mode} {base}"
    elif mode:
        administration_summary = mode
    else:
        administration_summary = base or ""

    # eg Remote Questionnaire (Parent on Child; 4-8 min duration)
    
    return f"""
<table class="table-no-vertical-lines readme-intro">
<tbody>
{table_row("Full Name", full_name_value)}
{table_row("Table Name", table_name)}
{table_row("Concatenated Data", inst.get('concatenated'), code=True)}
{table_row("Construct", inst.get("construct"))}
{table_row("Study Visits", visits)}
{table_row("Type", administration_summary)}
{table_row("Quality Control", qc)}

</tbody>
</table>
"""

# {table_row("Full Name", full_name_value)}
# {table_row("Versions", versions)}
# {table_row("Table Name", inst.get("table_name"), code=True)}
# {table_row("Concatenated Data", inst.get('concatenated'), code=True)}
# {table_row("Construct", inst.get("construct"))}
# {table_row("Study Visits", inst.get("visits"))}
# {table_row("Type", administration_summary)}
# {table_row("Quality Control", qc)}


    # if isinstance(versions, list):
    #     versions = "<ul>" + "".join(
    #         f"<li>{item}</li>"
    #         for item in versions
    #     ) + "</ul>"

    #     {table_row("Table Name", inst.get("table_name"), code=True)}