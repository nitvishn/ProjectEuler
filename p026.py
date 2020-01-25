import sys
sys.path.append('../libraries')
import addmath

import math
from addmath import Fraction

d=1
max_val=0
for i in range(1, 1001):
    if(Fraction(1,i).recurring_cycles()>max_val):
        max_val=Fraction(1,i).recurring_cycles()
        d=i
print(d)
