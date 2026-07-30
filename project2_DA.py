#EDA(Exploratory Data Analysis) and Data Visualization


#Importing librabries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#Loading the cleaned dataset
project2 = pd.read_excel('Project1_cleaned_data.xlsx')

#Dropping unnecessary column
project2 = project2.drop('Unnamed: 0', axis=1)

#statistics
cols = ['Quantity', 'UnitPrice', 'TotalPrice']
for col in cols:
    if col in project2.columns:
        print(f"{col}:")
        print(f"Count: {project2[col].count()}")
        print(f"Mean: {project2[col].mean()}")
        print(f"Median: {project2[col].median()}\n")
        
#Extracting year
project2['Year'] = project2['Date'].dt.year

#Making the year column to be an integer
project2['Year'] = pd.to_numeric(project2['Year'],errors='coerce').astype('Int64')

#Extracting month 
project2['Month'] = project2['Date'].dt.strftime('%b')

#Business Questions
#1. monthly revneue and yearly revenue 
monthly_reve = project2.groupby('Month')['TotalPrice'].sum()
plt.plot(monthly_reve.index, monthly_reve.values, marker='o')
plt.xlabel('Month')
plt.title('Monthly Revenue Trend')

#Yearly Revenue
yearly_reve = project2.groupby('Year')['TotalPrice'].sum()
plt.plot(yearly_reve.index, yearly_reve.values, marker='o')
plt.xlabel('Month')
plt.xticks(rotation=45)
plt.title('Yearly Revenue Trend')


#2. Sales and Revenue Performance
# Which products and referral source drive the most total revenue
product = project2.groupby('Product')['TotalPrice'].sum()
products = product.sort_values(ascending=False)
plt.bar(products.index, products.values, label='Revenue')
plt.xlabel('Product')
plt.xticks(rotation=45)
plt.title('Revenue by Products')

# Total revenue by Referral source
sale = project2.groupby('ReferralSource')['TotalPrice'].sum()
sales = sale.sort_values(ascending=False)
plt.bar(sales.index, sales.values, label='Revenue')
plt.xlabel('Referral Source')
plt.xticks(rotation=45)
plt.title('Revenue by Referral Source')


#3. Customer behavior and Retention
#Do customers who use coupon codes have higher revenue
customer = project2.groupby('CouponCode')['TotalPrice'].sum()
customers = customer.sort_values(ascending=False)
plt.bar(customers.index, customers.values, label='Revenue')
plt.xlabel('Coupon Code')
plt.xticks(rotation=45)
plt.title('Revenue by Coupon Codes')

#4. Operations & Fulfillment
#What is our order status breakdown and year?
sns.countplot(x='OrderStatus', data=project2, hue='Year')
plt.xlabel('Order Status')
plt.ylabel('Count')
plt.title('Order Status Breakdown')

#Checking the value count of the order status 
project2['OrderStatus'].value_counts()

#Checking the total number of repeated customers that we have
#count how many orders each customer has
orders_per_customer = project2.groupby('CustomerID')['OrderID'].nunique()

#Filter customers who order more than once
repeat_customers = orders_per_customer[orders_per_customer > 1]

#The total count 
total_repeat_customers = len(repeat_customers)
print(f"Total Repeated Customers : {total_repeat_customers}")


#5.Basket Analysis
#How does number of items in cart relate to payment
#items in cart vs payment
item = project2.groupby('PaymentMethod')['ItemsInCart'].sum()
items = item.sort_values(ascending=False)
plt.bar(items.index, items.values)
plt.xlabel('Payment Method')
plt.xticks(rotation=45)
plt.title('Total Number of items in Cart by Payment Method')