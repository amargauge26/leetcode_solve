class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """ nums.sort()

        ls = float("-inf")

        count = 0

        longest =1

        for i in range(len(nums)):

            if nums[i]-1==ls:
                count +=1
                ls=nums[i]
            
            elif nums[i]!=ls:
                ls=nums[i]
                count =1
            
            longest = max( longest,count)
        
        return 0 if nums==[] else longest"""

        longest = 1
        s = set(nums)

        for a in s:
            if a-1 not in s:
                x= a
                count =1
                while x+1 in s:
                    count +=1
                    x +=1
            
                longest = max(longest,count)
        return 0 if nums==[] else longest

            
            
