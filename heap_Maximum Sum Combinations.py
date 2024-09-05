
import heapq


class Solution:

    def solve(self, A, B, C):

        minHeap = []

        heapLen = 0

        

        for a in A:

            for b in B:

                heapq.heappush(minHeap, a+b)

                heapLen += 1

                

                if heapLen > C:

                    heapq.heappop(minHeap)

                    heapLen -= 1

        

        res = []

        while minHeap:

            res.append(heapq.heappop(minHeap))

        

        return res[::-1]

        
