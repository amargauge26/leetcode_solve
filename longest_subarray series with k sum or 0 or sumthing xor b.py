#Largest subarray with 0 sum
class Solution:
    def maxLen(self, n, arr):
        #Code here
        
        h = {}
        
        m_len =0 
        summ=0
        for i in range(n):
            summ +=arr[i]
            
            if arr[i]==0 and m_len==0:
                m_len=1
            
            if summ==0:
                m_len= i+1
            
            
            if summ in h:
                m_len = max(m_len,i-h[summ])
            else:
                h[summ]=i
        
        return m_len


# NOW I AM DOUING NO OF SUBAARYS WHIOS COUNT IS K 

from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        presum =0
        m =defaultdict(int)
        m[0]=1
        count =0

        for i in range(n):
            presum += nums[i]


            remove = presum - k 

            count += m[remove]

            m[presum]+=1
        
        return count


# Subarrays with XOR ‘K’ no of subaarsy count 

from collections import defaultdict

def subarraysWithSumK(a: [int], b: int) -> int:
    # Write your code here

    n = len(a)
    mpp = defaultdict(int)

    mpp[0]=1

    prexor = 0

    count =0

    for i in range(n):
        prexor^=a[i]

        remove = prexor^b


        count+= mpp[remove]

        mpp[prexor]+=1

    return count    




