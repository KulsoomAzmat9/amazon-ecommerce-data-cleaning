import pandas as pd

# Load the raw file
df = pd.read_csv('data/amazon_orders_40_rows.csv')

print(f"Before cleaning: {len(df)} rows")

# 1. Clean extra spaces from text columns
text_columns = ['Product_Name', 'City', 'Status', 'Date']
for col in text_columns:
    df[col] = df[col].astype(str).str.strip()

# 2. Fix missing Date - replace empty and 'nan' strings
df['Date'] = df['Date'].replace(['', 'nan', 'None'], '2024-01-06')
df['Date'] = df['Date'].fillna('2024-01-06')

# 3. Remove fully duplicate rows OR duplicate product+price+date+city
df = df.drop_duplicates()
# Also remove duplicate orders with same Product, Price, Quantity, City, Date
df = df.drop_duplicates(subset=['Product_Name', 'Price', 'Quantity', 'City', 'Date'], keep='first')

# 4. Save cleaned file
df.to_csv('data/cleaned_amazon_orders.csv', index=False)

print(f"After cleaning: {len(df)} rows")
print(df.head(10))