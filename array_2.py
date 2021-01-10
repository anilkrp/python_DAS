#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
a=np.array([1,2,3])
a


# In[2]:


np.zeros(3)


# In[3]:


np.ones(3)


# In[4]:


np.empty(2)


# In[5]:


np.arange(4)


# In[6]:


np.arange(2,9,2)


# In[7]:


np.linspace(1,10,5)


# In[8]:


n=np.arange(16).reshape(4,4)
n


# In[9]:


n.min()


# In[10]:


n.size


# In[11]:


n.shape


# In[12]:


n%3==0


# ## Basic array operations

# In[13]:


a=np.arange(4).reshape(2,2)
b=np.arange(4).reshape(2,2)**2


# In[14]:


a,b


# In[15]:


a+b


# In[16]:


a-b


# In[17]:


b-a


# In[18]:


a@b


# In[19]:


a.diagonal()


# In[20]:


a.trace()


# In[21]:


b.trace()


# In[22]:


c=a@b


# In[23]:


c


# In[24]:


d=c.trace()


# In[25]:


d


# In[26]:


a.max(axis=1)


# In[27]:


e=np.arange(64).reshape(8,8)
e


# In[28]:


e@e


# In[29]:


unique=np.unique(e)
unique


# In[30]:


a_2d=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
a_2d


# In[31]:


np.unique(a_2d)


# In[32]:


np.unique(a_2d,axis=0)


# In[33]:


np.unique(a_2d,axis=1)


# In[34]:


a_2d


# In[35]:


a_2d.T


# In[36]:


a_2d.transpose()


# In[37]:


a_2d.reshape(4,3)


# In[38]:


np.flip(a_2d)


# In[39]:


np.flip(a_2d,axis=1)


# In[40]:


a_2d[1]=np.flip(a_2d[1])


# In[41]:


a_2d


# In[44]:


a_2d[2]=np.flip(a_2d[2],axis=0)


# In[45]:


a_2d


# In[46]:


a=a_2d.flatten()


# In[47]:


a


# In[48]:


a[4]=22


# In[49]:


a


# In[50]:


a_2d


# In[51]:


b=a_2d.ravel()


# In[52]:


b


# In[53]:


a_2d


# In[54]:


b[1]=11


# In[55]:


b


# In[56]:


a_2d


# In[57]:


help(max)


# In[58]:


get_ipython().run_line_magic('pinfo', 'a_2d')


# In[59]:


get_ipython().run_line_magic('pinfo2', 'a_2d')


# ## Working with mathematical formulas

# In[62]:


# mean square error
pre=np.array([1,1,1])
lab=np.array([1,2,3])
error=(1/3)*np.sum(np.square(pre-lab))
error


# In[63]:


a=np.arange(16).reshape(4,4)
a


# In[64]:


np.save('mat',a)


# In[67]:


np.load('mat.npy')


# In[68]:


np.savetxt('mat1',a)


# In[69]:


np.loadtxt('mat1')


# In[70]:


np.savetxt('mat.csv',a)


# In[71]:


np.loadtxt('mat.csv')


# In[72]:


import pandas as pd


# In[73]:


df =pd.DataFrame(a)


# In[74]:


df


# In[75]:


df.info()


# In[76]:


import matplotlib.pyplot as plt


# In[77]:


x=np.linspace(0,5,20)
y=np.linspace(0,10,20)
plt.plot(x,y,'purple')
plt.show()


# In[ ]:




