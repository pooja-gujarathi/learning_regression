
# coding: utf-8

# In[11]:


import numpy as np
import pandas as pd
get_ipython().magic('pylab inline')
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


# In[3]:


df=pd.read_csv("demo.csv")


# In[4]:


df


# In[12]:


df.plot.scatter('miles_travelled','travel_time')


# In[13]:


df.plot.scatter('num_deliveries','travel_time')


# In[14]:


df.plot.scatter('gas_price','travel_time')


# In[15]:


df.plot.scatter('miles_travelled','num_deliveries')


# In[16]:


df.plot.scatter('num_deliveries','gas_price')


# In[17]:


df.plot.scatter('miles_travelled','gas_price')


# In[18]:


df.corr()

