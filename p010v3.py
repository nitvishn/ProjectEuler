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


n = 2
sum = 0
while n < 2000000:
    if isPrime(n):
        sum += n
    n += 1
    print(n)

print(sum)
