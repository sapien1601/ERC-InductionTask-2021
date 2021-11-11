#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
r=int(10)
c=int(10)
m=[ ]
for i in range(r): 
    l=[]
    for j in range(c):
        v=int(input("house {} status in row {}<non-infected/infected>--row-wise:".format(j+1,i+1)))  #take input of house status
        l.append(v)
    m.append(l)                                                          #append l to m making it a 2-D array
def safeHouses(m,r):
    k=0
    for f in range(0,r):                                                       
        for g in range(0,c):                 # Find the safeHouses by comparing safety of all possible pairs in given array
              if g==0 and  f!=0 and f!=r-1:  
                       if m[f][g]==0 and m[f-1][g]==0 and m[f-1][g+1]==0 and m[f][g+1]==0 and m[f+1][g]==0 and m[f+1][g+1]==0:
                             k+=1 
              elif f==0 and  g!=0 and g!=c-1:  
                        if m[f][g]==0 and m[f][g-1]==0 and m[f][g+1]==0 and m[f+1][g-1]==0 and m[f+1][g]==0 and m[f+1][g+1]==0:
                             k+=1
              elif f==r-1 and  g!=0 and g!=c-1:
                        if m[f][g]==0 and m[f-1][g-1]==0 and m[f-1][g]==0 and m[f-1][g+1]==0 and m[f][g-1]==0 and m[f][g+1]==0:
                             k+=1
              elif g==c-1 and  f!=0 and f!=r-1:    #takes care of edge houses excluding corners
                        if m[f][g]==0 and m[f-1][g-1]==0 and m[f-1][g]==0 and m[f][g-1]==0 and m[f+1][g-1]==0 and m[f+1][g]==0:
                             k+=1    
              elif f==0 and g==0:
                        if m[f][g]==0 and m[f][g+1]==0 and m[f+1][g]==0 and m[f+1][g+1]==0:
                             k+=1
              elif f==r-1 and g==c-1:
                        if m[f][g]==0 and m[f][g-1]==0 and m[f-1][g]==0 and m[f-1][g-1]==0:
                             k+=1
              elif f==0 and g==c-1:
                        if m[f][g]==0 and m[f][g-1]==0 and m[f+1][g]==0 and m[f+1][g-1]==0:
                             k+=1 
              elif f==r-1 and g==0:               #takes care of corner houses
                        if m[f][g]==0 and m[f-1][g]==0 and m[f][g+1]==0 and m[f-1][g+1]==0:
                             k+=1
              else:                              #takes care of all other houses
                        if m[f][g]==0 and m[f-1][g-1]==0 and m[f-1][g]==0 and m[f-1][g+1]==0 and m[f][g-1]==0 and m[f][g+1]==0 and m[f+1][g-1]==0 and m[f+1][g]==0 and m[f+1][g+1]==0:
                             k+=1
             
    return k
print(safeHouses(m,r)) 


# In[ ]:





# In[ ]:




