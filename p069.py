import sys
sys.path.append('../libraries')
import addmath

best=0
for n in range(2, 1000000, 2):
    phi=n/addmath.totient(n)
    print(n)
    if(phi==5.539388020833333):
        break
        print(n)
