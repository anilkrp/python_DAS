#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class ListNode :
    def __init__(self,data):
        self.data=data
        
a=ListNode(12)
b=ListNode(52)
c=ListNode(11)
a.data,b.data,c.data


# In[ ]:


class ListNode :
    def __init__(self,data):
        self.data=data
        self.next=None
a=ListNode(23)
a.next=b
print(a.data,a.next)
b=ListNode(34)
print(b.data,b.next,a.next.next)


# In[ ]:


def traversal(head):
    curNode=head
    while curNode is not None :
        print(curNode.data)
        curNode=curNode.next


# In[ ]:


# linked list
class LinkStack:
    class _Node:
        __slots__='_element','_next'
        def __init__(self,element,next):
            self._element=element
            self._next=next
    def __init__(self):
        self._head=None
        self._size=0
        
    def __len__(self):
        return self._size
    def is_empty(self):
        return self._size==0
    def push(self,e):
        self._head=self._Node(e,self._head)
        self._size+=1
    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._head._element
    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        answer=self._head._element
        self._head=self._head._next
        self._size-=1
        return answer


# In[ ]:


class Node :
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
class LinkedList :
    def __init__(self):
        self.head=None
    def indert(self,data):
        newnode=Node(data)
        if (self.head):
            current=self.head
            while (current.next):
                current=current.next
            current.next=newnode
        else :
            self.head=newnode
    def printAll (self):
        self.current=self.head
        while (self.current):
            print(self.current.data)
            self.current=self.current.next


# In[ ]:


a=LinkedList()

a.head=Node(5)
e2=Node('tue')
e3=Node('wed')
a.head.next=e2
e2.next=e3
a.printAll()


# In[ ]:




