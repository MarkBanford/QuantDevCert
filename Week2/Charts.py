from chartpy import Chart,Style
import pandas as pd
import numpy as np

df_chartpy = pd.DataFrame(index=pd.date_range(start='1/1/2018', periods=8),
                          data=np.random.rand(8,2), columns=['A', 'B'])

# note that chartpy has its own different styling for Matplotlib charts
style = Style(bokeh_plot_mode="offline_jupyter", plotly_plot_mode='offline_jupyter',
              title='Random chart',
              width=600, height=300, source='Cool stuff!')
Chart(engine='matplotlib').plot(df_chartpy, style=style);

style.chart_type = 'bar'
Chart(engine='matplotlib').plot(df_chartpy, style=style);