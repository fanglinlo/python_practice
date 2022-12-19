import pandas as pd
import ssl

#pycharm 這樣才看得見完整表格
pd.set_option("display.max_columns",None)

#ssl協定，避免出現url error
ssl._create_default_https_context = ssl._create_unverified_context
url = 'https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv'
cars_df = pd.read_csv(url)

# Count the number of missing values in each column
print(cars_df.head())
cars_df_missing = cars_df.isnull().sum()
print(cars_df_missing)

#find the maximum number of missing values.
print(cars_df_missing.max())
cars_df_mean = cars_df.copy(deep=True)
cars_df_mean.fillna(cars_df_mean.mean())
print(cars_df_mean.head())

# Calculate the average price of different manufacturers.
Manufacturer_avg_price = cars_df.groupby('Manufacturer')['Price'].mean()
print(Manufacturer_avg_price)

#How to replace missing values of `price` columns with the mean depending on its manufacturers?
cars_df_mean_manu = cars_df.copy(deep=True)
cars_df_mean_manu['Price'].fillna(cars_df.groupby('Manufacturer')['Price'].transform('mean'),inplace=True)
print(cars_df_mean_manu.head())
