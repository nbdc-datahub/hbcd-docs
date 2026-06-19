from .utils import is_present, table_row


def build_readme(inst):

    qc = inst.get("qc")

    if qc:
        qc_items = [
            f"<li>{item.strip()}</li>"
            for item in qc.split(";")
            if item.strip()
        ]
        qc = f"<ul>{''.join(qc_items)}</ul>"

    return f"""
<table class="table-no-vertical-lines readme-intro">
<tbody>

{table_row("Table Name", inst.get("table_name"), code=True)}
{table_row("Concatenated Data", inst.get('file_tree'), code=True)}
{table_row("Construct", inst.get("construct"))}
{table_row("Type (Duration)", f"{inst.get('type')} ({inst.get('duration')})")}
{table_row("Study Visits", inst.get("visits"))}
{table_row("Quality Control", qc)}

</tbody>
</table>
"""