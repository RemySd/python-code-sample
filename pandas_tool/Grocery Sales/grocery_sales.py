# import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# display plots in the Jupyter notebook

# import datasets (you may have to change the directory/file names)
# note the encoding option to deal with a read error!
cities = pd.read_csv('./cities.csv', encoding = 'ISO-8859-1', engine='python')
customers = pd.read_csv('./customers.csv', encoding = 'ISO-8859-1', engine='python')
item_master = pd.read_csv('./item_master.csv', encoding = 'ISO-8859-1', engine='python')
sales = pd.read_csv('./sales.csv', encoding = 'ISO-8859-1', engine='python')
sales_rep = pd.read_csv('./sales_rep.csv', encoding = 'ISO-8859-1', engine='python')

# as an example, print the first rows of sales using the head() method
print(sales.head(5))

print('Null Values by Column - \'cities\' Dataset')
print(cities.isnull().sum())
print(cities.dtypes)
cities["Desc"] = cities["Desc"].fillna("no desc")

print('Null Values by Column - \'customers\' Dataset')
print(customers.isnull().sum())
print(customers.dtypes)

print('Null Values by Column - \'item_master\' Dataset')
print(item_master.isnull().sum())
print(item_master.dtypes)

print('Null Values by Column - \'sales\' Dataset')
print(sales.isnull().sum())
print(sales.dtypes)


sales["Date"] = pd.to_datetime(sales["Date"])
sales["Invoice Date"] = pd.to_datetime(sales["Date"])
sales["Promised Delivery Date"] = pd.to_datetime(sales["Date"])

print(sales.dtypes)


print('Null Values by Column - \'sales_rep\' Dataset')
print(sales_rep.isnull().sum())
print(sales_rep.dtypes)
sales_rep["Sales Rep Name2"] = sales_rep["Sales Rep Name2"].fillna("no name 2")
sales_rep["Sales Rep Name3"] = sales_rep["Sales Rep Name3"].fillna("no name 3")


customers_cities = pd.merge(customers, cities, left_on="City Code", right_on="City Code")

final_df = pd.merge(sales, customers_cities, left_on="Customer Number", right_on="Customer Number")
final_df = pd.merge(final_df, item_master, left_on="Item Number", right_on="Item Number")
final_df = pd.merge(final_df, sales_rep, left_on="Sales Rep Number", right_on="Sales Rep ID")


fig, ax = plt.subplots(figsize=(10, 5))
grouped_data = final_df.groupby(by=["Region"]).sum().sort_values('Sales', ascending = False)['Sales'] # <- complete this line
grouped_data.plot(ax = ax, kind = 'bar')
plt.title('Total Sales ($) By Region')
plt.show()

# regional sales over time
fig, ax = plt.subplots(figsize=(10, 5))
final_df.groupby([pd.Grouper(key='Date', freq='Y'), 'Region'])['Sales'].sum().unstack().plot(ax = ax, kind = 'bar')
plt.title('Annual Sales ($) By Region')
plt.show()

# total sales by product group
fig, ax = plt.subplots(figsize=(10, 5))
grouped_data = final_df.groupby(["Product Group"]).sum().sort_values('Sales', ascending = False)['Sales'] # <- complete this line
grouped_data.plot(ax = ax, kind = 'bar')
plt.title('Total Sales ($) By Product Group')
plt.show()

# product group sales over time
fig, ax = plt.subplots(figsize=(15, 8))
final_df.groupby([pd.Grouper(key='Date', freq='Y'), 'Product Group'])['Sales'].sum().unstack().plot(ax = ax, colormap = 'tab20')
plt.title('Annual Sales ($) By Product Group')
plt.show()

# total sales by manager
fig, ax = plt.subplots(figsize=(10, 5))
grouped_data = final_df.groupby(["Manager Number"])['Sales'].sum()
grouped_data.plot(kind = 'bar', ax = ax)
plt.title('Total Sales ($) By Manager')
plt.show()


# sales per manager over time
fig, ax = plt.subplots(figsize=(15, 8))
grouped_data = final_df.groupby([pd.Grouper(key='Date', freq='Y'), 'Manager Number'])['Sales'].sum()
grouped_data.unstack().plot(kind = 'bar', ax = ax, colormap = 'tab20')
plt.title('Annual Sales ($) By Manager')
plt.show()

# sales per manager in the USA
fig, ax = plt.subplots(figsize=(15, 8))
grouped_data = final_df[final_df['Region'] == 'USA'].groupby([pd.Grouper(key='Date', freq='Y'), 'Manager'])['Sales'].sum()
grouped_data.unstack().plot(kind = 'bar', ax = ax, colormap = 'tab20')
plt.title('Annual USA Sales ($) By Manager in the USA')
plt.show()
