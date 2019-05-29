#!/usr/bin/env python
# coding: utf-8

# 
# 
# # Project: Movie Investigation 
# 
# ## Table of Contents
# <ul>
# <li><a href="#intro">Introduction</a></li>
# <li><a href="#wrangling">Data Wrangling</a></li>
# <li><a href="#eda">Exploratory Data Analysis</a></li>
# <li><a href="#conclusions">Conclusions</a></li>
# </ul>

# <a id='intro'></a>
# ## Introduction
# ### The Research Question are : 
# **Question 1: THE MOVIES PRODUCTION OVER THE YEARS?**
# 
# **Question  2 : Movies with most and least earned revenue?¶**
# 
# **Question  3: Movies with largest budgets?¶**
# 
# **Question  4:  WHAT is the Top 10 highest grossing movies?**
# 
# **Question  5: IS high budgets mean high revenues?**
# 

# In[37]:



import pandas as pd
import numpy as np
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


# Load your data and print out a few lines. Perform operations to inspect data
#   types and look for instances of missing or possibly errant data.
df = pd.read_csv('tmdb-movies.csv')
df.head()


# ## Communication
# 
# 
# **Obsevations from the data set
# i will use the dollar as currency Because It’s not mentioned.**
# 
# **the genres and the production_companies are soreated with | so we need to remove it so we can analysis**

# In[4]:


##investigate the data
df.describe()


# In[5]:


##investigate the data

df.genres.count()


# In[6]:


##creating a colom for what i want to work with and eliminate the others
colm=['id','popularity','budget','revenue','original_title','director','runtime','genres','production_companies','vote_count','vote_average','release_date','release_year']
df=df[colm]
df.head()


# In[7]:


##checking the type 
df.dtypes


# In[8]:


##the null Value 
df.isnull().sum()


# <a id='wrangling'></a>
# ## Data Wrangling
# 
# 

# In[9]:


##Check for columns containing null values

df.info()


# In[10]:


##creating a list of null values
df.columns[df.isnull().any()].tolist()


# In[11]:


df.isnull().any(axis=1).sum()


# In[12]:


df.describe()


# ## Communication
# 
# 
# **here we showed the colums we Selected**

# In[13]:


df.dtypes


# In[14]:


##Convert 'release_date', budget, popularity to datetime from 'object' (string)
df['release_date'] =pd.to_datetime(df['release_date'])
df['budget'] = df['budget'].astype(int)
df['popularity'] = df['popularity'].astype(float)


# In[15]:


##removing the duplicates
df.drop_duplicates(inplace = True)


# In[16]:


sum(df.duplicated())


# <a id='eda'></a>
# ## Exploratory Data Analysis
# 
# 
# ###  Question 1: THE MOVIES PRODUCTION OVER THE YEARS

# In[28]:


## simple plot no need for function 
movyer= df['release_year'].value_counts().sort_index();
plt.plot(movyer);
plt.title('Movies production trend over the years');
plt.xlabel('Year');
plt.ylabel('Movies released over the years ');


# ## Communication
# 
# 
# **What we can see from the plot is the increasing of the movies production over the years and the peek in 2011**

# ### Question 2 : Movies with most and least earned revenue¶
# 

# In[34]:



#defining the function
def calculate(column):
    #for highest earned profit
    high= df[column].idxmax()
    high_details=pd.DataFrame(df.loc[high])
    
    
    #collectin data in one place
    info=pd.concat([high_details], axis=1)
    
    return info

#calling the function
calculate('revenue')


# ### Question  3: Movies with largest budgets¶
# 

# In[36]:


# the same function
calculate('budget')


# ## Communication
# 
# 
# **WE will see here the highest revenue ,the avatar movie got more than 2.5 billon,
# this is between 1970 - 2010.**
# 
# **you will see that the highest movie in revenue started from late 2009**

# ### Question 4:  WHAT is the Top 10 highest grossing movies

# In[35]:


## to calculate the highest grossing movies
high_revenues


# ### Question 5: IS high budgets mean high revenues?
# 

# In[130]:


## creating a colum with ('budget','revenue','release_date') then calculate the length 
cols=['budget','revenue','release_date']
len(df[(df['budget']==0) | (df['revenue']==0)])


# In[129]:


##to calculate the Budget vs Revenue i created df2 that take the df and >0 
df2=df[(df['budget']>0) & (df['revenue']>0)]
df2.plot(x='budget',y='revenue',kind='scatter',figsize=(9,9));
plt.ylabel('Revenue in billions ');
plt.title('Budget AND Revenue')
plt.xlabel('Budget million');


# ## Communication
# 
# **You will see from the plot that not alot of movies reched the 1 billon in revenue, but in the other hand a lot of movies got more than 1 billon in budget. they been spending more Money making the movie.**
# 
# **And we will noties that the average budget for movies is between 0.1 and 1 billon, that should give an idea for the investors in the future**

# <a id='conclusions'></a>
# ## Conclusions Phase
# 
# 
# > i found in the analysis that the movie Industry is increasing over the years and is one of the highest Growing business , and i Know that doesn’t mean higher budget more revenue , it’s depends on the crew and director and of course the story , for Example the Jurassic World got the highest budget and Didn’t get the highest revenue.
# I chose the movie database and i promdm cleaning and removing the null Value then i answerd 3 question ,
# Question 1 i calculate the production of movies over the years and from that you can see how much moves got produce in each year.
# >Question 2 WHAT is the Top 10 highest Revenue movies in the year from ( 1970 to 2010 ) , I want to know what is the highest Revenue movie in the years selected , i chose this year beacuse ver good movies publeshed thats year 
# >Question 3 i want to see what is the high budgets mean high revenues and no it’s not 
# >What can I conclude when I analyze these values? First you can see the table for high_revenues in uses the director for these movies to work in your projects and the actress in these movies , and you can know from  THE MOVIES PRODUCTION OVER THE YEARS plot that the entertainment Industry Increasing over the years and from that you can Invest in the Industry . 
# 
# ## Limitiations 
# 
# >what the problem is that budget and revenue columns did not have a currency specified so i choosed dollars.         
# >Rows and colums with null values were dropped, Because of that a lot of key data might have been lost in the process.                                                                                                             
# >i wish that there were data for the crew members that help in creating a movie like writers, etc. to analyse those data.

# In[ ]:


from subprocess import call
call(['python', '-m', 'nbconvert', 'Investigate_a_Dataset.ipynb'])

