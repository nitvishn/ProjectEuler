from addmath import *
def amicable(int1):
    if(sum(factors(sum(factors(int1))))==int1 and not sum(factors(int1))==int1):
        return True
    return False

amsum=0
for i in range(1,10001):
    if amicable(i):
        amsum+=i
print(amsum)