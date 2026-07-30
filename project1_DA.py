#Data Cleaning


#importing our libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import seaborn

#Loading the dataset
project1 = pd.read_excel('Dataset for Data Analytics.xlsx')
project1.head(5)

#Checking the dataset information
project1.info()

#Describing the dataset
project1.describe()

#Checking for duplicates
project1.duplicated().sum()

#Checking for missing values
project1.isnull().sum()

#percentage of missing value
project = round((project1['CouponCode'].isnull().sum() / len(project1['CouponCode']))* 100, 2)

#filling up the missing values
project1['CouponCode'] = project1['CouponCode'].fillna('NO COUPON CODE')

#Checking for outliers using a boxplot
sns.boxplot(data=project1)
plt.xticks(rotation=45)

#applying winsorization for outliers
from scipy.stats.mstats import winsorize
project1['TotalPrice'] = winsorize(project1['TotalPrice'], limits=[0.01, 0.01])

#Describing the dataset
project1.describe()

#Converting the data column that is an object to a datetime column
project1['Date'] = pd.to_datetime(project1['Date'])

#Saving the cleaned dataset
project1.to_excel('Project1_cleaned_data.xlsx')