import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 
sns.set_style('whitegrid')


books_df = pl.DataFrame(schema=pl.read_csv('dataset/book1000k-1100k.csv').schema)
books_df.head()

# 4. Is number of pages correlated with rating or number of reviews?

corr = books_df.select([
        'RatingDistTotal', 
        'RatingDist1', 
        'RatingDist2', 
        'RatingDist3', 
        'RatingDist4', 
        'RatingDist5', 
        'CountsOfReview', 
        'PagesNumber',
    ]).corr()
plt.figure(figsize=(12, 9))
sns.heatmap(corr, annot=True)

#### 5. Which years had the biggest number of books written?
plt.figure(figsize=(12, 9))
books_years = sns.barplot(
    x=books_df.groupby('PublishYear').agg(pl.count('Name')).sort('PublishYear').tail(60)['PublishYear'].to_pandas(),
    y=books_df.groupby('PublishYear').agg(pl.count('Name')).sort('PublishYear').tail(60)['Name'].to_pandas()
)
books_years.set_xticklabels(books_years.get_xticklabels(), rotation=90)
books_years.set_xlabel('Publish Year')
books_years.set_ylabel('Number of books')

#### 6. Is there tendency to reduce number of pages in nowaday books?

books = books_df.groupby('PublishYear').agg(pl.mean('PagesNumber')).sort('PublishYear').tail(50)
plt.figure(figsize=(12, 9))
sns.lineplot(x='PublishYear', y='PagesNumber', data=books)


