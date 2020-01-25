import addmath
from time import *


def triangleGen():
    number = 3
    prev = 2
        number += prev + 1
        prev += 1
        yield number

def num_factors(num):
    return len(addmath.factors(num))

for number in triangleGen():
    fact = num_factors(number)
    if(fact > 500):
        print(number, fact)
        break
