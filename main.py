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
{row("Construct", inst.get("construct"))}
{row("Type", inst.get("administration"))}
{row("Study Visits", inst.get("visits"), value_class="visit-list")}
{row("Quality Control", inst.get("qc"))}

</tbody>
</table>
"""



# Administration details (respondent, method, duration) are not currently included in the table, but could be added back in if desired. If so, would need to add to YAML file and then add rows here similar to the other fields.
# admin = f"""
# <b>Respondent</b>: {inst.get('respondent')}<br>
# <b>Method</b>: {inst.get('method')}
# """