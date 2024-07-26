class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxx =float('-inf')
        p=1
        s=1
        n = len(nums)
        for i in range(len(nums)):
            if p==0:
                p=1
            if s==0:
                s=1
            p=p*nums[i]
            s=s*nums[n-1-i]
            maxx= max(maxx,max(s,p))
        return maxx
