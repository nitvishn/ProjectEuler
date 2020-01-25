import math
import itertools
from copy import copy


def divisorsum(n):
    sum = 0
    for i in range(1, n):
        if(n % i == 0):
            sum += i
    return sum


def amicable(int1):
    if(divisorsum(divisorsum(int1)) == int1):
        return True
    return False


def decimal_from_binary_expansion(binary_string):
    string = str(binary_string)
    tot = 0
    j = 1
    for char in string:
        i = int(char)
        tot += i / (2**j)
        j += 1
    print(tot)


def sieve(numbers, n):
    for m in range(n * n, len(numbers) + 1, 2 * n):
        numbers[m - 1] = False


def primesFromFile(filename):
    file = open(filename, "r")
    primes = []
    for line in file:
        line.replace('\n', "")
        line = int(line)
        primes.append(line)
    return primes


def get_digits(number):
    digits = set()
    number = str(number)
    for char in number:
        digits.add(int(char))
    return digits


def convertNumbers(numbers):
    primes = []
    for index in range(len(numbers)):
        if (numbers[index] == True):
            primes.append(index)
    return primes


def primes_under(limit):
    crosslimit = int(math.sqrt(limit))
    if(crosslimit < 20):
        crosslimit = limit
    sieve = [True] * limit
    sieve[0] = False

    for n in range(4, limit, 2):
        sieve[n - 1] = False

    for n in range(3, limit, 2):
        if sieve[n - 1]:
            for m in range(n * n, limit, 2 * n):
                sieve[m - 1] = False

    primes = []
    for n in range(2, limit):
        if sieve[n - 1]:
            primes.append(n)
    return primes


def isPrime(n):
    """Returns True if n is prime."""
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i*i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True


def number_from_digits(digits):
    number = ''
    for digit in digits:
        number += str(digit)
    return number


def number_rotations(number):
    rotations = []
    number = str(number)
    current = number[1:] + number[0]
    rotations.append(current)
    while (current != number):
        current = current[1:] + current[0]
        rotations.append(current)
    return rotations


def factorize(number):
    primes = primes_under(int(math.sqrt(number)))
    powernums = []
    for prime in primes:
        if (number == 1):
            break
        power = 0
        while (number % prime == 0):
            number = int(number / prime)
            power += 1
        powernums.append(power + 1)
    product = 1
    for number in powernums:
        product *= number
    return product


def pascalTriangle(row, column):
    triangle = [[1], [1, 2]]
    n = 2
    k = 2
    for i in range(row ** 2):
        k += 1
        if (n == k - 1):
            triangle[n - 1].append(1)
            n += 1
            k = 2
            triangle.append([1, ])
        triangle[n - 1].append(triangle[n - 2][k - 2] + triangle[n - 2][k - 1])
    try:
        return triangle[row - 1][column - 1]
    except:
        return "Sorry, wrong row and column"


def factors_raw(n):
    """
    Returns the factors of the number.
    factors may be repeated, to ensure that the
    product of the factors is equal to the number.
    """
    divisors = []
    for i in range(2, int(math.sqrt(n)) + int(n)):
        if (n % i == 0):
            if (n / i == i or i == 1):
                divisors.append(i)
            else:
                divisors.append(i)
                divisors.append(int(n / i))
    return divisors


def intersection(list1, list2):
    return list(set(list1).intersection(list2))


def num_factors(n):
    facts = 0
    for prime in primes:
        if (prime > n):
            break
        if (n % prime == 0):
            facts += 1
    return facts


def fib():
    cursor1 = 1
    cursor2 = 1
    temp = 0
    yield cursor1
    yield cursor2
    while (True):
        temp = cursor1 + cursor2
        cursor1 = cursor2
        cursor2 = temp
        yield temp


def squares_under(n):
    squares = set()
    for i in range(1, math.ceil(math.sqrt(n))):
        squares.add(i ** 2)
    squares = list(squares)
    squares.sort()
    return squares


