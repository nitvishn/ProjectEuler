import math
import addmath

def length(n):
	if n%2==0:
		n+=1

	while(True):
		if int(math.sqrt(n))==math.sqrt(n):
			return int(math.sqrt(n))
		n+=2

n=3*3
skip=2
sum=1
i=1
diagcounter=1
primes=0
while(primes/diagcounter >= 0.1 or diagcounter==1):
# while(i<=n):
	sum+=i
	i+=skip
	if addmath.isPrime(i):
		primes+=1
	if primes/diagcounter < 0.1:
		break
	diagcounter+=1
	if int(math.sqrt(i))==math.sqrt(i):
		skip+=2

print("Primes:", primes)
print("Length:",length(i))
print("Ratio:", primes/diagcounter)