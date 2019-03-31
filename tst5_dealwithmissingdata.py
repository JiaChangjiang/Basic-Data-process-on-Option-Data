import pandas as pd
movies=pd.read_csv('movies.csv',sep=',')
movies=pd.read_csv('movies.csv',sep=',')
tags=pd.read_csv('tags.csv',sep=',')
ratings=pd.read_csv('ratings.csv',sep=',')
"""print(movies.shape)
print(movies.isnull().any())
print(tags.isnull().any())
print(tags.shape)
tags=tags.dropna()
print(tags.isnull().any())
print(tags.shape)
"""
a=2
c=6
t=ratings.boxplot(column='rating',figsize=(15,20))
print(t)
