#!/usr/bin/env python
# coding: utf-8

# In[9]:


class Queuse:
    def __init__(self):
        self.items=[]
    
    def enqueuse(self,item):
        self.items.append(item)
        
    def size(self):
        return len(self.items)
    
    def dequeuse(self):
        if len(self.items)==0:
            return 'sorry !! Queuse is empty'
        else:
            return self.items.pop()
    
    def is_empty(self):
        return self.items==[]
    
    def fisrt(self):
        if self.is_empty():
            return 'sorry !! queuse is empty'
        else:
            return self.items[0]
    
q=Queuse()
for i in range(20):
    q.enqueuse(i)
print(q.items)
q.dequeuse(),q.dequeuse(),q.fisrt(),q.is_empty()


# In[ ]:




