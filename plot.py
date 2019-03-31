import pandas as pd
import  numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv('OptionsDaily_2018_03_01.csv', low_memory=False)
data.columns=['date','product code','strike price','contract month','call/put','time of trades','volume','A','B']
del data['B']
datatime=data.ix[:,['date','time of trades']]
t_time=datatime.ix[:,'time of trades']
i=0
while(i<100):
    a=[t_time[i]]
    i=i+1
    a=str(a[0])
    if len(a)!=7 or len(a)!=8:
        datatime['second']='NaN'
        datatime['minute']='NaN'
        datatime['hour']='NaN'
        continue
    datatime['second']=a[-4]+a[-3]
    datatime['minute']=a[-6]+a[-5]
    print(i)
    if len(a)==7:
        datatime['hour']=a[0]+a[1]
    else:
            datatime['hour']=a[0]

print(datatime.head(10))

