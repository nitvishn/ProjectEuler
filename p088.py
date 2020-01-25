memo = {}


def factorise(n):
    if n in memo:
        return memo[n]
    factors = set()
    i = 2
    while i * i <= n:
        if n % i == 0:
            factors.add((n // i, i))
            for item in factorise(i):
                if (n // i, ) + item in factors:
                    continue
                extension = item + (n // i, )
                factors.add(extension)
            for item in factorise(n // i):
                if (n // i, ) + item in factors:
                    continue
                extension = item + (i, )
                factors.add(extension)
        i += 1
    memo[n] = factors
    return memo[n]


def minimal_product_sum(k):
    found = False
    n = 0
    while not found:
        n += 1
        factors = factorise(n)
        for item in factors:
            length = len(item)
            if length > k:
                continue
            if sum(item) + (k - length) == n:
                found = True
                break
    return n


def version_one():
    counted = set()
    for k in range(2, 12000 + 1):
        n = minimal_product_sum(k)
        print(k, n)
        counted.add(n)
    print(sum(counted))


def version_two():
    min_dict = {}
    for n in range(1, 13000):
        items = factorise(n)
        for item in items:
            if sum(item) > n:
                continue
            k = len(item) + (n - sum(item))
            min_dict[k] = min_dict.get(k, set())
            min_dict[k].add(n)
    minVals = set()
    for k in min_dict:
        if not 2 <= k <= 12000:
            continue
        minVals.add(min(min_dict[k]))
    print(sum(minVals))


if __name__ == "__main__":
    version_two()
