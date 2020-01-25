def factorial(n):
    product=1
    for i in range(n,1,-1):
        product*=i
    return product
    
product=str(factorial(100))
sum=0
for digit in product:
    sum+=int(digit)
print(sum)