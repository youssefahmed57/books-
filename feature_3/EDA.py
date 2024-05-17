#!/usr/bin/env python
# coding: utf-8

# ## Exploratory Data Analysis
# >This notebook shows some basic Exploratory Data Analysis about the dataset

# ### Objectives
# 0. Clean data
# 1. Which book is the most popular?
# 2. Which author is the most popular?
# 3. Which number wrote the biggest number of books?
# 4. Is number of pages correlated with ratings or number of reviews?
# 5. Which years had the biggest number of books written?
# 6. Is there tendency to reduce number of pages in nowaday books?

# ### Import libraries

# In[1]:


import pandas as pd 
import polars as pl 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 
get_ipython().run_line_magic('matplotlib', 'inline')
sns.set_style('whitegrid')


# ### Load the data

# In[2]:


books_df = pl.DataFrame(schema=pl.read_csv('dataset/book1000k-1100k.csv').schema)
books_df.head()


# #### 1. Which book is the most popular?

# In[47]:


# The book with biggest number of ratings (total)
books_df.filter(books_df['RatingDistTotal'] == books_df['RatingDistTotal'].max())


# In[48]:


# The book with biggest number of 5-star ratings
books_df.filter(books_df['RatingDist5'] == books_df['RatingDist5'].max())


# Book by J. K. Rowling in Greece, maybe it's Harry Potter. Amazing!

# In[49]:


books_df.filter(books_df['Rating'] == 5)

