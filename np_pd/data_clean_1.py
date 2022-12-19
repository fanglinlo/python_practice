import numpy as np
import pandas as pd
raw_data = {'first_name': ['Jason', np.nan, 'Tina', 'Jake', 'Amy'],
        'last_name': ['Miller', np.nan, 'Ali', 'Milner', 'Cooze'],
        'age': [42, np.nan, 36, 24, 73],
        'sex': ['m', np.nan, 'f', 'm', 'f'],
        'preTestScore': [4, np.nan, np.nan, 2, 3],
        'postTestScore': [25, np.nan, np.nan, 62, 70]}
df = pd.DataFrame(raw_data, columns = ['first_name', 'last_name', 'age', 'sex', 'preTestScore', 'postTestScore'])

#資料觀察
print('Drop missing observations')
print(df.head())
print(df.info())
print(df.isnull().sum())

# new_value
print('Create a new column full of missing values')
df.insert(6, 'new_column', np.nan)
print(df)


#刪除全空值的列
print('Drop rows where all cells in that row is NA')
df=df.dropna(how='all')
print(df)

#Fill in missing data with zeros
print(df.fillna(0))

#Fill in missing in preTestScore with the mean value of preTestScore
preTest_mean = df['preTestScore'].mean()
df['preTestScore'].fillna(value=preTest_mean , inplace= True)
print(df)

#Fill in missing in postTestScore with each sex’s mean value of postTestScore
sex_postScore=df.groupby('sex')['postTestScore'].transform('mean')
df['postTestScore'].fillna(sex_postScore,inplace=True)
print(df)


df = pd.DataFrame(raw_data, columns = ['first_name', 'last_name', 'age', 'sex', 'preTestScore', 'postTestScore'])
df_notnull = df.notnull().all(axis=1)
print(df[df_notnull])
