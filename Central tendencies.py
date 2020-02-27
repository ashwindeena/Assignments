#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# In[3]:


a = [9,11,13,2,4,5,5]


# In[8]:


a.sort()


# In[9]:


a


# In[11]:


np.mean(a)


# In[12]:


b = [2.2,10.2,14.7,5.9,4.9,10.5,11.1]


# In[13]:


b


# In[14]:


b.sort()


# In[15]:


np.mean(b)


# In[16]:


b


# In[17]:


c = [2.75,7.75,10.5,10.5,25.2]


# In[18]:


np.mean(c)


# In[32]:


a = 0
b = 1
print(a)
print(b)
for i in range(0,11):
    c = a+b
    a = b
    b = c
    print(c)
    new = [c]


# In[34]:


new = [0,1,1,2,3,5,8,13,21,34,55,89,144]


# In[35]:


np.mean(new)


# In[ ]:




