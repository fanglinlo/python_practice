import pandas as pd
import numpy as np
from sklearn.datasets import load_iris

iris = load_iris()
df = pd.DataFrame(data= np.c_[iris['data'], iris['target']],
                     columns= iris['feature_names'] + ['target'])

print(df.head())

import matplotlib.pyplot as plt

fig,ax = plt.subplots()

for y in df.columns:
    ax.plot(df[[y]],label=y)

plt.legend()
plt.show()

corr = df.corr()
print(corr)
