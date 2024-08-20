class Solution:
    def partition(self, s: str) -> List[List[str]]:
        path =[]
        res = []

        self.part(0,s,path,res)

        return res

    def part(self,ind,arr,temp,res):
        if ind == len(arr):
            res.append(temp[:])
            return
        
        for i in range(ind,len(arr)):
            if self.isp(arr,ind,i):
                temp.append(arr[ind:i+1])
                self.part(i+1,arr,temp,res)
                temp.pop()

    def isp(self,s,start,end):
        while start<=end:
            if s[start]!=s[end]:
                return False
            start+=1
            end-=1
        
        return True