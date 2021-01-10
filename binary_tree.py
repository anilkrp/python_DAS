#!/usr/bin/env python
# coding: utf-8

# In[16]:


class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
        
    def insert(self,data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left=Node(data)
                else :
                    self.left.insert(data)
            elif data > self.data :
                if self.right is None :
                    self.right=Node(data)
                else : 
                    self.right.insert(data)
        else :
            self.data= data
            
    def findval (self,val):
        if val <self.data:
            if self.left is None:
                return str(val) + ' is not found '
            return self.left.findval(val)
        elif val > self.data:
            if self.right is None:
                return str(val) + ' is not found '
            return self.right.findval(val)
        else : 
            return str(self.data) + " is found "
    
    def printtree(self):
        if self.left :
            self.left.printtree()
        print(self.data)
        if self.right :
            self.right.printtree()


# In[23]:


root= Node(23)

root.insert(13)
root.insert(11)
root.insert(14)
root.insert(15)
root.insert(16)
print(root.findval(4))
print(root.findval(11))
print(root.printtree())


# In[ ]:




