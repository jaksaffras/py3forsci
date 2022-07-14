import pandas as pd

df = pd.read_csv('../DATA/sales_records.csv')  # <.>

print(df.describe())  # <.>
print()

print(df.info())  # <.>
print()

print(df.head())  # <.>

print(df.iloc[:5].loc[:,['Item Type', 'Sales Channel', 'Units Sold']])

#  iloc[row, col]   # numeric index
#  loc(row, col]    # row/column labels

#       value or slice or list
print('-' * 60)

# print(df.describe(include='O'))

result = df[(df.Country.str.contains('and')) & (df['Item Type'] == 'Baby Food')].loc[:,['Country', 'Units Sold', 'Unit Price']]
result['total'] = result['Units Sold'] * result['Unit Price']

print(result)
