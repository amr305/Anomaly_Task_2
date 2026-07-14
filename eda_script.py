# step1 : importing the data and the libraries

import numpy as np
import pandas as pd
df = pd.read_csv('ecommerce_users.csv')

# step2: inspect the data

print("="*10, "data info.", "="*10)
print(df.info(), '\n'*2)
print("="*10, "data describtion", "="*10, '\n'*2)
print(df.describe(), '\n'*2)

# step3: Finding & Filling the age missing values

mean_age = df['age'].mean()
df['age'] = df['age'].fillna(mean_age)
print (df['age'])

# step4: Clean purchases

df['total_purchases'] = df['total_purchases'].fillna(0)

print("="*10, "data after cleaning", "="*10,'\n'*2)
print(df)

# Data Exploration:

tot_rev = df[df['account_status']== 'Active']['revenue'].sum()
print("="*10, "Total Revenue from active users:",tot_rev , "="*10, '\n'*2)

# Tier analysis:

tier_avg_purchases = df.groupby('subscription_tier')['total_purchases'].mean()
print ("="*10, " Average total_purchases per subscription_tier: ", tier_avg_purchases, "="*10)
top_tier = tier_avg_purchases.idxmax()
top_avg = tier_avg_purchases.max()
print(f"\nThe '{top_tier}' tier buys the most on average: {top_avg:.2f} purchases", '\n'*2)

# The creative Edge Question: Do younger users buy more? or it depends on the tier?
# if a company knows which age group spends more money, they can send special offers to make even more money
age_tier_purchases = df.groupby(['age', 'subscription_tier'])['total_purchases'].mean()
print(age_tier_purchases,'\n'*2)
correlation = df['age'].corr(df['total_purchases'])
print(f"There is a {correlation:.2f} correlation between age and total purchases.", '\n'*2)
print(" Moderate positive relationship (older users tend to buy more)")
