class Solution:
    def romanToInt(self, s: str) -> int:
        f ={"I":1 , "V":5 ,"X":10 ,"L":50,"C":100,"D":500,"M":1000}
        num =0
        l = len(s)
        for i in range(l-1):
            if f[s[i]]<f[s[i+1]]:
                num-=f[s[i]]
            
            else:
                num+=f[s[i]]
        
        return num+f[s[-1]]