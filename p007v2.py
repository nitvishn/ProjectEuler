def isPrime(n):
    if n == 2:
        return True
    elif n == 3:
        return True

    if n % 2 == 0:
        return False
    elif n % 3 == 0:
        return False

    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w
    return True


i = 0
n = 2
while(i != 10001):
    if isPrime(n):
        i += 1
    n += 1
print(n)
