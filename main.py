import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Create Locators for ticks on the time axis
import the as the

years = mdates.YearLocator()
months = mdates.MonthLocator()
years_fmt = mdates.DateFormatter('%Y')

df_tesla = pd.read_csv('TESLA Search Trend vs Price.csv')
df_btc_search = pd.read_csv('Bitcoin Search Trend.csv')
df_btc_price = pd.read_csv('Daily Bitcoin Price.csv')
df_unemployment = pd.read_csv('UE Benefits Search vs UE Rate 2004-19.csv')


"""TESLA DF"""
# Shape of Data Frame tesla
# print(df_tesla.shape)
# Name Of Columns tesla
# print(df_tesla.columns)
tesla_min_num_search = df_tesla.TSLA_WEB_SEARCH.min()
tesla_max_num_search = df_tesla.TSLA_WEB_SEARCH.max()
# print(f"largest num: {tesla_max_num_search} and smallest num:{tesla_min_num_search}")
# print(df_tesla.describe())

"""UNEMPLOYMENT DF"""
# print(df_unemployment.shape)
# print(df_unemployment.columns)
# print(df_unemployment.describe())

"""BTC PRICE DF"""
# print(df_btc_price.describe())

"""BTC SEARCH DF"""
# print(df_btc_search.describe())

"""Find Missing Data or NAN Value"""
# print(df_tesla.isna().values.any())
# print(df_unemployment.isna().values.any())
# print(df_btc_price.isna().values.any())
# print(df_btc_search.isna().values.any())

"""Number of Missing data occur"""
# print(df_btc_price.isna().values.sum())
"""Rows with null"""
# print(df_btc_price[df_btc_price.CLOSE.isna()].shape)
# df_btc_price.dropna(inplace=True)
# print(df_btc_price.shape)

"""String to DateTimeObject"""
df_tesla.MONTH = pd.to_datetime(df_tesla.MONTH)
df_btc_search.MONTH = pd.to_datetime(df_btc_search.MONTH)
df_unemployment.MONTH = pd.to_datetime(df_unemployment.MONTH)
df_btc_price.DATE = pd.to_datetime(df_btc_price.DATE)

# print(df_tesla.MONTH.head())
"""
BTC price is daily Data and BTC search is Monthly data
daily data --> monthly //data convert// ....using .resample()        
"""
# df_btc_monthly = df_btc_price.resample('M', on='DATE').mean()
# print(df_btc_monthly.shape)
df_btc_monthly = df_btc_price.resample('M', on='DATE').last()
# print(df_btc_monthly.shape)

"""Tesla Stock Price Vs Sreach Volume"""
# plt.figure(figsize=(8, 5), dpi=120)
# plt.title('Tesla Web Search vs Price', fontsize=9)
# ax1 = plt.gca()
# ax2 = ax1.twinx()
#
#
# ax1.plot(df_tesla.MONTH, df_tesla.TSLA_USD_CLOSE, color='r', linewidth=2)
# ax2.plot(df_tesla.MONTH, df_tesla.TSLA_WEB_SEARCH, color='skyblue', linewidth=2)
# ax1.set_xlabel("Year")
# ax1.set_ylabel('Stock price', color='r', fontsize=7)
# ax2.set_ylabel('Search result', color='skyblue', fontsize=7)
#
# ax1.set_ylim([0, 600])
# ax1.set_xlim([df_tesla.MONTH.min(), df_tesla.MONTH.max()])
# # format the ticksax1.xaxis.set_major_locator(years)ax1.xaxis.set_major_formatter(years_fmt)ax1.xaxis.set_minor_locator(months)
#
# plt.show()
"""Bitcoin News Search vs Resampled Price"""
#
# plt.figure(figsize=(8, 5), dpi=120)
#
# plt.title('Bitcoin News Search vs Resampled Price', fontsize=9)
# plt.xticks(fontsize=7, rotation=7)
#
# ax1 = plt.gca()7y7yt

# ax2 = ax1.twinx()
#
# ax1.set_ylabel('BTC Price', color='#F08F2E', fontsize=7)
# ax2.set_ylabel('Search Trend', color='skyblue', fontsize=7)
#
# # ax1.xaxis.set_major_locator(years)
# # ax1.xaxis.set_major_formatter(years_fmt)
# # ax1.xaxis.set_minor_locator(months)
#
# ax1.set_ylim(bottom=0, top=15000)
# ax1.set_xlim([df_btc_monthly.index.min(), df_btc_monthly.index.max()])
#
# # Experiment with the linestyle and markers
# ax1.plot(df_btc_monthly.index, df_btc_monthly.CLOSE,
#          color='#F08F2E', linewidth=3, linestyle='--')
# ax2.plot(df_btc_monthly.index, df_btc_search.BTC_NEWS_SEARCH,
#          color='skyblue', linewidth=3, marker='o')
#
# plt.show()

"""Monthly Search of "Unemployment Benefits" in the U.S. vs the U/E Rate"""
# plt.figure(figsize=(8, 5), dpi=120)
# plt.title('Monthly Search of "Unemployment Benefits" in the U.S. vs the U/E Rate', fontsize=7)
# plt.yticks(fontsize=7)
# plt.xticks(fontsize=7, rotation=45)
#
# ax1 = plt.gca()
# ax2 = ax1.twinx()
#
# ax1.set_ylabel('FRED U/E Rate', color='purple', fontsize=7)
# ax2.set_ylabel('Search Trend', color='skyblue', fontsize=7)
#
# ax1.xaxis.set_major_locator(years)
# ax1.xaxis.set_major_formatter(years_fmt)
# ax1.xaxis.set_minor_locator(months)
#
# ax1.set_ylim(bottom=3, top=10.5)
# ax1.set_xlim([df_unemployment.MONTH.min(), df_unemployment.MONTH.max()])
#
# # Show the grid lines as dark grey lines
# ax1.grid(color='grey', linestyle='--')
#
# # Change the dataset used
# ax1.plot(df_unemployment.MONTH, df_unemployment.UNRATE,
#          color='purple', linewidth=3, linestyle='--')
# ax2.plot(df_unemployment.MONTH, df_unemployment.UE_BENEFITS_WEB_SEARCH,
#          color='skyblue', linewidth=3)
#
# plt.show()

"""Rolling Monthly US "Unemployment Benefits" Web Searches vs UNRATE"""
# plt.figure(figsize=(8, 5), dpi=120)
# plt.title('Rolling Monthly US "Unemployment Benefits" Web Searches vs UNRATE', fontsize=7)
# plt.yticks(fontsize=7)
# plt.xticks(fontsize=7, rotation=45)
#
# ax1 = plt.gca()
# ax2 = ax1.twinx()
#
# ax1.xaxis.set_major_locator(years)
# ax1.xaxis.set_major_formatter(years_fmt)
# ax1.xaxis.set_minor_locator(months)
#
# ax1.set_ylabel('FRED U/E Rate', color='purple', fontsize=8)
# ax2.set_ylabel('Search Trend', color='skyblue', fontsize=8)
#
# ax1.set_ylim(bottom=3, top=10.5)
# ax1.set_xlim([df_unemployment.MONTH[0], df_unemployment.MONTH.max()])
#
# # Calculate the rolling average over a 6 month window
# roll_df = df_unemployment[['UE_BENEFITS_WEB_SEARCH', 'UNRATE']].rolling(window=6).mean()
#
# ax1.plot(df_unemployment.MONTH, roll_df.UNRATE, 'purple', linewidth=2, linestyle='-.')
# ax2.plot(df_unemployment.MONTH, roll_df.UE_BENEFITS_WEB_SEARCH, 'skyblue', linewidth=3)
#
# plt.show()

""""""
df_ue_2020 = pd.read_csv('UE Benefits Search vs UE Rate 2004-20.csv')
df_ue_2020.MONTH = pd.to_datetime(df_ue_2020.MONTH)
plt.figure(figsize=(8, 5), dpi=120)
plt.yticks(fontsize=7)
plt.xticks(fontsize=7, rotation=45)
plt.title('Monthly US "Unemployment Benefits" Web Search vs UNRATE incl 2020', fontsize=18)

ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.set_ylabel('FRED U/E Rate', color='purple', fontsize=8)
ax2.set_ylabel('Search Trend', color='skyblue', fontsize=8)

ax1.set_xlim([df_ue_2020.MONTH.min(), df_ue_2020.MONTH.max()])

ax1.plot(df_ue_2020.MONTH, df_ue_2020.UNRATE, 'purple', linewidth=2)
ax2.plot(df_ue_2020.MONTH, df_ue_2020.UE_BENEFITS_WEB_SEARCH, 'skyblue', linewidth=2)

plt.show()