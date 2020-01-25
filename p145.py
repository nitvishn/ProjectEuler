def reverse(n):
    assert type(n) == int
    return int(str(n)[::-1])

def reversible(n):
    k = n + reverse(n)
    for char in str(k):
        if int(char) % 2 == 0:
            return False
    return k

r_set = set()
for n in range(10**9):
    if n in r_set:
        continue
    if reversible(n):
        print(n)
        r_set.add(n)
        r_set.add(reverse(n))
