#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math
import random
import numpy as np
from collections import defaultdict as dd
def dist(v1,v2):
    distance=math.sqrt(sum([(a-b)**2 for a,b in zip(v1,v2)])) #that's just the euclidean distance
    return distance
data=[(3,4,1),(2,5,2),(5,6,1),(1,4,4),(5,2,3),(2,5,2),(3,6,4),(1,6,1),(4,3,2)]
data=list(map(lambda x: np.array(x),data))
k=3
max_steps=20

centroids=[[] for i in range(k)]



a=random.sample(range(0,len(data)),k)
for number in range(k):
    centroids[number]=data[a[number]]
    
print(centroids)    
    
for i in range(max_steps):
    
    classes=dd(list)
    for elements in data:
        distance=[dist(elements,cluster) for cluster in centroids]
        cluster=distance.index(min(distance))
        classes[cluster].append(elements)
        
        
        
    old_centroids=centroids  
    data.append(np.array((1,2,3)))
    for cluster in classes.keys():
        centroids[cluster]=sum(classes[cluster])/len(classes[cluster])
        print(sum(classes[cluster])/len(classes[cluster]),classes[cluster])
    
    print(centroids)
    print(old_centroids)
    if centroids==old_centroids:
        break

