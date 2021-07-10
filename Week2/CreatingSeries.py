import pandas as pd
import numpy as np

series = pd.Series(range(12, 17))

# generate a date index and a list of data points from 0 to 8
series_dates = pd.Series(index=pd.date_range(start='1-Jan-2018', periods=8), data=range(0, 8))

df = pd.DataFrame(index=pd.date_range(start='1/1/2018', periods=8), data=np.random.rand(8, 3), columns=['A', 'B', 'C'])

# replace last element in column c

df.at[df.index[-1], 'C'] = 1.0

# Filling missing points

df.at[df.index[[-2, 5]], 'B'] = np.nan


df = df.fillna(method='ffill')
print(df)
