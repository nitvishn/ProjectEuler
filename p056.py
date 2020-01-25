import addmath

maxVal=0
for a in range(100):
    for b in range(100):
        if(addmath.digitsum(a**b)>maxVal):
            maxVal=addmath.digitsum(a**b)
print(maxVal)

def factorial(n):
    if(n<=1):
        return 1
    return n*factorial(n-1)