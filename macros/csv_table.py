import csv
import html
from pathlib import Path

# mainly used for ERICA at the moment

def define_env(env):

    @env.macro
    def csv_table(
        csv_file,
        title=None,
        row_colors=None,
        note=None,
        table_class="table-no-vertical-lines",
    ):
        """Render a CSV file as an HTML table with optional styling."""

        csv_path = (
            Path(env.project_dir)
            / "docs/resources/tables"
            / csv_file
        )

        with csv_path.open("r", encoding="utf-8", newline="") as f:
            reader = csv.reader(f)
            rows = list(reader)

        if not rows:
            return ""

        headers = rows[0]
        data_rows = rows[1:]
        num_columns = len(headers)

        # Optional spanning title row
        title_row = ""
        if title:
            title_row = f"""
<tr>
<th colspan="{num_columns}">
<b>{html.escape(title)}</b>
</th>
</tr>
"""

        # Regular column headers
        headings = "".join(
            f"<th>{html.escape(header)}</th>"
            for header in headers
        )

        # Optional row colors:
        body_rows = []

        for i, row in enumerate(data_rows):
            style = ""

            if row_colors:
                for color, indices in row_colors.items():
                    if i in indices:
                        style = f' style="background-color: {html.escape(color)};"'
                        break

            cells = "".join(
                f"<td>{html.escape(cell)}</td>"
                for cell in row
            )

            body_rows.append(
                f"<tr{style}>{cells}</tr>"
            )

        body = "\n".join(body_rows)

        # Optional spanning footer/note
        note_row = ""
        if note:
            note_row = f"""
<tr>
<td colspan="{num_columns}">
<i>{html.escape(note)}</i>
</td>
</tr>
"""

        return f"""
<table class="{html.escape(table_class)}">
<thead>
{title_row}
<tr>{headings}</tr>
</thead>
<tbody>
{body}
{note_row}
</tbody>
</table>
"""