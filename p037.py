import addmath
import numpy

primes=set(addmath.primes_under(2000000))

def truncatable(number):
    number=str(number)
    for i in range(len(number)):
        j=len(number)-i
        if(number[i:]=='' or number[:j]==''):
            break
        if(not(int(number[i:]) in primes and int(number[:j]) in primes)):
            return False
    return True

trunc=[]
sumall=0
for i in primes:
    if(len(str(i))==1):
        continue
    if(truncatable(i)):
        trunc.append(i)

print(trunc)
        
for element in trunc:
    for digit in range(1, 10):
        new=str(element)+str(digit)
        if(truncatable(int(new)) and int(new) not in trunc):
            trunc.append(int(str(digit)+str(element)))
    
print(sum(trunc), len(trunc), '\n', trunc)