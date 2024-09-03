class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 ,n2 =len(nums1),len(nums2)

        arr=[]
        i,j=0,0
        while i<n1 and j<n2:
            if nums1[i]<nums2[j]:
                arr.append(nums1[i])
                i+=1
            
            else:
                arr.append(nums2[j])
                j+=1
            
        
        arr.extend(nums1[i:])
        arr.extend(nums2[j:])

        n = n1+n2
        if n%2==1:
            return float(arr[n//2])
        
        mid =(arr[n//2]+arr[(n//2)-1])/2.0

        return mid


            
