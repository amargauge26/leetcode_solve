#User function Template for python3
class Solution:
	def minCoins(self, coins, M, sum):
		# code here
        coins.sort()
        count=0
        for i in range(M-1,-1,-1):
            if sum < coins[i]:
                continue
            while sum>=coins[i] and sum!=0:
                count+=1
                sum-=coins[i]
                
        if sum !=0:
            return -1
        return count
