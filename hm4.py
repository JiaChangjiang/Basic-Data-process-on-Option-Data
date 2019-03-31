import pandas as pd
import numpy as np
data3= pd.read_csv('OptionsDaily_2018_03_01.csv', low_memory=False)
data3.columns=['date','product code','strike price','contract month','call/put','time of trades','option premium','volume','transaction volume']
data3=data3.dropna()
data3=data3.loc[data3['product code'].str.contains('TXO'),:]
data3.loc[data3['product code'].str.contains('TXO'),['product code']]=42
data3['call/put']=data3['call/put'].replace('    P     ',2)
data3['call/put']=data3['call/put'].replace('    C     ',1)
for i in np.arrange(0,10000,15)
    a=data3.iloc[i:i+15,:]
    pd.write_
