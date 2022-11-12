#Name- Wasay Usmani
#ID- 1878157

# In[1]:


import pandas as pd 
import numpy as np


# In[2]:


dfmain = pd.read_csv('D:\FullInventory.csv')


# In[3]:


DamagedInventory = dfmain.query("Damaged == 'damaged'")


# In[4]:


#DamagedInventory.csv
DamagedInventory


# In[ ]:




