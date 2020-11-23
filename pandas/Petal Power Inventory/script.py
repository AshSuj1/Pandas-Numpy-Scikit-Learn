import pandas as pd

inventory = pd.read_csv('inventory.csv')

# Inspect the first 10 rows of inventory.
print(inventory.head(10))

# create a new data frame with only staten island data
staten_island = inventory.head(10)
print(staten_island)

# Products are sold at the Staten Island location
product_request = staten_island.product_description
print(product_request)

# Types of seeds are sold at the Brooklyn location
seed_request = inventory[(inventory.location == 'Brooklyn') & (inventory.product_type == 'seeds')]
print(seed_request)

# Add a column to inventory called in_stock which is True if quantity is greater than 0 and False if quantity equals 0
inventory['in_stock'] = inventory.apply(lambda x: False if x['quantity']  == 0 else True, axis=1)
print(inventory.head())

# Create a column called total_value that is equal to price multiplied by quantity
inventory['total_value'] = inventory['price'] * inventory['quantity']
print(inventory.head())

# create a new column in inventory called full_description that has the complete description of each product
combine_lambda = lambda row: '{} - {}'.format(row.product_type, row.product_description)

inventory['full_description'] = inventory.apply(combine_lambda, axis = 1)
print(inventory.head())
