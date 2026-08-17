import csv
import html
from pathlib import Path

def define_env(env):

    @env.macro
    def csv_table(csv_file):
        """Render a CSV file as an HTML table."""

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
        headings = "".join(
            f"<th>{header}</th>"
            for header in headers
        )

        body = "".join(
            "<tr>"
            + "".join(
                f"<td>{html.escape(cell)}</td>"
                for cell in row
            )
            + "</tr>"
            for row in data_rows
        )

        return f"""
<table class="table-no-vertical-lines">
<thead>
<tr>{headings}</tr>
</thead>
<tbody>
{body}
</tbody>
</table>
"""