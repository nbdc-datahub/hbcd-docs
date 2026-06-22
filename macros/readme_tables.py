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

    type_value = inst.get("type", "")
    duration = inst.get("duration")

    if duration:
        type_value = f"{type_value} ({duration})"

    target = inst.get("child_specific")
    if target:
        if target== 'Yes':
             type_value = f"{type_value} - <i>Child-specific</i>"
             
    return f"""
<table class="table-no-vertical-lines readme-intro">
<tbody>
{table_row("Full Name", full_name_value)}
{table_row("Table Name", inst.get("table_name"), code=True)}
{table_row("Concatenated Data", inst.get('concatenated'), code=True)}
{table_row("Construct", inst.get("construct"))}
{table_row("Type", type_value)}
{table_row("Study Visits", inst.get("visits"))}
{table_row("Quality Control", qc)}

</tbody>
</table>
"""



'''
# with child-specific as separate row:

target = inst.get("child_specific")
    if target:
        if target== 'Yes':
            target_value = "Child"
        elif target== 'No':
            target_value = "Parent/Caregiver"

#then add after Type in table:
{table_row("Target", target_value)}
'''