class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []

        if numRows!=0:
            res.append([1])
        if numRows==0:
            return res
        
        for i in range(1,numRows):
            tres =[]
            temp =[0]+res[-1]+[0]
            for j in range(len(res[-1])+1):
                tres.append(temp[j]+temp[j+1])

            res.append(tres)
        return res
