#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def find_val(l,e):
    if e in l:
        return True
    else :
        return False
find_val([1,3,4,5],3),find_val([1,3,4,5],6),


# In[ ]:


def findval1(lst,item):
    pos=0
    found=False
    while pos<len(lst) and not found:
        if lst[pos]==item:
            found=True
        else:
            pos +=1
    return found
t=[1,2,32,8,17,42,13,0]
findval1(t,12),findval1(t,13)


# In[ ]:


def order_seq(lst,item):
    pos=0
    found=False
    stop=False
    while pos<len(lst) and not found and not stop:
        if lst[pos]==item:
            found = True
        elif lst[pos]>item:
            stop=True
        else:
            pos=pos+1
    return found
order_seq([1,2,7,4,5],3)


# In[ ]:


def binary_search(lst,item):
    first=0
    last = len(lst)-1
    found=False
    while first<=last and not found:
        mid=(first+last)//2      
        if lst[mid]==item:
            found=True
        elif item<lst[mid]:
            last=mid-1
        else:
            first=mid+1
    return found
binary_search([0,1,2,8,13,17,19,42],3)


# In[ ]:


binary_search([0,1,2,8,13,17,19,42],8)


# In[ ]:


def binary_search01(lst,item):
    if len(lst)==0:
        return False
    else:
        mid=len(lst)//2
        if lst[mid]==item:
            return True
        elif item<lst[mid]:
            return binary_search01(lst[:mid],item)
        else:
            return binary_search01(lst[mid+1:],item)
binary_search01([0,1,2,3,8,17,32,42],3)


# In[ ]:


binary_search01([0,1,2,3,8,17,32,42],16)


# In[ ]:


def findsmallest(lst):
    n=len(lst)
    smallest=lst[0]
    for i in range(1,n):
        if lst[i]<smallest:
            smallest=lst[i]
    return smallest

findsmallest([6,5,6,7,4,3,2])


# In[ ]:


def binary_search02(lst,item):
    low=0
    high=len(lst)-1
    while low<=high:
        mid=(low+high)//2
        if lst[mid]==item:
            return True
        elif item<lst[mid]:
            high=mid-1
        else:
            low=mid+1
    return False
binary_search02([1,2,3,4,5],4)


# In[ ]:


binary_search02([1,2,3,4,5],7)


# In[ ]:




