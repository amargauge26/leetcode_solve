class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = []
        n = len(heights)
        lsmall = [0] * n
        rsmall = [0] * n

        # Find nearest smaller to the left
        for i in range(n):
            while st and heights[st[-1]] >= heights[i]:
                st.pop()
            
            if st:
                lsmall[i] = st[-1] + 1
            else:
                lsmall[i] = 0
            
            st.append(i)
    
        st = []

        # Find nearest smaller to the right
        for i in range(n - 1, -1, -1):
            while st and heights[st[-1]] >= heights[i]:
                st.pop()
            
            if st:
                rsmall[i] = st[-1]
            else:
                rsmall[i] = n
            
            st.append(i)
        
        # Calculate the maximum area
        maxi = 0
        for i in range(n):
            width = rsmall[i] - lsmall[i]  # Width of the rectangle
            maxi = max(maxi, width * heights[i])
        
        return maxi

