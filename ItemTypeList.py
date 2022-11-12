#Name- Wasay Usmani
#ID- 1878157
# In[1]:


import pandas as pd 
import numpy as np


# In[2]:


dfmain = pd.read_csv('D:\FinalProjectPart1\FullInventory.csv')


# In[3]:


PhoneInventory = dfmain.query("ItemType == 'phone'")


# In[4]:


#PhoneInventory
PhoneInventory.head()


# In[5]:


LaptopInventory = dfmain.query("ItemType == 'laptop'")


# In[6]:


#LaptopInventory
LaptopInventory.head()


# In[7]:


#TowerInventory
TowerInventory = dfmain.query("ItemType == 'tower'")


# In[8]:


TowerInventory.head()

