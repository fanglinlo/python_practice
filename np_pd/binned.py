import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.random(100)*100)
n = int(input("請輸入組數"))
df['binned'] = pd.cut(df[0], n, labels=False)
print(df)
