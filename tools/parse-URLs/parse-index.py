from bs4 import BeautifulSoup
import csv

with open("temp.html", "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")
rows = soup.select("tbody tr")

output = []
last_url = None

for row in rows:
    cells = row.find_all("td")
    if not cells:
        continue

    # Instrument Name link (may be missing due to rowspan)
    link_tag = cells[0].find("a")
    if link_tag:
        last_url = link_tag.get("href")

    # Table Name (always in <code>)
    table_name = cells[-1].find("code").get_text(strip=True)

    output.append([last_url, table_name])

# Write CSV
with open("instrument_table_map.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Instrument_URL", "Table_Name"])
    writer.writerows(output)
