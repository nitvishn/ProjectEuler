def bouncy(n):
    ascension = True
    decension = True

    digits = []
    for char in str(n):
        digits.append(int(char))

    for i in range(len(digits) - 1):
        if digits[i] < digits[i + 1]:
            decension = False
        if digits[i] > digits[i + 1]:
            ascension = False
        if ascension is False and decension is False:
            return True
    return False

b = 0
nb = 1
n = 1
while b/(nb+b) < 0.99:
    n += 1
    if bouncy(n):
        b += 1
    else:
        nb += 1
print(n)
