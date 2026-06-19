from macros.utils import slugify_heading, is_present

def battery_match(instrument, battery):
    """
    Return True if the instrument should be included.
    """
    return battery is None or instrument.get("battery") == battery


# Build tables for all instruments within a given battery
def build_all_instruments_table(instruments, battery=None):

    rows = []
    seen_domains = set()

    for instrument in instruments.values():
        if not battery_match(instrument, battery):
            continue
        domain = instrument.get("domain", "")
        if not domain or domain in seen_domains:
            continue
        seen_domains.add(domain)
        domain_slug = slugify_heading(domain)

        rows.append(f"""
<tr class="domain-header open" data-domain="{domain_slug}">
  <td colspan="4">
    <span class="chevron">▸</span>{domain}
  </td>
</tr>
""")
        for child in instruments.values():
            if child.get("domain") != domain:
                continue
            if not battery_match(child, battery):
                continue

            type_duration = child.get("type", "")
            if is_present(child.get("duration")):
                type_duration += f" ({child.get('duration')})"

            measure = child.get("measure", "")
            measure_slug = slugify_heading(measure)

            if child.get("battery") == "Infant":
                href=f"../readmes/infant-batteries/#{measure_slug}"
            elif child.get("battery") == "Biomarkers & Remote":\
                href=f"../readmes/biomarkers/#{domain_slug}"
            else:
                href=f"../readmes/{domain_slug}/#{measure_slug}"

            rows.append(f"""
<tr class="domain {domain_slug}">
  <td>
    <a href="{href}" target="_blank">
      {measure}
    </a>
  </td>
  <td>{child.get("acronym", "")}</td>
  <td>{type_duration}</td>
  <td><code>{child.get("table_name", "")}</code></td>
</tr>
""")

    return f"""
<table class="table-no-vertical-lines expandable-table">
<thead>
<tr>
  <th>Assessment (By Domain)</th>
  <th>Acronym</th>
  <th>Type (Duration)</th>
  <th>Table Name</th>
</tr>
</thead>
<tbody>
{''.join(rows)}
</tbody>
</table>
"""


def build_domain_table(instruments, domain, battery=None):

    rows = []

    for instrument in instruments.values():

        if instrument.get("domain") != domain:
            continue

        if not battery_match(instrument, battery):
            continue

        measure = instrument.get("measure", "")
        slug = slugify_heading(measure)
        acronym = instrument.get("acronym") or ""

        # Type + duration
        type_duration = instrument.get("type", "")

        if is_present(instrument.get("duration")):
            type_duration += f" ({instrument.get('duration')})"

        # Scoring indicator
        scoring = (
            '<i class="fa-solid fa-circle-check icon-check"></i>'
            if instrument.get("scoring") == "YES"
            else "--"
        )

        rows.append(f"""
<tr>
<td><a href="#{slug}">{measure}</a></td>
<td>{acronym}</td>
<td>{type_duration}</td>
<td style="text-align:center;">{scoring}</td>
<td><code>{instrument.get("table_name", "")}</code></td>
</tr>
""")

    return f"""
<table class="table-no-vertical-lines-compact expandable-table">
<thead>
<tr>
  <th>Assessment</th>
  <th>Acronym</th>
  <th>Type (Duration)</th>
  <th style="text-align:center;">Scoring</th>
  <th>Table Name</th>
</tr>
</thead>
<tbody>
{''.join(rows)}
</tbody>
</table>
"""