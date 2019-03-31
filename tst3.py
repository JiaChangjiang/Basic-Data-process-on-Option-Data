import pandas as pd
import numpy as np
data=pd.read_csv('OptionsDaily_2018_03_01.csv',low_memory=False)
print(data.describe())
print(data.head())
print(data.index)
print(data.columns)
