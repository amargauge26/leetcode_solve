def pf(ind,n,ds,arr,s,t):
    if ind>=n:
        if s==t:
            for i in  ds:
                print(i,end=' ')
            print()
        return
    ds.append(arr[ind])
    s+=arr[ind]
    pf(ind+1,n,ds,arr,s,t)
    ds.pop()
    s-=arr[ind]
    pf(ind+1,n,ds,arr,s,t)
        


s=0
t =2

ds = []
arr = [1, 2, 1]
pf(0,len(arr),ds,arr,s,t)    
