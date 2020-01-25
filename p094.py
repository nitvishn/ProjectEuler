import math

def is_square(n):
    # return True
    return round(math.sqrt(n))**2 == n

def squared_area(a, b):
    # return True
    n = (4*(a**2) - b**2) * (b**2)
    print(n)
    if n % 16 != 0:
        return False
    return is_square(n//16)

print(squared_area(46817, 46816))
# a = 2
# b = 3
# acc = 0
# while 2*a + b <= 10**9:
#     b = a + 1
#     if squared_area(a, b):
#         acc += 2*a + b
#     b = a - 1
#     # print(a, b)
#     if squared_area(a, b):
#         acc += 2*a + b
#     a += 1
#     if a % 10**4 == 0:
#         print(a)
# print(acc)
