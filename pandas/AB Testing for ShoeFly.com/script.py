import pandas as pd

# Examine the first few rows 
ad_clicks = pd.read_csv('ad_clicks.csv')
print(ad_clicks.head())

# How many views (i.e., rows of the table) came from each platform (utm_source)?
utm_source_views = ad_clicks.groupby('utm_source').utm_source.count()
print(utm_source_views)

# Create a new column called is_click, which is True if ad_click_timestamp is not null and False otherwise
ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isnull()
print(ad_clicks.head())

# The percent of people who clicked on ads from each utm_source
clicks_by_source = ad_clicks.groupby(['utm_source','is_click']).user_id.count().reset_index()
print(clicks_by_source)

# Pivot the data so that the columns are is_click (either True or False), the index is utm_source, and the values are user_id
clicks_pivot = clicks_by_source.pivot(columns= 'is_click', index='utm_source', values='user_id' )
print(clicks_pivot)

# Create a new column in clicks_pivot called percent_clicked which is equal to the percent of users who clicked on the ad from each utm_source
clicks_pivot['percent_clicked'] = clicks_pivot[True]/ (clicks_pivot[True] + clicks_pivot[False]) * 100
print(clicks_pivot)

# The column experimental_group tells us whether the user was shown Ad A or Ad B
experimental_group_no = ad_clicks.groupby('experimental_group').user_id.count()

print(experimental_group_no)

experimental_group_click = ad_clicks.groupby(['experimental_group', 'is_click']).user_id.count().reset_index()
print(experimental_group_click)

experimental_pivot = experimental_group_click.pivot(index='experimental_group', columns='is_click', values='user_id')

# percentage of users clicked on Ad A or Ad B
experimental_pivot['click_percentage'] = experimental_pivot[True]/(experimental_pivot[True] + experimental_pivot[False])
print(experimental_pivot)

# Create two DataFrames: a_clicks and b_clicks
a_clicks = ad_clicks[ad_clicks.experimental_group == 'A']
b_clicks = ad_clicks[ad_clicks.experimental_group == 'B']

print(a_clicks)
print(b_clicks)

# For each group (a_clicks and b_clicks), calculate the percent of users who clicked on the ad by day
a_clicks = a_clicks.groupby(['is_click', 'day']).user_id.count().reset_index()
b_clicks = b_clicks.groupby(['is_click', 'day']).user_id.count().reset_index()

a_clicks = a_clicks.pivot(index='day', columns='is_click', values='user_id')
b_clicks = b_clicks.pivot(index='day', columns='is_click', values='user_id')

a_clicks['click_percentage'] = a_clicks[True]/ (a_clicks[True] + a_clicks[False]) * 100
b_clicks['click_percentage'] = b_clicks[True]/ (b_clicks[True] + b_clicks[False]) * 100

print(a_clicks)
print(b_clicks)
