import addmath

primes=addmath.primes_under(1000000)
circ=set()

def circular_prime(number):
    numbers = addmath.number_rotations(number)
    for element in numbers:
        if(int(element) not in primes):
            return False
    for element in numbers:
        circ.add(element)
    return True

count=0
for number in primes:
    if(number not in circ):
        if(circular_prime(number)):
            print(number)
            count+=1
print(len(circ))