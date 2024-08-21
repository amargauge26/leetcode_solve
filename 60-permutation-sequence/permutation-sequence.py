class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        fact =1
        arr =[]
        for i in range(1,n):
            fact*=i
            arr.append(i)
        arr.append(n)

        k =k-1
        ans=''

        while True:
            ans +=str(arr[k//fact])
            arr.pop(k//fact)
            if not arr:
                break
            k %=fact
            fact //=len(arr)
        
        return ans