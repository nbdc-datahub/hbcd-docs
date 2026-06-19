from .utils import is_present, table_row

def build_readme(inst):

    form_html = ""

    if is_present(inst.get("form_link")):
        form_html = f"""
<a href="{inst.get('form_link')}" class="button-link">
  View Questionnaire
</a>
"""

    return f"""
<table class="table-no-vertical-lines-compact readme-table">
<tbody>

{table_row("Table Name", inst.get("table_name"), code=True)}
{table_row("Acronym", inst.get("acronym"))}
{table_row("Type (Duration)", f"{inst.get('type')} ({inst.get('duration')})")}
{table_row("Response format", inst.get("responses"))}
{table_row("Number of Items", inst.get("total_items"))}

</tbody>
</table>

{form_html}
"""