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

    assessment_type_value = inst.get("assessment_type", "")
    respondent_category_value = inst.get("respondent_category", "")
    duration = inst.get("duration")

    # if duration:
    #     type_value = f"{type_value} ({duration})"

    administration = f"{assessment_type_value} ({respondent_category_value}, {duration})"
             
    return f"""
<table class="table-no-vertical-lines readme-intro">
<tbody>
{table_row("Full Name", full_name_value)}
{table_row("Table Name", inst.get("table_name"), code=True)}
{table_row("Concatenated Data", inst.get('concatenated'), code=True)}
{table_row("Construct", inst.get("construct"))}
{table_row("Study Visits", inst.get("visits"))}
{table_row("Type", administration)}
{table_row("Quality Control", qc)}

</tbody>
</table>
"""
