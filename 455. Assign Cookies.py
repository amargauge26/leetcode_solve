class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        """ count  =0
        glen = len(g)
        slen = len(s)
        arr =[]
        for i in range(glen):
            for j in range(slen):
                if g[i]<=s[j] and s[j] not in arr:
                    count +=1
                    arr.append(s[j])
                    break
            
        return count"""

        # above is the tle approch 

        # optimal approch 

        g.sort()
        s.sort()

        count =0
        i =0
        j =0

        while i < len(g) and j < len(s):
            if g[i]<=s[j]:
                count+=1
                i+=1
            
            j+=1
        
        return count
