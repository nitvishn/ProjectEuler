import math

def check(b, r):
    return (r**2 + 2 * r * b + b **2 - r - b)/(b**2 - b)

def findBNumerical(r):
    radical = math.sqrt(8 * r**2 + 1)
    if round(radical)**2 != 8 * r**2 + 1:
        return False
    radical = round(radical)
    return (1 + 2*r + radical)/2

for r in range(1, 10**12):
    b = findBNumerical(r)
    if b:
        print(r, b, (b + r)>10**12)
print(findBNumerical(35))
