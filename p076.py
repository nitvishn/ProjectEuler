import math

def map(n):
    if n % 2 == 0:
        return -1*n//2
    else:
        return ((n + 1))//2

def pentagonal(n):
    n = map(n)
    return (n*((3*n) - 1))//2

def sign(k):
    if k % 2 != 0:
        k += 1
    if (k//2) % 2:
        return 1
    else:
        return -1

partitions_memo = {}
def p(n):
    if n == 0:
        return 1
    if n < 0:
        return 0
    if n == 1:
        return 1
    if n in partitions_memo:
        return partitions_memo[n]
    k = 1
    partition = 0
    while n - pentagonal(k) >= 0:
        partition += p(n - pentagonal(k))*sign(k)
        k += 1
    partitions_memo[n] = partition
    return partition

if __name__ == "__main__":
    print(p(5))
