#!/usr/bin/env python
# coding: utf-8

# In[25]:


message = "I am very keen in building up my career in Data Science, but not sure from where to start. If I search the web it throws me thousands of articles, few are relevant others make me confused, again I come around to the same page. Supervised has provided me a good platform to remove all such qualms which were wrangling in my mind"


# In[26]:


message


# In[27]:


len(message)


# In[28]:


message.lower()


# In[29]:


import string


# In[30]:


no_punc = [i for i in message if i not in string.punctuation]


# In[31]:


no_punc


# In[32]:


data = ''.join(no_punc)


# In[33]:


data


# In[34]:


data.rstrip()


# In[35]:


len(data)


# In[36]:


data.find('Data Science')


# In[37]:


#for i in data:
    #new = data.split()
    #print(new.count(i))
    


# In[62]:


#Q 5,6
import pandas as pd
import numpy as np
new = data.split()


# In[97]:


new_s = pd.Series(new)
ran = new_s.value_counts()
#rando = np.unique(new_s,return_counts=True)
print('Words with a frequency more than 1 is \n',ran[ran > 1])


# In[49]:


#Q 5,6

for i in new:
    print(i,'',new.count(i))
    #if new.count(i) > 1:
        #print(i,'',new.count(i))


# In[40]:


#Question 7 - 

#Can you change the word "Supervised" to "Unsupervised" in the string
data


# In[41]:


data.replace('Supervised','Unsupervised')


# In[42]:


#Q 8


# In[43]:


message.split('.')


# In[44]:


data


# In[45]:


message.endswith('e')


# In[46]:


new.count('a')


# In[47]:


data.split()


# In[ ]:




