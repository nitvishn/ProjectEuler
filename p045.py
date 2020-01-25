import math
def is_pentagonal(y):
    n= (math.sqrt(1 + 24 * y) + 1.0) / 6.0
    return int(n)==n

def hexGen():
    n=144
    while(True):
        yield n*((2*n)-1)
        n+=1
    
for item in hexGen():
    if(is_pentagonal(item)):
        print(item)
        break