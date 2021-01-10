#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def data(lst,e):
    for i in range(len(lst)):
        if lst[i]==e:
            return True
    return False
lst=[1,2,3,4,5,6,7,8,9]
data(lst,4)


# In[ ]:


def linear_search(l,e):
    for i in range(len(l)):
        if l[i]==e:
            return True       
    return False

linear_search(lst,43)


# In[ ]:


def bubble_sort(l):
    swap=False
    while not swap:
        swap = True
        for j in range(1,len(l)):
            if l[j-1]<l[j]:
                swap = False
                temp=l[j]              
                l[j]=l[j-1]
                l[j-1]=temp
    return l
l=[5,3,4,1,2]
bubble_sort(l)                


# In[ ]:


def selection(l):
    suffle=0
    while suffle != len(l):
        for i in range(suffle,len(l)):
            if l[i]<l[suffle]:
                l[suffle],l[i]=l[i],l[suffle]
            suffle +=1
    return l
selection(l)


# In[ ]:


def merge_data(left,right):
    result=[]
    i,j=0,0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
        while (i<len(left)):
            result.append(left[i])
            i+=1
        while (j <len(right)):
            result.append(right[j])
            j+=1
        return result
merge_data([5,6,4,3,2,1],[9,8,7])


# In[ ]:


def merge_sort(l):
    if len(l)<2:
        return l[:]
    else:
        middle=len(l)//2
        left=merge_sort(l[:middle])
        right=merge_sort(l[middle:])
        result=[left+right]
        return result
merge_sort([6,5,1,3,2])


# In[ ]:


def insert(lst):
    n=len(lst)
    for i in range(1,n):
        val=lst[i]
        pos=i
        while pos >0 and val <lst[pos-1]:
            lst[pos]=lst[pos-1]
            pos -=1
        lst[pos]=val
    return lst
insert([5,4,3,5,2,1])


# In[ ]:


def mergeList(lst1,lst2):
    newlst=[]
    a=0
    b=0
    while a <len(lst1) and b<len(lst2):
        if lst1[a]<lst2[b]:
            newlst.append(lst1[a])
            a+=1
        else :
            newlst.append(lst2[b])
            b+=1
    while a<len(lst1):
        newlst.append(lst1[a])
        a+=1
    while b<len(lst2):
        newlst.append(lst2[b])
        b+=1
    return newlst

mergeList([1,2,3,8,9],[4,5,6])
            


# In[ ]:




