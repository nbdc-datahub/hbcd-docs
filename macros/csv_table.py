import csv
import html
from pathlib import Path

# Mainly used for ERICA and Static/Dynamic tables.
# outputs to data/tables

def format_cell(cell):
    """Escape HTML and preserve line breaks within CSV cells."""
    escaped = html.escape(cell)

    return (
        escaped
        .replace("\r\n", "\n")
        .replace("\r", "\n")
        .replace("\n", "<br>")
    )

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
            / "data/"
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

        # Optional spanning title row.
        title_row = ""

        if title:
            title_row = f"""
<tr>
<th colspan="{num_columns}">
<b>{html.escape(title)}</b>
</th>
</tr>
"""

        # Regular column headers.
        headings = "".join(
            f"<th>{html.escape(header)}</th>"
            for header in headers
        )

        # Table body with optional row colors.
        body_rows = []

        for row_index, row in enumerate(data_rows):
            style = ""

            if row_colors:
                for color, indices in row_colors.items():
                    if row_index in indices:
                        safe_color = html.escape(
                            str(color),
                            quote=True,
                        )
                        style = (
                            f' style="background-color: {safe_color};"'
                        )
                        break

            # cells = "".join(
            #     f"<td>{html.escape(cell)}</td>"
            #     for cell in row
            # )
            cells = "".join(
                f"<td>{format_cell(cell)}</td>"
                for cell in row
)

            body_rows.append(
                f"<tr{style}>{cells}</tr>"
            )

        body = "\n".join(body_rows)

        # Optional spanning footer/note.
        note_row = ""

        if note:
            note_row = f"""
<tr>
<td colspan="{num_columns}">
<i>{html.escape(note)}</i>
</td>
</tr>
"""

        safe_table_class = html.escape(
            table_class,
            quote=True,
        )

        return f"""
<table class="{safe_table_class}">
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