from typing import *

  
def ninjaTraining(n: int, points: List[List[int]]) -> int:

    dp=[[-1 for _ in range(4)] for _ in range(n)]

    return maxi(n-1,3,dp,points)

def maxi(day,past,dp,points):
    if day==0:
        maxx =0
        for i in range(0,3):
            if past!=i:
                maxx=max(maxx,points[day][i])
        dp[day][past]=maxx
        return dp[day][past]
    
    if dp[day][past]!=-1:
        return dp[day][past]
    
    maxx=0
    for i in range(0,3):
        if i!=past:
            point=points[day][i]+maxi(day-1,i,dp,points)
            maxx= max(maxx,point)
    dp[day][past]=maxx

    return dp[day][past]




