#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
a = np.arange(15).reshape(3,5)
a


# In[ ]:


a.shape


# In[ ]:


a.dtype.name


# In[ ]:


a.itemsize


# In[ ]:


a.size


# In[ ]:


b= np.array([6,7,9])
b


# In[ ]:


type(b)


# In[ ]:


b=np.array([1.2,3.5,6.4])
b


# In[ ]:


b.dtype


# In[ ]:


c=np.array([(1,2,3,4),(5,6,4,3)])
c


# In[ ]:


d=np.array([[1,2],[3,4]],dtype=complex)
d


# In[ ]:


np.zeros((3,4))


# In[ ]:


np.ones((5,4))


# In[ ]:


np.ones((2,3,4),dtype=np.int16)


# In[ ]:


np.empty((2,4))


# In[ ]:


np.arange(10,30,5)


# In[ ]:


np.arange(0,2,0.3)


# In[ ]:


np.linspace(0,2,8)


# In[ ]:


np.arange(10,30,5)


# In[ ]:


x=np.linspace(0,2*np.pi,100)
x


# In[ ]:


np.sin(x)


# In[ ]:


a=np.arange(6) # 1d array
a


# In[ ]:


b=np.arange(12).reshape(3,4) # 2d array
b


# In[ ]:


c=np.arange(24).reshape(2,3,4) # 3d array
c


# In[ ]:


np.arange(10000).reshape(100,100)


# In[ ]:


a=np.array([20,30,40,50])
b=np.arange(4)
b
c=a-b
c


# In[ ]:


b**2


# In[ ]:


10*np.sin(a)


# In[ ]:


a<35


# In[ ]:


a=np.array([[1,1],
            [0,1]])
b=np.array([[2,0],
            [3,4]])
a*b  # elementwise product


# In[ ]:


c=a@b # matrix product
c


# In[ ]:


a.dot(b) # another matrix product


# In[ ]:


c.min()


# In[ ]:


c.max()


# In[ ]:


c.round()


# In[ ]:


b= np.arange(12).reshape(3,4)
b


# In[ ]:


b.sum()


# In[ ]:


b.sum(axis=0)


# In[ ]:


b.sum(axis=1)


# In[ ]:


a= np.floor(10*np.random.random((3,4)))
a


# In[ ]:


a.shape


# In[ ]:


a.ravel()


# In[ ]:


a.reshape(6,2)


# In[ ]:


a.T


# In[ ]:


a.T.shape


# In[ ]:


a.shape


# In[ ]:


a.resize(2,6)
a


# In[ ]:


a= np.floor(10*np.random.random((2,12)))
a


# In[ ]:


np.hsplit(a,3)


# In[ ]:


np.hsplit(a,(3,4))


# In[ ]:


a=np.arange((12)).reshape(3,4)
a


# In[ ]:


b=a


# In[ ]:


b is a 


# In[ ]:


def f(x):
    print(id(x))
id(a),id(b)


# In[ ]:


c= a.view()


# In[ ]:


c is a 


# In[ ]:


c.base is a


# In[ ]:


a = np.arange(12)**2
a


# In[ ]:


i = np.array([1,1,3,8,5])
a[i]


# In[ ]:


j= np.array([[3,4],[5,6]])
a[j]


# In[ ]:


palette=np.array([[0,0,0],
                 [255,0,0],
                 [0,255,0],
                 [0,0,255],
                 [255,255,255]])
image=np.array([[0,1,2,0],
               [0,3,4,0]])
palette[image]


# In[ ]:


a=np.arange(12).reshape(3,4)
a


# In[ ]:


i=np.array([[0,1],
            [1,2]])
j=np.array([[2,1],
            [3,3]])

a[i,j]


# In[ ]:


time = np.linspace(20,145,5)
data=np.sin(np.arange(20)).reshape(5,4)
time


# In[ ]:


data


# In[ ]:


ind = data.argmax(axis=0)
ind


# In[ ]:


time[ind]


# In[ ]:


a= np.arange(5)
a


# In[ ]:


a[[1,3]]=0


# In[ ]:


a


# In[ ]:


a= np.arange(12).reshape(3,4)
b=a>4


# In[ ]:


b


# In[ ]:


a[b]


# In[ ]:


a[b]=0


# In[ ]:


a


# In[ ]:


b


# In[ ]:


a[b]


# In[ ]:


import matplotlib.pyplot as plt
def man (h,w,matrix=20):
    y,x = np.ogrid[-1.4:1.4:h*1j,-2:0.8:w*1j]
    c= x+y*1j
    z=c
    divitime = matrix=np.zeros(z.shape,dtype=int)
    for i in range(20):
        z=z**2+c
        diverge=z*np.conj(z)>2**2
        div_now = diverge & (divitime==matrix)
        divitime[div_now]=i
        z[diverge]=2
    return divitime
plt.imshow(man(400,400))


# In[ ]:


a=np.arange(12).reshape(3,4)
b1=np.array([False,True,True])
b2=np.array([True,False,True,False])
a,a[b1,:],a[:,b2]


# In[ ]:


a= np.array([2,3,4,5])
b= np.array([8,5,4])
c= np.array([5,4,6,8,3])
ax,bx,cx=np.ix_(a,b,c)
ax,bx,cx


# In[ ]:


ax+bx+cx


# ## Linear Algebra

# In[ ]:


a= np.array([[1.0,2.0],[3.0,4.0]])
a


# In[ ]:


a.transpose()


# In[ ]:


np.linalg.inv(a)


# In[ ]:


k=np.eye(4)
k


# In[ ]:


4*k


# In[ ]:


k@k


# In[ ]:


np.trace(k)


# In[ ]:


k=np.arange(16).reshape(4,4)
k


# In[ ]:


k@k,k*k


# In[ ]:


np.trace(k)


# In[ ]:




