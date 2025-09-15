import os
import csv

# Root directory where your markdown files are stored
ROOT_DIR = "../docs/instruments"

WARNING_SNIPPET = '<div id="warning"'
ALERT_SNIPPET = '<div id="alert"'

results = []

for root, _, files in os.walk(ROOT_DIR):
    for file in files:
        if file.endswith(".md"):
            filepath = os.path.join(root, file)
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
                    has_warning = WARNING_SNIPPET in content
                    has_alert = ALERT_SNIPPET in content

                    if has_warning and has_alert:
                        status = "Both"
                    elif has_warning:
                        status = "Data Warning"
                    elif has_alert:
                        status = "Responsible Use Warning"
                    else:
                        status = "None"

                    results.append((filepath, status))
            except Exception as e:
                print(f"Could not read {filepath}: {e}")

# Write results to CSV file
output_file = "markdown_warnings.csv"
with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Filepath", "Status"])
    writer.writerows(results)

print(f"Results written to {output_file}")


'''
import os

# Root directory where your markdown files are stored
ROOT_DIR = "../docs/instruments"

# Text snippets to look for
WARNING_SNIPPET = '<div id="warning"'
ALERT_SNIPPET = '<div id="alert"'

warning_files = []
alert_files = []

for root, _, files in os.walk(ROOT_DIR):
    for file in files:
        if file.endswith(".md"):
            filepath = os.path.join(root, file)
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
                    if WARNING_SNIPPET in content:
                        warning_files.append(filepath)
                    if ALERT_SNIPPET in content:
                        alert_files.append(filepath)
            except Exception as e:
                print(f"Could not read {filepath}: {e}")

# Print results
print("=== Files with Data Warning ===")
for f in warning_files:
    print(f)

print("\n=== Files with Responsible Use Warning ===")
for f in alert_files:
    print(f)
'''