#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Heap simple form
def heap(arr,n,i):
    largest=i
    l=2*i+1
    r=2*i+2
    if l<n and arr[i] < arr[l]:
        largest=i
    elif r<n and arr[largest]<arr[r]:
        largest=i
    elif largest != i:
        arr[i],arr[largest]=arr[largest],arr[i]
        heap(arr,n,largest)
        
def insert(arr,num):
    size=len(arr)
    if size ==0:
        arr.append(num)
    else:
        arr.append(num)
        for i in range((size//2)-1,-1,-1):
            heap(arr,size,i)

def deleteNode(arr,num):
    size=len(arr)
    i=0
    for i in range(0,size):
        if num==arr[i]:
            break
    arr[i],arr[size-1]=arr[size-1],arr[i]
    arr.remove(num)
    for i in range((len(arr)//2)-1,-1,-1):
        heap(arr,len(arr),i)

ar=[]
insert(ar,3)
insert(ar,2)
insert(ar,1)
insert(ar,4)
insert(ar,7)
for i in range(100):
    insert(ar,i)
print(str(ar))
deleteNode(ar,4)
print(str(ar))


# In[ ]:


import heapq
arr=[]
for i in range(1,10):
    heapq.heappush(arr,i**2)
print(arr)
heapq.heappush(arr,44)
heapq.heappop(arr)


# In[ ]:


# Max heap heapsort
class MaxHeap:
    def __init__(self,items=[]):
        super().__init__()
        self.heap=[0]
        for i in items:
            self.heap.append(i)
            self.__floatUp(len(self.heap)-1)
    
    def push(self,data):
        self.heap.append(data)
        self.__floatUp(len(self.heap)-1)
    
    def peek(self):
        if self.heap[1]:
            return self.heap[1]
        else:
            return False
    
    def pop(self):
        if len(self.heap)>2:
            self.__swap(1,len(self.heap)-1)
            max=self.heap.pop()
            self.__bubbleDown(1)
        elif len(self.heap)==2:
            max=self.heap.pop()
        else:
            max= False
        return max
    
    def __swap(self,i,j):
        self.heap[i],self.heap[j]=self.heap[j],self.heap[i]
    
    def __floatUp(self,index):
        parent=index//2
        if index<= 1:
            return
        elif self.heap[index]>self.heap[parent]:
            self.__swap(index,parent)
            self.__floatUp(parent)
    
    def __bubbleDown(self,index):
        left=index*2
        right=index*2+1
        largest=index
        if len(self.heap)>left and self.heap[largest]<self.heap[left]:
            largest=left
        elif len(self.heap)>right and self.heap[largest]<self.heap[right]:
            largest=right
        elif largest !=index:
            self.__swap(index,largest)
            self.__bubbleDown(largest )
        
        
m=MaxHeap([x for x in range(1,21)])
m.push(10)
print(str(m.heap[0:len(m.heap)]))
print(str(m.pop()))
print(str(m.peek()))


# In[ ]:




