from time import *
from math import *
max=int(input("Upperbound: "))
start=time()
def sieve(numbers,x):
    for i in range(1,len(numbers)+1):
        if(i%x==0 and not i==x):
            numbers[i-1]=False

def getNumbers(numbers):
    indexes=[]
    for i in range(len(numbers)):
        if(numbers[i]==True):
            indexes.append(i+1)
    return indexes

def reverseString(numbers):
    indexes=[]
    for element in numbers:
        if(numbers[element]==True):
            indexes.append(False)
        else:
            indexes.append(True)
    return indexes
            
numbers=[]
clock()
for i in range(max):
    numbers.append(True)
numbers[0]=False
prime=2
index=1
while(prime<sqrt(len(numbers))):
    sieve(numbers,prime)
    
print(sum(getNumbers(numbers)))
print("Time: "+str(clock())+" seconds")