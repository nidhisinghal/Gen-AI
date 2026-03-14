import pandas as pd
from pathlib import Path

p = Path(r"c:\Users\Anuj\Downloads\AI Tester\Project\Project-003-RICEPOT-RESTBrokerAPITestCases\Rest Broker API Test Case Sheet.xlsx")
if not p.exists():
    print(f"File not found: {p}")
    raise SystemExit(1)

df = pd.read_excel(p, sheet_name=0)
pd.set_option('display.max_colwidth', None)

# Print header
cols = list(df.columns)
print(' | '.join(cols))

# Print rows
for _, row in df.iterrows():
    cells = [str(row[c]) if pd.notna(row[c]) else '' for c in cols]
    print(' | '.join(cells))
