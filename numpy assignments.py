#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1. Create a 1D array of numbers from 0 to 9.


# In[2]:


import numpy as np


# In[5]:


arr1 = np.arange(0,10)


# In[6]:


arr1


# In[7]:


#2. Create a 3×3 numpy array of all True’s


# In[17]:


arr2 = np.array([['TRUE','TRUE','TRUE'],['TRUE','TRUE','TRUE'],['TRUE','TRUE','TRUE']])


# In[18]:


arr2.shape


# In[19]:


arr2


# In[20]:


#3. Given an array as input, print only odd numbers as output


# In[21]:


arr1


# In[32]:


arr_odd = arr1[np.where(arr1%2!=0)]


# In[33]:


arr_odd


# In[34]:


#4. Replace all odd numbers in arr with -2


# In[35]:


arr1


# In[57]:


arr1[arr1%2!=0] = -2


# In[58]:


arr1


# In[59]:


#5. How to reshape an array?


# In[68]:


new_arr = np.ones(shape=(4,2))


# In[70]:


new_arr.shape


# In[71]:


new_arr


# In[72]:


new_arr.reshape(2,4)


# In[73]:


new_arr.shape


# In[74]:


#6. Convert a 1D array to a 2D array with 2 rows


# In[75]:


arr1


# In[76]:


arr1.shape


# In[79]:


arr_2d= arr1.reshape(2,5)


# In[246]:


arr_2d


# In[256]:


arr_2d[::]


# In[81]:


arr_2d.shape


# In[83]:


#7. Given an array  a  = [1,2,3,4,5,6,7,8,9] , create  new array b from a such that b includes all odd numbers and 4 multiples. 


# In[90]:


a  = np.arange(1,10)


# In[91]:


a


# In[96]:


b = a[np.where((a%2!=0) | (a%4==0) )]


# In[97]:


b


# In[98]:


#8. Given array, check if there are any null values and print them out. 


# In[ ]:


arr5 = np.array([[3,,0],[1,0,2]])


# In[ ]:


arr5


# In[121]:


arr5[arr5 <= 0]


# In[122]:


#9. How to replace all missing values with 0 in a numpy array?


# In[123]:


#10. How to find the count of each unique number in a NumPy array?


# In[133]:


np.unique(arr_2d,return_counts=True)


# In[134]:


#11. How to convert a numerical array to a categorical (text) array?


# In[181]:


arr1.dtype


# In[140]:


a,b = np.unique(arr1,return_inverse=True)


# In[141]:


a


# In[142]:


b


# In[177]:


arr_al = np.array(['a','b','c','a','f','d'])


# In[187]:


b,c = np.unique(arr_al, return_inverse=True)
b


# In[188]:


c


# In[196]:


a = np.array([-2,-9,-1,0,8,1,9])


# In[197]:


b,c = np.unique(a,return_inverse=True)


# In[198]:


b


# In[199]:


c


# In[200]:





# In[146]:


#12. Write a program to print all numbers between 99 and 299 which are either divisible by 5 or 7. Exclude the elements which are divisible by both. 


# In[147]:


arr12 = np.arange(1,400)


# In[152]:


#arr_div5= arr12[arr12%5==0]


# In[156]:


first_op= arr12[np.where((arr12%5==0) | (arr12%7==0))]


# In[157]:


first_op


# In[159]:


second_op = first_op[np.where((first_op > 99) & (first_op < 299))]


# In[160]:


second_op


# In[170]:


final = second_op[np.where((second_op%5!=0) | (second_op%7!=0))]


# In[171]:


final


# In[172]:


#13. Write a program to reverse an array and print (Don’t use inbuilt reverse functions)


# In[211]:


arr1 = np.array([-2,-4,-5,-6,0,1,10,15,8])
arr1


# In[241]:


arr1[::-1]


# In[242]:


#pending 8 9 & 11


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[207]:


#arr1.shape[0]


# In[221]:


j = 0
for i in arr1:
    n = arr1.shape[0]
    j = j -1
    if(j < -10):
        print('no')
    else:
        np.append = arr1[j]
        print(arr2)
        
    


# In[226]:


rev = arr1[::-1]


# In[228]:


rev


# In[233]:


arr34 = np.arange(10)


# In[234]:


arr34


# In[235]:


arr34.shape


# In[240]:


arr34[::-1]


# In[ ]:


# can we delete specific elements(not by index) from an array ? if so how ?

