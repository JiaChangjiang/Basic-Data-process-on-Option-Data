
import pandas as pd
import time
data2= pd.read_csv('OptionsDaily_2018_03_01.csv', low_memory=False)
data2.columns=['date','product code','strike price','contract month','call/put','time of trades','option premium','volume','transaction volume']
data2=data2.dropna()
time_start=time.time()
data2['transaction volume']=data2['option premium']*data2['volume']
time_end=time.time()
print(time_end-time_start)
data2=data2.loc[data2['product code'].str.contains('TXO'),:]
data2.loc[data2['product code'].str.contains('TXO'),['product code']]=42
p=data2['call/put'].str.contains('P')
c=data2['call/put'].str.contains('C')
data2.loc[p,['call/put']]=2
data2.loc[c,['call/put']]=1
print(data2)
