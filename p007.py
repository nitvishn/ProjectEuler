from math import *
def isprime(n):
    for i in range(1,int(sqrt(n)+1)):
        if(n%i==0 and (not i==1) and (not i==n)):
            return False
    return True
    
primecount=0
cursor=0
while(primecount<10002):
    cursor+=1
    if(isprime(cursor)):
        primecount+=1
print(cursor)