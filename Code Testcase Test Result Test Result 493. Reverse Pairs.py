class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        l = 0
        h = len(nums)-1
        return self.msort(nums,l,h)
        
    def msort(self,arr,l,h):
        c = 0 
        if l>=h:
            return 0
        

        mid = (h+l)//2


        c += self.msort(arr,l,mid)
        c +=self.msort(arr,mid+1,h)
        c += self.count(arr,l,mid,h)
        self.merge(arr,l,mid,h)
        return c

    def merge(self,arr,low,mid,high):
        temp = []

        l = low
        r = mid+1
        
        while l<=mid and r<=high:
            if arr[l]<arr[r]:
                temp.append(arr[l])
                l+=1
            
            else:
                temp.append(arr[r])
                r+=1
        
        while l<=mid:
            temp.append(arr[l])
            l+=1
        
        while r<=high:
            temp.append(arr[r])
            r+=1
        #  yeah wala abhi bhi doubt full hai 
        for i in range(len(temp)):
            arr[low + i] = temp[i]
        
        
    def count(self,arr,low,mid,high):
        r = mid+1
        l = low
        co =0 
        for i in range(low,mid+1):
            while r<=high and arr[i]> arr[r]*2:
                r+=1
            co += (r-(mid+1))
        return co
        


