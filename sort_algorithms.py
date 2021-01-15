#!/usr/bin/env python
# coding: utf-8

# # Sorting Algorithms

# ####  * Bubble Sort
# ####  * Merge Sort
# ####  * Insertion Sort
# ####  * Shell Sort
# ####  * Selection Sort

# In[3]:


# Bubble Sort
def bubblesort(lst):
    for iter_num in range(len(lst)-1,0,-1):
        for idx in range(iter_num):
            if lst[idx]>lst[idx+1]:
                temp=lst[idx]
                lst[idx]=lst[idx+1]
                lst[idx+1]=temp
    return lst
lst=[19,2,13,31,4,45]
bubblesort(lst)


# In[6]:


# Merge Sort
def merge_sort(lst):
    if len(lst) <=1:
        return lst
    middle=len(lst)//2
    left_lst=lst[:middle]
    right_lst=lst[middle:]
    left_lst=merge_sort(left_lst)
    right_lst=merge_sort(right_lst)
    return merge(left_lst,right_lst)

def merge(left_lst,right_lst):
    res=[]
    while len(left_lst)!=0 and len(right_lst)!=0:
        if left_lst[0]<right_lst[0]:
            res.append(left_lst[0])
            left_lst.remove(left_lst[0])
        else:
            res.append(right_lst[0])
            right_lst.remove(right_lst[0])
    if len(left_lst)==0:
        res=res+right_lst
    else:
        res=res+left_lst
    return res



lst=[64,34,25,22,11]
merge_sort(lst)


# In[11]:


# Insertion
def insertion(lst):
    for i in range(1,len(lst)):
        j=i-1
        nxt_element=lst[i]
        while (lst[j]>nxt_element) and (j>=0):
            lst[j+1]=lst[j]
            j=j-1
        lst[j+1]=nxt_element
    return lst

lst=[19,2,31,45,6,11,121]
insertion(lst)


# In[14]:


# Shell sort
def Shell(lst):
    gap=len(lst)//2
    while gap>0:
        for i in range(gap,len(lst)):
            temp=lst[i]
            j=i      
            while j>=gap and lst[j-gap]>temp:
                lst[j]=lst[j-gap]
                j=j-gap
            lst[j]=temp
        gap=gap//2
    return lst

lst=[19,2,31,45,6,11,121]
Shell(lst)


# In[15]:


# selection sort
def selection_sort(lst):
    for idx in range(len(lst)):
        min_idx=idx
        for j in range(idx+1,len(lst)):
            if lst[min_idx]>lst[j]:
                min_idx=j
                lst[idx],lst[min_idx]=lst[min_idx],lst[idx]
    return lst

lst=[19,2,31,45,6,11,121]
selection_sort(lst)


# In[ ]:




