n=100

def squaresum(n):
    if(n==1):
        return 1
    i=n**2
    return i+squaresum(n-1)

def sumall(n):
    if(n==1):
        return n
    return n+sumall(n-1)
    
print(-squaresum(n)+sumall(n)**2)