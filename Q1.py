#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np

r=int(input("rows=?")) #take row input
c=int(3)
m=[ ]                  #initialize an empty matrix
for i in range(r):
    l=[]
    for j in range(c):
        v=int(input("coordinate {}:".format(i+1)))  #take coordinate input
        l.append(v)                               
    m.append(l)                      #append l to m making it a 2-D array
n=np.array(m)                                   
def findMinEuDist(n,r):
  minEuDist=10**10                   #initialize a minEuDist as infinite
  for f in range(r):
    for g in range(f+1,r):           # Find the minEuDist by comparing distances of all possible pairs in given array
     k=np.sqrt(np.sum(np.square(n[f]-n[g])))                            
     if k < minEuDist:
        minEuDist=k
        f1=f
        g1=g
  print("Co-ordinates with indexes {},{} in the array have the shortest Euclidian distance".format(f1, g1))
  return minEuDist                       #return minEuDist
print(findMinEuDist(n,r))


# In[ ]:




