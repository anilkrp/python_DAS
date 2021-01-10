#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def list_number(l):
    the_sum=0
    for i in l:
        the_sum+=i
    return the_sum

list_number([1,2,3,4,5,6])


# In[ ]:


def list_number1(l):
    if len(l)== 1:
        return l[0]
    else:
        return l[0]+list_number1(l[1:])
list_number1([1,2,3,4,5])



# In[ ]:


def fact(N):
    if N==1:
        return 1
    else:
        return N*fact(N-1)
fact(5)


# In[ ]:


def To_str(n,base):
    strt='0123456789ABCDEF'
    if n<base:
        return strt[n]
    else:
        return To_str(n//base,base)+strt[n%base]
To_str(15,16)



# In[ ]:


def mul(a,b):
    if b==1:
        return a
    else :
        return a+mul(a,b-1)
mul(3,4)


# In[ ]:


def printmove(fr,to):
    print(f'move from {fr} to {to}')
def Tower(n,fr,to,spare):
    if  n== 1:
        printmove(fr,to)
    else:
        Tower(n-1,fr,spare,to)
        Tower(1,fr,to,spare)
        Tower(n-1,spare,to,fr)

Tower(3,1,3,3)


# In[ ]:


def fibo(x):
    if x==0 or x==1:
        return 1
    else:
        return fibo(x-1)+fibo(x-2)
fibo(5)


# In[ ]:
