#!/usr/bin/env python
# coding: utf-8

# In[ ]:


l=[1,2,3,4,5]
5*sum(l)


# In[ ]:


sum(5*y for y in l)


# In[ ]:


sum(i for i in range(10,21))


# In[ ]:


s=0
for i in range(10,21):
    s+=i
s


# In[ ]:


5*sum(i for i in range(1,11))


# In[ ]:


sum(5455*i for i in range(1,1100))+5*sum(i for i in range(1,1001))


# In[ ]:


5*sum(i for i in range(1,11))+5*sum(i for i in range(12,25))


# In[ ]:


sum([i+j for i in range(1,11) for j in range(12,25)])


# In[ ]:


sum([i for i in range(1,11)])


# In[ ]:


(11*10)/2


# In[ ]:


h=10
sum(2**i for i in range(0,h-5))


# In[ ]:


2**6


# In[ ]:


from random import randrange
n=10**90
p=randrange(n)
n>p


# In[ ]:


def S(seq,i=0):
    if i==len(seq):return 0
    return S(seq,i+1)+seq[i]
S([])


# In[ ]:


def T(seq,i=0):
    if i==len(seq):return 1
    return T(seq,i+1)+1
S([])


# In[ ]:


seq=range(1,101)
S(seq)


# In[ ]:


T(seq)


# In[ ]:


(54).__add__(54)


# In[ ]:


range(1,223)


# In[ ]:





# In[ ]:


l='anil'
l


# In[ ]:


l[1]


# In[ ]:


l.center(10)


# In[ ]:


l.count('a')


# In[ ]:


l.ljust(10)


# In[ ]:


k=set([1,2,3,2,3])
l=set([1,2,4,5,6,7,3,2,3])
k&l


# In[ ]:


print('%d and %d '%(k,l))


# In[ ]:


l=1
while l<5:
    print('hello')
    l+=1
print('done !')


# In[ ]:


word_list = ['cat','dog','rabbit']
letter_list = [ ]
for a_word in word_list:
    for a_letter in a_word:
        letter_list.append(a_letter)
print(letter_list)


# In[ ]:


def sumo(n):
    the_sum=0
    for i in range(1,n+1):
        the_sum=the_sum+i
    return the_sum

sumo(10)


# In[ ]:


import time
def sum_of_n_2(n):
    start = time.time()
    the_sum = 0
    for i in range(1, n+1):
        the_sum = the_sum + i
    end = time.time()
return the_sum,end-start
sum_of_n_2(52)


# In[ ]:


l=[1,2,3,4,5,6,5,4,5,6,7,8,9,10]
for i in l:
    for j in l:
        if i*j==5:
            print('5 yesssss')
        elif i*j==7:
            print('7 seven q!!!!!!!!!')
        else:
            print(i,j,i*j)


# In[ ]:




