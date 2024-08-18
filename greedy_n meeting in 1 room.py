#User function Template for python3

class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        meet = [[start[i],end[i],i+1] for i in range(n)]
        smeet = sorted(meet,key=lambda x:x[1])
        limit = smeet[0][1]
        
        count =1
        
        for i in range(1,n):
            if smeet[i][0]>limit:
                limit= smeet[i][1]
                count+=1
        return count 

