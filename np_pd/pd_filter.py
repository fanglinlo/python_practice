import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))

# - 1. filtered by first column > 20?
print(df[df[0]>20])

# - 2. filtered by first column + second column > 50
print(df[df[0] + df[1] >50])

# - 3. filtered by first column < 30 or second column > 30
print(df[(df[0] < 30) | (df[1] >30) ])

# - 4. filtered by total sum of row > 100
col_sum = df.sum(axis= 1)
print(df[ col_sum > 100 ])
