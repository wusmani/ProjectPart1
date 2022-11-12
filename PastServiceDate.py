#Name- Wasay Usmani
#ID- 1878157
# In[1]:


import pandas as pd 
import numpy as np


# In[5]:


dfmain = pd.read_csv('D:\FullInventory.csv')


# In[6]:


print(type(dfmain.ServiceDate[0]))


# In[7]:


dfmain['ServiceDate'] = pd.to_datetime(dfmain['ServiceDate'])


# In[8]:


print(type(dfmain.ServiceDate[0]))


# In[9]:


dfmain.sort_values(by='ServiceDate', inplace=True)
dfmain


# In[10]:


PastServiceDateInventory = dfmain


# In[11]:


#PastServiceDateInventory.csv
PastServiceDateInventory

