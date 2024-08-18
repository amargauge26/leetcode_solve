class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans =[]
        nums.sort()
        n = len(nums)
        for i in range(n):
            if i!=0 and nums[i]==nums[i-1]:
                continue

            j = i+1
            k = n-1
            while j<k:
                total = nums[i]+nums[j]+nums[k]
                
                if total <0:
                    j+=1
                
                elif total>0:
                    k-=1
                
                else:
                    temp = [nums[i],nums[j],nums[k]]
                    ans.append(temp)
                    j +=1
                    k -=1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1
                    
                    while j<k and nums[k]==nums[k+1]:
                        k-=1
        
        return ans


        #return self.betterapp(nums)

    def betterapp(self,nums):
        s = set()

        n = len(nums)
        for i in range(n):
            hashset=set()
            for j in range(i+1,n):
                rem = -(nums[i]+nums[j])
                if rem in hashset:
                    temp = [nums[i],nums[j],rem]

                    temp.sort()
                    s.add(tuple(temp))
                hashset.add(nums[j])
        return list(s)



        
        
