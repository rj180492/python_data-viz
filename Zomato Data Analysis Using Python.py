#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


dataframe = pd.read_csv("Downloads/Zomato_data .csv")


# In[3]:


dataframe.head()


# In[4]:


# def handle_rate(value):
#     value=str(value).split('/')
#     value=value[0];
#     return float(value)

# dataframe['rate']=dataframe['rate'].apply(handle_rate)
# dataframe['rate']



def handleRate(value):
    value=str(value).split('/')
    value1=value[0];
    return value1
 
dataframe['rate']=dataframe['rate'].apply(handleRate)
print(dataframe.head())


# In[5]:


dataframe.info()


# In[6]:


sns.countplot(x=dataframe['listed_in(type)'])
plt.xlabel('Type of restaurant')


# In[7]:


grouped_data=dataframe.groupby('listed_in(type)')['votes'].sum()
grouped_data
result=pd.DataFrame({'votes':grouped_data})
plt.plot(result,c='green',marker='o')
plt.xlabel('Type of restaurant',c='red',size=20)
plt.ylabel('Votes',c='red',size=20)


# In[8]:


grouped_data


# In[9]:


result


# In[10]:


#restaurant’s name that received the maximum votes
max_votes=dataframe['votes'].max()
max_votes


# In[13]:


restaurant_with_max_votes=dataframe.loc[dataframe['votes']==max_votes,'name']
restaurant_with_max_votes


# In[19]:


sns.countplot(x=dataframe['online_order'])


# In[43]:


#exploring rating column
plt.hist(dataframe['rate'],bins=5,range=(0,5))
plt.title('Ratings Distribution')
plt.show()


# In[44]:


sns.countplot(x=dataframe['approx_cost(for two people)'])


# In[48]:


#check online orders receive higher ratings than offline orders.

#convert non numeric data to numeric data
online_order_map={'Yes':1,'No':2}
dataframe['online_order_num']=dataframe['online_order'].map(online_order_map)
plt.figure(figsize = (6,6))
sns.boxplot(x = 'online_order_num', y = 'rate', data = dataframe)


# In[52]:


pivot_table=dataframe.pivot_table(index='listed_in(type)',columns='online_order',aggfunc='size', fill_value=0)
sns.heatmap(pivot_table,annot=True,cmap="YlGnBu",fmt='d')
plt.title('Heatmap')
plt.show()

