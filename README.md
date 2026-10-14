Amazon E-Commerce Data Cleaning Project

Cleaned messy Amazon orders data and converted it into analysis-ready format.

Project Overview
Raw data had duplicate orders, inconsistent formatting, and unclean columns.
Cleaned it using Python (Pandas) for e-commerce analysis.

Files
data/amazon_orders_40_rows.csv- Raw Data (40 rows).
data/cleaned_amazon_orders.csv - Cleaned Data (34 rows)

Cleaning Done:

Removed 2 duplicate T-Shirt orders (1002, 1021)
Removed 4 rows with missing dates (1003, 1014, 1026, 1037)
Fixed 35+ product names with extra spaces (e.g. 'T-Shirt ' → 'T-Shirt')
Fixed 14 cities with extra spaces (e.g. ' Islamabad ' → 'Islamabad')
Standardized Product_Name to Title Case (CAP → Cap)

Result: 40 rows → 34 rows = 6 rows removed, all columns cleaned.

Tech Stack
Python
Pandas

sProject Structure
amazon-ecommerce-data-cleaning/
data/
amazon_orders_40_rows.csv
cleaned_amazon_orders.csv
scripts/
clean.py
requirements.txt
README.md


 How to Run:
bash
Install dependencies
pip install -r requirements.txt

Run cleaning script
python scripts/clean.py

Proof of Work:
terminal_output.png

What This Project Does

1. Removes duplicate orders
2. Cleans and formats data
3. Makes data ready for analysis and dashboard





