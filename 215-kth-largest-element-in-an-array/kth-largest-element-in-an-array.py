import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Negate all elements to simulate a max-heap
        maxh = [-x for x in nums]
        
        # Heapify the negated list to create a max-heap
        heapq.heapify(maxh)
        
        # Pop k elements from the heap and return the k-th largest
        pop = None
        while k:
            pop = -heapq.heappop(maxh)  # Negate again to get original value
            k -= 1
        
        return pop