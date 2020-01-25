import math
from decimal import Decimal


def oddPeriod(n):
    if math.ceil(n**(1/2))**2 == n:
        return False
    m = 0
    d = 1
    a0 = int(math.sqrt(n))
    a = a0
    counter = 0
    while a != 2 * a0:
        m = (d * a) - m
        d = (n - m**2) / d
        a = int((a0 + m) / d)
        counter += 1
    if counter % 2 == 0:
        return False
    return True


N = 10000
n = 2
count = 0
while(n <= N):
    if oddPeriod(n):
        count += 1
        print(n)
    n += 1
print(count)
