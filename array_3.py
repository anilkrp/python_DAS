#!/usr/bin/env python
# coding: utf-8

# ## Numpy Basics

# In[1]:


import numpy as np


# In[2]:


a=np.arange(25).reshape(5,5)
a


# In[3]:


np.power(100,8,dtype=np.int64)


# In[4]:


np.power(100,8,dtype=np.int32)


# In[5]:


np.zeros((2,3))


# In[6]:


np.indices((3,3))


# ## I/O with Numpy

# In[7]:


from io import StringIO
data = "1, 2, 3\n4, 5, 6"
np.genfromtxt(StringIO(data),delimiter=", ")


# In[8]:


data=u"""#
# skip me!
# skip me to!
1,2
3,4
5,6 # this is the third line of the "data Structures & Algorithms.ipynb"
7,8
# and here comes the last line
9,0
"""
print(np.genfromtxt(StringIO(data),comments='#',delimiter=','))


# In[9]:


data = u'1 2 3 \n4 5 6'
np.genfromtxt(StringIO(data),usecols=(0,-1))


# In[10]:


k = np.arange(12).reshape(3,4)
k


# In[11]:


k[2]


# In[12]:


k[1]


# In[13]:


k[1][1]


# In[14]:


k[-1][-2]


# In[15]:


x=np.arange(10,1,-1)
x


# In[16]:


x[np.array([3,3,1,8])]


# In[ ]:





# In[17]:


b=x>5


# In[18]:


b


# In[19]:


x[b]


# In[20]:


big_end_buffer = bytearray([0,1,2,3])
big_end_buffer


# In[21]:


big_end_arr=np.ndarray(shape=(2,),dtype='>i2',buffer=big_end_buffer)


# In[22]:


big_end_arr


# In[23]:


big_end_arr[0]


# In[24]:


big_end_arr[1]


# In[ ]:
