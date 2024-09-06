class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hm ={n:i for i,n in enumerate(nums1)}

        res = [-1]*len(nums1)

        st =[]

        for num in nums2:
            while st and st[-1]<num:
                smallno = st.pop()
                if smallno in hm:
                    res[hm[smallno]]=num
            st.append(num)

        
        return res
