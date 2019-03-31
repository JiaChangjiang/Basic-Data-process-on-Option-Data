import pandas as pd
movies=pd.read_csv('movies.csv',sep=',')
movies=pd.read_csv('movies.csv',sep=',')
tags=pd.read_csv('tags.csv',sep=',')
ratings=pd.read_csv('ratings.csv',sep=',')
print(ratings.describe())
print(ratings['rating'].mean())
print(ratings['rating'].min())
print(ratings['rating'].max())
print(ratings['rating'].std())
print(ratings['rating'].mode())
print(ratings.corr())
filter_1=ratings['rating'] > 5
print(filter_1.any())
print(type(filter_1))
print(filter_1)
filter_2=ratings['rating']>0
print(filter_2.all())
