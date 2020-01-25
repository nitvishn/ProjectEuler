import addmath
import math

n=1001*1001

skip=2
sum=1
i=3
while(i<=n):
	sum+=i
	i+=skip
	print(i)
	if int(math.sqrt(i))==math.sqrt(i):
		skip+=2

print(sum)