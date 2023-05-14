#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')


# In[6]:


hs = pd.read_csv('bundesliga_player.csv')


# In[7]:


hs


# In[9]:


hs.index


# In[10]:


hs.head()


# In[11]:


hs.tail()


# In[12]:


hs.columns


# In[13]:


hs = pd.read_csv('bundesliga_player.csv',index_col='Unnamed')


# In[14]:


hs


# In[17]:


hs.drop(['Unnamed: 0', 'name', 'full_name', 'age', 'height'],axis=1)


# In[18]:


hs.drop(['Unnamed: 0', 'name', 'full_name', 'age', 'height'],axis=1,inplace=True)


# In[19]:


hs


# In[20]:


hs.describe(include='all')


# In[21]:


hs.head(5)


# In[22]:


hs.tail(10)


# In[23]:


hs.corr()


# In[24]:


hs.sample()


# In[25]:


hs.nunique()


# In[26]:


hs


# In[29]:


hs['foot'].value_counts()


# In[30]:


hs.cov()


# In[35]:


hs.groupby("place_of_birth").max_price.mean()


# In[37]:


hs.sample


# In[38]:


hs.plot()


# In[ ]:




