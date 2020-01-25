from addmath import *
time.clock()
maxnum=100000
cursor=0
flag=False
primes=set(primes_under(99))
for number in odd_composites():
    if(number in primes):
        continue
    elif(not(divisible(number, primes))):
        primes.add(number)
        continue
    for square in squares_under(number):
        flag=False
        for prime in primes_under(number):
            if(prime+2*square==number):
                print(number, '=', prime, '+', '2*', square)
                flag=True
                break
        if(flag):
            break
    if(not(flag)):
        print(number)
        break
    flag=False
print(time.clock())