from sys import *
from collections import *
from math import *
import heapq
def minHeap(N: int, Q: [[]]) -> []:
    heap = []
    res = []


    for q in Q:
        if q[0]==0:
            heapq.heappush(heap,q[1])
        
        elif q[0]==1:
            if heap:
                res.append(heapq.heappop(heap))
    

    return res
 
