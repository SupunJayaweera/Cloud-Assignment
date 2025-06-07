#!/usr/bin/env python3
import sys

current_key = None
total_sales = 0.0

for line in sys.stdin:
    line = line.strip()
    if not line or '\t' not in line:
        continue  # Skip blank or malformed lines

    try:
        key, sale = line.split("\t")
        sale = float(sale)
    except ValueError:
        continue  # Skip if conversion fails

    if current_key == key:
        total_sales += sale
    else:
        if current_key is not None:
            print(f"{current_key}\t{total_sales}")
        current_key = key
        total_sales = sale

if current_key is not None:
    print(f"{current_key}\t{total_sales}")