def odds():
    cursor = 9
    while (True):
        yield cursor
        cursor += 2


def divisible(num, list1):
    for element in list1:
        if (num % element == 0):
            return True
    return False


def odd_composites():
    primes = set(primes_under(1000000))
    for number in odds():
        if number not in primes:
            yield number
            continue
        else:
            if (divisible(number, primes)):
                yield number
            else:
                primes.add(number)
                continue


def factorial(x):
    product = 1
    for i in range(2, x + 1):
        product *= i
    return product


def combinations(n, r):
    if (n < r):
        raise ValueError

    if (r <= n / 2):
        acc = 1
        for i in range(n, n - r, -1):
            acc *= i
        return acc
    else:
        acc = 1
        for i in range(n, r, -1):
            acc *= i
        return acc


def digitsum(n):
    n = str(n)
    tot = 0
    for c in n:
        tot += int(c)
    return tot


def numDigits(n):
    assert n > 0

    return int(math.log(n, 10)) + 1


prime_factors_memo = {}
def prime_factors(n):
    """
    returns a 1D list of primes whose product is n
    """
    if n in prime_factors_memo:
        return prime_factors_memo[n]

    i = 2
    factors = []
    while i * i <= n:
        if n % i == 0:
            factors.extend(prime_factors(n//i))
            factors.extend(prime_factors(i))
            prime_factors_memo[n] = factors
            return factors
        i += 1
    prime_factors_memo[n] = [n]
    return [n]

def prime_factorise(n):
    """
    Returns a list of (prime, multiplicity) pairs.
    """
    def convert_format(factors):
        factors_set = set(factors)
        pair_set = []
        for n in factors_set:
            pair_set.append((n, factors.count(n)))
        return pair_set
    return convert_format(prime_factors(n))
    # i = 2
    # factors = []
    # while(n > 1):
    #     times = 0
    #     while(n % i == 0):
    #         n = n // i
    #         times += 1
    #     if times > 0:
    #         factors.append((i, times))
    #     i += 1
    # return factors

def factors(n):
    """
    Returns a set of all the factors of n, including 1. Not including n itself.
    """
    primefactors = []
    for F in prime_factorise(n):
        primefactors += [F[0]]*F[1]
    factors = {n}
    for r in range(len(primefactors)):
        for pair in itertools.combinations(primefactors, r):
            acc = 1
            for item in pair:
                acc *= item
            factors.add(acc)
    return factors


def coprime(x, y):
    if (x > y):
        lower = x
        higher = y
    else:
        lower = y
        higher = x
    if (higher % lower == 0):
        return False
    if (higher % 2 == 0 and lower % 2 == 0):
        return False
    for prime in set(prime_factorise(lower)):
        if (higher % prime == 0):
            return False
    return True


def is_square(apositiveint):
    """
    Pure integer approach. Bit slow.
    """
    if apositiveint < 1 or int(apositiveint) != apositiveint:
        return False
    x = apositiveint // 2
    seen = set([x])
    while x * x != apositiveint:
        x = (x + (apositiveint // x)) // 2
        if x in seen: return False
        seen.add(x)
    return x

def shoelace(points):
    Y = []
    X = []
    for point in points:
        X.append(point[0])
        Y.append(point[1])

    X = [X[-1], ] + X
    Y = [Y[-1], ] + Y

    X.append(X[1])
    Y.append(Y[1])

    acc = 0
    for i in range(1, len(X) - 1):
        acc += X[i]*(Y[i + 1] - Y[i - 1])
    return abs(acc)/2

totient_memo = {}
def totient(n):
    if n in totient_memo:
        return totient_memo[n]
    acc = n
    for prime in set(prime_factors(n)):
        acc *= (1 - (1 / prime))

    return int(acc)

def hcf(a, b):
    a = abs(a)
    b = abs(b)
    if b == 0:
        return a
    else:
        return hcf(b, a % b)

if __name__ == "__main__":
    print(sum(primes_under(2000000)))
