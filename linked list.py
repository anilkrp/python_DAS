#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Node :
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.nextval=None

class LinkedList :
    def __init__(self):
        self.headval=None
        
    def Atbeginning(self,newdata):
        newnode=Node(newdata)
        # update  the nodes nextval to exiting node
        newnode.nextval=self.headval
        self.headval=newnode
        
    def AtEnd(self,newdata):
        newnode=Node(newdata)
        if self.headval is None:
            self.headval=newnode
            return
        laste=self.headval
        while (laste.nextval):
            laste=laste.nextval
        laste.nextval=newnode
        
    def Inbetween(self,middlenode,newdata):
        if middlenode is None:
            print('the mention node is absent')
            return
        newnode=Node(newdata)
        newnode.nextval=middlenode.nextval
        middlenode.nextval=newnode
    
    def RemoveNode(self,removekey):
        headval=self.headval
        if (headval is not None):
            if (headval.dataval == removekey):
                self.head=headval.nextval
                headval=None
                return
        while (headval is not None):
            if (headval.dataval == removekey):
                break
            prev=headval
            headval=headval.nextval
        if (headval == None):
            return
        prev.nextval=headval.nextval
        headval=None

    def printlist(self):
        printval=self.headval
        while printval is not None:
            print(printval.dataval)
            printval=printval.nextval
    


# In[ ]:


llist=LinkedList()
llist.headval=Node('mon')
e2=Node('tue')
e3=Node('wed')
llist.headval.nextval=e2
e2.nextval=e3
llist.Atbeginning('sun')
llist.AtEnd('fri')
llist.Inbetween(e2,'hello')
llist.RemoveNode('hello')
llist.printlist()


# In[ ]:


class DlistNode:
    def __init__(self , data):
        self.data=data
        self.next=None
        self.pre=None
    def revTraversal(tail):
        curNode=tail
        while curNode is not None:
            print(curNode.data)
            curNode=curNode.pre
    


# In[ ]:




