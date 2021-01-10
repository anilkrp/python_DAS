#!/usr/bin/env python
# coding: utf-8

# In[1]:


s=0
for i in range(1,11):
    s+=i
print(s)


# In[2]:


[x**2 for x in range(11)]


# In[3]:


s=0
l=[2,3,5]
for i in l:
    for j in l:
        s+=i*j
        print(i,j)
print(s)


# In[8]:


s=0
l1=[1,2,3,4,5]
l2=[6,7,8,9,10]
for i in l1:
    for j in l2:
        s+=i*j
        print(i,j)
s


# In[4]:


s=0
l=[[0,1],[2,3],[4,5]]
for i in l:
    for j in i:
        s+=j
        print(j)
        
s


# In[13]:


s=0
l=[1,2,3]
n=len(l)
for i in range(n-1):
    for j in range(i+1,n):
        s+=l[i]*l[j]
        print(l[i],l[j])
s


# In[16]:


import timeit
timeit.timeit("X=2+2")


# In[21]:


timeit.timeit("X = sum(range(10))")


# In[34]:


hash(12)


# In[30]:


hash('anil')


# In[21]:


a,b,c=range(3)


# In[23]:


n=[
    [a,b],
    [b,c],
    [a,c]
]


# In[26]:


len(n[c])


# In[27]:


a,b,c,d,e,f,g,h=range(8)
N = [
{b:2, c:1, d:3, e:9, f:4}, # a
{c:4, e:3}, # b
{d:8}, # c
{e:7}, # d
{f:5}, # e
{c:2, g:2, h:2}, # f
{f:1, h:6}, # g
{f:9, g:8} # h
]


# In[29]:


b in N[a]


# In[30]:


len(N[g])


# In[31]:


N[h][f]


# In[35]:


a,b,c,d,e,f,g,h=range(8)
#     a b c d e f g h 
N = [[0,1,1,1,1,1,0,0], # a
     [0,0,1,0,1,0,0,0], # b
     [0,0,0,1,0,0,0,0], # c
     [0,0,0,0,1,0,0,0], # d
     [0,0,0,0,0,1,0,0], # e
     [0,0,1,0,0,0,1,1], # f
     [0,0,0,0,0,1,0,1], # g
     [0,0,0,0,0,1,1,0]] # h
N[a][b]


# In[41]:


[[0]*10 for i in range(10)]


# In[42]:


import numpy as np
np.zeros([10,10])


# In[43]:


from random import randrange
l=[randrange(10000) for i in range(1000)]


# In[49]:


s=''
for i in input():
    s+=i
s


# In[54]:


l=[]
l.extend([1,2,3,4])
l


# In[58]:


1.0


# In[59]:


0.1


# In[2]:


from math import sqrt
x=98798797.13
sqrt(x+1)-sqrt(x)


# In[ ]:





# In[5]:


s=[1,2,3,4,5]
5*sum(s)


# In[6]:


sum(5*y for y in s)


# In[10]:


def f(x):
    return x**2


# In[11]:


sum([f(i) for i in range(5)])


# In[16]:


sum([(n*(n-1))/2 for n in range(10)])


# In[37]:


[2**i for i in range(10)]


# In[38]:


x=[2**i for i in range(1,10)]
y=[x for x in range(1,10)]


# In[39]:


import matplotlib.pyplot as plt
plt.plot(x,y)


# In[41]:


from random import randrange
n=10**90
p=[randrange(10**90) for i in range(20)]
plt.plot(p)


# In[ ]:




