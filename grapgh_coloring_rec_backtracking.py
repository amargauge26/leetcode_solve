#User function Template for python3


#Function to determine if graph can be coloured with at most M colours such
#that no two adjacent vertices of graph are coloured with same colour.
def graphColoring(graph, k, V):
    col = [0]*V
    if solve(0,graph,k,V,col):
        return True
    return False

def solve(node,g,k,v,col):
    if node ==v:
        return True
    
    for i in range(1,k+1):
        if issafe(node,col,g,v,i):
            col[node]=i
            if solve(node+1,g,k,v,col):
                return True
            col[node]=0
    return False
    
def issafe(node,col,g,v,i):
    for k in g[node]:
        if col[k]==i:
            return False
    return True
    
