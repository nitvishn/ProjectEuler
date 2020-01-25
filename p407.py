#!/usr/bin/python
def M(n):
    things=[]
    n-=1
    a=n-1
    while(n>0):
        if(a**2 % n == a%n):
            things.append(a)
            n-=1
            a=n
        a-=1
    return sum(things)
 
num=1000
import time
time.clock()
start=time.time()
print(M(num))
print("clock time:",time.clock(),"\n wall time:",time.time()-start)