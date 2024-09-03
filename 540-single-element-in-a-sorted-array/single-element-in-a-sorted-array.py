class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)

        if  n ==1:
            return nums[0]
        

        if nums[0]!=nums[1]:
            return nums[0]
        

        if nums[n-1]!= nums[n-2]:
            return nums[n-1]

        
        l = 1
        h = n-2


        while l<=h:

            mid = (l+h)//2

            if nums[mid]!=nums[mid+1] and nums[mid]!=nums[mid-1]:
                return nums[mid]
            
            elif mid%2 ==1 and  nums[mid]==nums[mid-1] or (mid%2==0 and nums[mid]==nums[mid+1]):
                l = mid +1
            
            else:
                h = mid-1
        
        return -1