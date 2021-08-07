from findatapy.market import Market, MarketDataRequest, MarketDataGenerator
import quandl
import pandas as pd
from chartpy import Chart,Style

QUANDL_API_KEY = 'vDx8WfqQyszzCTUfssKr'

md_request = MarketDataRequest(
    start_date='01 Jan 2001',  # Start date
    finish_date='12 Aug 2019',  # Finish date
    tickers=['WTI'],  # What we want the ticker to look like once download
    vendor_tickers=["EIA/PET_RWTC_D"],  # The ticker used by the vendor
    fields=['close'],  # What fields we want (usually close, we can also define vendor fields)
    data_source='quandl',  # What is the data source?
    quandl_api_key=QUANDL_API_KEY)  # Most data sources will require us to specify an API key/password

market = Market(market_data_generator=MarketDataGenerator())

df_wti = market.fetch_market(md_request)

Chart(engine='matplotlib').plot(df_wti)
