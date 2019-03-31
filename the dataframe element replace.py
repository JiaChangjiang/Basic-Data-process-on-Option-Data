import pandas as pd
import  numpy as np
data3= pd.read_csv('OptionsDaily_2018_03_01.csv', low_memory=False)
data3.columns=['date','product code','strike price','contract month','call/put','time of trades','option premium','volume','transaction volume']
data3=data3.dropna()
data3=data3.loc[data3['product code'].str.contains('TXO'),:]
data3.loc[data3['product code'].str.contains('TXO'),['product code']]=42
data3['call/put']=data3['call/put'].replace('    P     ',2)
data3['call/put']=data3['call/put'].replace('    C     ',1)

def et(row,col):
    return data3.iloc[row-1:row,col-1:col]
print(et(2,2))

data3.loc[data3['contract month'].str.contains('W'),['contract month']]=20180399
for i in range(8):
    a=data3[col[i]]
    b=data3[col[i+1]]
    a=a.astype(np.double)
    b=b.astype(np.double)
    data3=pd.concat([data3,a+b],axis=1)
    print(i)
"""
for i in range(8):
    a=data3[col[i]]
    b=data3[col[i+1]]
    a=a.astype('str')
    b=b.astype('str')
    a.add(b,fill_value=0)
    print(i)

"""
