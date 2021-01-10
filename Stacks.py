#!/usr/bin/env python
# coding: utf-8

# In[10]:


class Stack:
    
    def __init__(self):
        self.items=[]
    
    def is_empty(self):
        return self.items==[]
    
    def push(self,item):
        self.items.append(item)
        return str(item)
    
    def size(self):
        return len(self.items)
    
    def pop(self):
        if self.is_empty():
            return 'sorry !! stack is empty'
        else:
            self.items.pop(0)
       
    def top(self):
        if self.is_empty():
            return 'sorry !! stack is empty'
        else:
            return self.items[-1]
            
s=Stack()
for i in range(20):
    s.push(i)
print(s.items)
s.pop()
s.top()
s.size()


# In[ ]:




