import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime, timedelta
from matplotlib import dates as mpl_dates

plt.style.use('seaborn')

# dates = [
#     datetime(2019,5,24),
#     datetime(2019,5,25),
#     datetime(2019,5,26),
#     datetime(2019,5,27),
#     datetime(2019,5,28),
#     datetime(2019,5,29),
#     datetime(2019,5,30),
#     datetime(2019,5,31)
# ]

# y = [0,1,3,4,6,8,9,11]

# plt.plot_date(dates, y, linestyle='solid')

# plt.gcf().autofmt_xdate()

# date_format = mpl_dates.DateFormatter('%b, %d, %Y')

# plt.gca().xaxis.set_major_formatter(date_format)

data = pd.read_csv('Stocks.csv')

data['Date'] = pd.to_datetime(data['Date'])
data.sort_values('Date', inplace=True)

price_date = data['Date']
price_close = data['Close']

plt.plot_date(price_date, price_close,  linestyle='solid')

plt.gcf().autofmt_xdate()

date_format = mpl_dates.DateFormatter('%b, %d, %Y')
plt.gca().xaxis.set_major_formatter(date_format)

plt.title('Bitcoin Stocks')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.tight_layout()

plt.show()