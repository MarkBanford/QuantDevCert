import pandas as pd
import numpy as np

daily_index = pd.date_range(start='01-Jan-2019', end='30-Jan-2019', freq='D')

data = np.random.randint(10, size=(len(daily_index), 3))
df_daily = pd.DataFrame(index=daily_index, data=data, columns=['A_col', 'B_col', 'C_col'])

print(df_daily.head(5))

number_words = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven",
                8: "eight", 9: "nine", 10: "ten"}

df_daily[['A_col', 'B_col']] = df_daily[['A_col', 'B_col']].replace(number_words)

print(df_daily.head(3))

new = pd.crosstab(df_daily['A_col'], df_daily['B_col'])

print(new)
