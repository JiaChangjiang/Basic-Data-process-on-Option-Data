import tushare as ts
import pandas as pd
import matplotlib.pyplot as plt
plt.figure(figsize=(40,30))
def get_stock_price(code0,start0,end0,ktype0):
    data = ts.get_hist_data(code0,start=start0,end=end0,ktype=ktype0)
    data.loc[data['p_change']<-4,'p_change']=1
    y=data['p_change']
    fig=plt.plot(y,label='p_change')
    y1=data['close']
    fig=plt.plot(y1,label='close_price')
    plt.legend()
    plt.xlabel('TIME')
    plt.xticks(rotation=45)
    plt.show()
start = '2016-01-01'
end = '2018-03-30'
code = '600315'
ktype = 'W'

get_stock_price(code,start,end,ktype)
