memo = {}
def computeArrival(n):
    def next_member(k):
        tot = 0
        for digit in str(k):
            tot += int(digit) ** 2
        return tot
    if n in memo:
        return memo[n]
    if n == 89 or n == 1:
        return n
    memo[n] = computeArrival(next_member(n))
    return memo[n]

counter = 0
for n in range(1, 10000000):
    if computeArrival(n) == 89:
        counter += 1
    print(n)
print(counter)
