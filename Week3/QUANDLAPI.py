import quandl
import pandas as pd

quandl.ApiConfig.api_key = 'vDx8WfqQyszzCTUfssKr'

df_wti = pd.DataFrame(quandl.get("EIA/PET_RWTC_D", start_date="2010-01-01", end_date="2019-12-31"))

# Work out the quarter on quarter changes (need to resample the data first!)
df_wti.columns = ['WTI Crude Oil (QoQ % change)']
df_wti = df_wti.resample('Q').last()
df_wti = (df_wti / df_wti.shift(1) - 1) * 100

# Download Texas unemployment data from the BLS database on Quandl (Bureau of Labor Statistics)
df_une = pd.DataFrame(quandl.get("BLSE/LAUST480000000000004", start_date="2010-01-01", end_date="2019-12-31"))
df_une.columns = ['Texas Unemployment (QoQ % change)']
df_une = df_une.resample('Q').last()
df_une = (df_une / df_une.shift(1) - 1) * 100

df = df_wti.join(df_une)

from chartpy import Style, Chart

# Use chartpy as it make it easier to use multiple y-axes!
style = Style(title='Crude vs Texas Unemployment',
              y_axis_2_series='Texas Unemployment (QoQ % change)',
              y_axis_showgrid=False, y_axis_2_showgrid=False, source='Quandl/BLS/EIA')
Chart(engine='matplotlib').plot(df, style=style)