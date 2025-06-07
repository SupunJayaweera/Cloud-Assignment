#!/usr/bin/env python3
import sys
import csv

reader = csv.reader(sys.stdin)
header = next(reader, None)  

for row in reader:
    try:
        city = row[5].strip()             #  'City' is at index 1
        sale_str = row[21].strip()          # Sale (Dollars)' is at index 21
        sale = float(sale_str.replace('$', '').replace(',', ''))
        print(f"{city}\t{sale}")
    except Exception:
        continue  