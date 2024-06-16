#!/usr/bin/env python
# coding: utf-8

# In[54]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[55]:


dataframe = pd.read_csv("Downloads/Zomato_data .csv")


# In[56]:


dataframe.head()


# In[57]:


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


# In[58]:


dataframe.info()


# In[59]:


sns.countplot(x=dataframe['listed_in(type)'])
plt.xlabel('Type of restaurant')


# In[60]:


grouped_data=dataframe.groupby('listed_in(type)')['votes'].sum()
grouped_data
result=pd.DataFrame({'votes':grouped_data})
plt.plot(result,c='green',marker='o')
plt.xlabel('Type of restaurant',c='red',size=20)
plt.ylabel('Votes',c='red',size=20)


# In[61]:


grouped_data


# In[62]:


result


# In[63]:


#restaurant’s name that received the maximum votes
max_votes=dataframe['votes'].max()
max_votes


# In[64]:


restaurant_with_max_votes=dataframe.loc[dataframe['votes']==max_votes,'name']
restaurant_with_max_votes


# In[65]:


sns.countplot(x=dataframe['online_order'])


# In[66]:


#exploring rating column
plt.hist(dataframe['rate'],bins=5,range=(0,5))
plt.title('Ratings Distribution')
plt.show()


# In[67]:


sns.countplot(x=dataframe['approx_cost(for two people)'])


# In[68]:


#check online orders receive higher ratings than offline orders.

#convert non numeric data to numeric data
online_order_map={'Yes':1,'No':2}
dataframe['online_order_num']=dataframe['online_order'].map(online_order_map)
plt.figure(figsize = (6,6))
sns.boxplot(x = 'online_order_num', y = 'rate', data = dataframe)


# In[69]:


pivot_table=dataframe.pivot_table(index='listed_in(type)',columns='online_order',aggfunc='size', fill_value=0)
sns.heatmap(pivot_table,annot=True,cmap="YlGnBu",fmt='d')
plt.title('Heatmap')
plt.show()

