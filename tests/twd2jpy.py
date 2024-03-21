from common_method.date import Datetimes
from api.api_method import api
from common_method.drawing import scatter_plot
import matplotlib.pyplot as plt

def twd2jpy(api_version=1, date='2024-03-10', endpoint='currencies', peiord=7):
    response_date_list = []
    response_jpy_list = []
    for i in range(peiord, 0, -1):
        dates = Datetimes.date_period_format(date, i)
        print(dates)
        url = f'https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@{api_version}/{dates}/{endpoint}/twd/jpy.json'
        print(url)
        response = api.get(url)
        response_date_list.append(response['date'])
        response_jpy_list.append(response['jpy'])

    #繪圖
    scatter_plot.plot(response_date_list, response_date_list, title='exchange_rate', xlabel='date',ylabel='exchange_rate')
    plt.show()


twd2jpy()