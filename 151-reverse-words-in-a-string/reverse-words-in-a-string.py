class Solution:
    def reverseWords(self, s: str) -> str:
        words= s.split()

        newS =''
        words=words[::-1]

        for char in words:
            newS+=char+" "
        return newS[0:-1]