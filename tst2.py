"""筛选TXO，并改为为42，contract month 交易时间，这个月的第三个周三交割时间，c=1,p=2,volumn交易价格,a:交易量，b:交易值，统计时间的函数。


code=data2.ix[:,'product code']
kind=[]
for i in code:
    if(i not in kind):
        kind.append(i)
print(kind)
"""
import pandas as pd
import  numpy as np
import matplotlib.pyplot as plt

data2= pd.read_csv('OptionsDaily_2018_03_01.csv', low_memory=False)
data2.columns=['date','product code','strike price','contract month','call/put','time of trades','option premium','volume','transaction volume']
data2=data2.dropna()
data2['transaction volume']=data2['option premium']*data2['volume']
containtxo=data['product code'].str.contains('TXO')

txo=data2.loc[data2['product code']=='    TXO     ',:]
txo['product code']=42
""":txo.iloc[:,1]=42"""
txo.loc[txo['call/put']=='    P     ',:]

p['call/put']=2
c=p.loc[p['call/put']=='    C     ',:]
c['call/put']=1
