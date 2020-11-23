import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])
# Inspect the DataFrames using print and head
print(visits.head())
print(cart.head())
print(checkout.head())
print(purchase.head())

# Combine visits and cart using a left merge.
visits_cart = pd.merge(visits, cart, how='left')

# Combine visits and cart using a left merge
print(visits_cart['user_id'].count())

# How many of the timestamps are null for the column cart_time?
cart_time_null = visits_cart.cart_time.isnull().count()
print(cart_time_null)


# What percent of users who visited Cool T-Shirts Inc. ended up not placing a t-shirt in their cart?
visits_cart['vcart_time_null'] = visits_cart.cart_time.isnull()
percent_user_vic = visits_cart[visits_cart.vcart_time_null == True]
percent_cart_vic = float(percent_user_vic.user_id.count())/float(visits_cart.user_id.count()) * 100
print(percent_cart_vic)

# Percentage of users put items in their cart, but did not proceed to checkout 

cart_checkout = pd.merge(cart, checkout, how='left')
cart_checkout_nullcount = cart_checkout.checkout_time.isnull().count()
cart_checkout['isnull']= cart_checkout.checkout_time.isnull()
cart_checkout_isnull = cart_checkout[cart_checkout['isnull']== True]
print(float(cart_checkout_isnull['isnull'].count()) / float(cart_checkout['isnull'].count()) * 100)


# Merge all datasets

cart = pd.read_csv('cart.csv',
                   parse_dates=[1])

visits_cart = pd.merge(visits, cart, how='left')
visits_cart_checkout = pd.merge(visits_cart, checkout, how='left')
all_data = pd.merge(visits_cart_checkout, purchase, how='left')
print(all_data.head())

# What percentage of users proceeded to checkout, but did not purchase a t-shirt?
all_data['checkoutisnotnull'] = ~all_data.checkout_time.isnull()
all_data['purchaseisnull'] = all_data.purchase_time.isnull()
all_data_checkoutisnotnull = all_data[all_data.checkoutisnotnull == True]
all_data_purchaseisnull = all_data[all_data.purchaseisnull == False]
percentage_checkout_ntpur = float(all_data_purchaseisnull.purchaseisnull.count()) / float(all_data_checkoutisnotnull.checkoutisnotnull.count())* 100
print(percentage_checkout_ntpur)

# Average Time to Purchase
all_data['time_to_purchase'] = \
    all_data.purchase_time - \
    all_data.visit_time
  
print(all_data.time_to_purchase)
print(all_data.time_to_purchase.mean())
