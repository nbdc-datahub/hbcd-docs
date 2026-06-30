from .utils import is_present, table_row

def build_readme(inst):

    # for QC info, convert to list if there are multiple lines
    qc = inst.get("qc")
    if isinstance(qc, list):
        qc = "<ul>" + "".join(
            f"<li>{item}</li>"
            for item in qc
        ) + "</ul>"

    full_name_value = inst.get("full_name")
    acronym = inst.get("acronym")

    if acronym:
        full_name_value = f"{full_name_value} ({acronym})"

    # Preserve line breaks for visits (rare cases)
    # visits = inst.get("visits")
    # if visits:
    #     visits = visits.replace("\n", "<br>")


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
{table_row("Table Name", inst.get("table_name"), code=True)}
{table_row("Concatenated Data", inst.get('concatenated'), code=True)}
{table_row("Construct", inst.get("construct"))}
{table_row("Study Visits", inst.get("visits"))}
{table_row("Type", administration_summary)}
{table_row("Quality Control", qc)}

</tbody>
</table>
"""
