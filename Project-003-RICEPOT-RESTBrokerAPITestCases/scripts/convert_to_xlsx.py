import pandas as pd
from pathlib import Path

src = Path(r"c:\Users\Anuj\Downloads\AI Tester\Project\Project-003-RICEPOT-RESTBrokerAPITestCases\Rest Broker API Test Case Sheet.xlsx")
# Read pipe-delimited text file (header row present)
text = src.read_text(encoding='utf-8')
lines = [l for l in text.splitlines() if l.strip()]
rows = []
for i, line in enumerate(lines):
    # split into 14 columns max (13 splits)
    parts = line.split(' | ', 13)
    rows.append(parts)

# First row is header
header = rows[0]
data = rows[1:]
# Ensure all rows have same length as header
for r in data:
    if len(r) < len(header):
        # pad with empty strings
        r.extend([''] * (len(header) - len(r)))

df = pd.DataFrame(data, columns=header)
# Write to native xlsx (overwrite)
dst = src
with pd.ExcelWriter(dst, engine='openpyxl') as writer:
    df.to_excel(writer, index=False, sheet_name='TestCases')

print(f"Wrote native xlsx to: {dst}")
