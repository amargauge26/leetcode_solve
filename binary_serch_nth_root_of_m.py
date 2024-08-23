def NthRoot(n: int, m: int) -> int:
    # Write Your Code Here

    
    """ while m!=1:
        if m%n!=0:
            return -1
        
        else:
            m//=n
            count+=1
        
        if m==1:
            return count
    
    return -1"""
    l =1
    r =m
    while l<=r:
        mid = (l+r)//2

        if pow(mid,n)==m:
            return mid

        elif pow(mid,n)>m:
            r=mid-1
        
        else:
            l = mid +1
    
    return -1
