import pandas as pd
import json
json_file_path = 'large.json'
with open(json_file_path, 'r', encoding='utf-8-sig') as f:
    data = json.load(f)
    print(data) 
df = pd.DataFrame(data)

csv_file_path = 'output.csv'

df.to_csv(csv_file_path, index=False)

print(f"Conversion successful. CSV file saved at {csv_file_path}")
