import pandas as pd
import numpy as np

date_index = pd.date_range(start='01-Jan-2019', end='31-Jan-2019', freq='min')
data = np.random.rand(len(date_index), 2)

df_intraday = pd.DataFrame(index=date_index, data=data, columns=['A_col', 'B_col'])

# print(df_intraday)

df_hourly_last = df_intraday.resample('H').last()
df_weekly = df_intraday.resample('W').last()
df_hourly_mean = df_intraday.resample('H').mean()

df = df_intraday
# Summing columns and rows, it will ignore NaNs (unlike NumPy)
df_sum_cols = df.sum(axis=0)
print(df_sum_cols)
df_sum_rows = df.sum(axis=1)
print(df_sum_rows)

# calculate rolling 5D moving average

df_rolling = df.rolling(5, min_periods=1).mean()
print(df_rolling)
