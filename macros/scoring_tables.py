import os

from .utils import is_present, table_row

def build_scoring_table(inst):

    proprietary_note = ""

    if inst.get("proprietary") == "YES":
        proprietary_note = "<b><i>Instrument is proprietary</i></b>"

    script_row = ""

    if is_present(inst.get("scoring_script")):

        script_name = os.path.basename(
            inst.get("scoring_script")
        )

        script_row = f"""
<tr>
<td>Scoring Script</td>
<td>
<a href="{inst.get('scoring_script')}">
<code>{script_name}</code>
</a>
</td>
</tr>
"""

    return f"""
<details class="admonition info" open>
<summary><strong>Scoring Procedures</strong></summary>

<p>{proprietary_note}</p>

<table class="table-no-vertical-lines-compact readme-table">
<tbody>

{script_row}
{table_row("Scale", inst.get("scale"))}
{table_row("Summary Scores", inst.get("score_types"))}
{table_row("Items Excluded From Scoring", inst.get("excluded_from_scoring"), code=True)}
{table_row("Reverse-scored items", inst.get("reverse_coded"), code=True)}
{table_row("Branching Logic", inst.get("branching_logic"))}
{table_row("Cutoff score", inst.get("cutoff"))}
{table_row("Missingness", inst.get("missingness"))}

</tbody>
</table>

</details>
"""