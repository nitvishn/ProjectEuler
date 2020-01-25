import addmath

def fifth_power(numbers):
    sumall=0
    for number in numbers:
        sumall+=number**5
    return sumall

sumall=0
upperbound=6*(9**5)
for number in range(2**5, upperbound+1):
    digits = addmath.get_digits(number)
    if(fifth_power(digits)==number):
        sumall+=number
print(sumall)