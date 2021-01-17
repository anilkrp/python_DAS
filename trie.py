#!/usr/bin/env python
# coding: utf-8

# In[4]:


class TriesNode:
    def __init__(self):
        self.children=[None]*26
        self.isEndOfWord=False

class Trie:
    def __init__(self):
        self.root=self.getNode()
        
    def getNode(self):
        return TriesNode()
    
    def _charToIndex(self,ch):
        return ord(ch)-ord('a')
    
    def insert(self,key):
        pCrawl=self.root
        lenght=len(key)
        for level in range(lenght):
            index=self._charToIndex(key[level])
            if not pCrawl.children[index]:
                pCrawl.children[index]=self.getNode()
            pCrawl=pCrawl.children[index]
        pCrawl.isEndOfWord=True
        
    def search(self,key):
        pCrawl=self.root
        lenght=len(key)
        for level in range(lenght):
            index=self._charToIndex(key[level])
            if not pCrawl.children[index]:
                return False
            pCrawl=pCrawl.children[index]
        return pCrawl!=None and pCrawl.isEndOfWord
    
def main():
    keys=['the','a','there','any','by','their']
    output=['not present in list','present in list']
    t=Trie()
    for key in keys:
        t.insert(key)
    print('{} --- {}'.format('the',output[t.search('the')]))
    print('{} --- {}'.format('any',output[t.search('any')]))
    print('{} --- {}'.format('by',output[t.search('by')]))
    print('{} --- {}'.format('hello',output[t.search('hello')]))
    
    
main()


# In[ ]:




