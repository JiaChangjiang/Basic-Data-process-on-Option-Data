import pandas as pd
import time
data2= pd.read_csv('OptionsDaily_2018_03_01.csv', low_memory=False)
data2.columns=['date','product code','strike price','contract month','call/put','time of trades','option premium','volume','transaction volume']
time_start=time.time()
a=0
for i in data2['option premium']:
    data2.iloc[a,8]=data2.iloc[a,7]*data2.iloc[a,6]
    a+=1
time_end=time.time()
print(time_end-time_start)
data2=data2.dropna()
data2.loc[data2['product code'].str.contains('TXO'),['product code']]=2
data2['call/put']=data2['call/put'].replace('    P     ',2)
data2['call/put']=data2['call/put'].replace('    C     ',1)

