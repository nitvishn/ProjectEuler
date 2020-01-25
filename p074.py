factorials = {0: 1, 1: 1, 2: 2, 3: 6, 4: 24,
              5: 120, 6: 720, 7: 5040, 8: 40320, 9: 362880}

def digit_factorial(n):
    if type(n) != int:
        raise TypeError
    acc = 0
    for digit in str(n):
        acc += factorials[int(digit)]
    return acc

chains_memo = {}
def non_repeating_terms(orig_n):
    n = orig_n
    chain = {n: 1}
    chain_list = []
    count = 0
    while 2 not in chain.values():
        n = digit_factorial(n)
        if n in chains_memo:
            return chains_memo[n] + count
        count += 1
        chain[n] = chain.get(n, 0) + 1
        chain_list.append(n)
    for i in range(count):
        chains_memo[chain_list[i]] = count - i
    return count

count = 0
for n in range(100, 1000000):
    if non_repeating_terms(n) == 60:
        count += 1
    print(n)
print(count)
