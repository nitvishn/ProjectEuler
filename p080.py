import math
import decimal
import addmath

def findX(num, acc):
    closest = 0
    for x in range(10):
        if (x*(acc + x)) > num:
            return x - 1
        if num - (x*(acc + x)) < num - (closest*(acc + closest)):
            closest = x
    return closest

def sqrt_digits(num, precision=100):
    digits = []
    i = 0
    while i * i <= num:
        i += 1

    #first bit
    acc = i - 1
    board = num
    board = (board - acc*(i-1))*100
    digits.append(i - 1)

    #the rest bit!
    acc = (acc*2)*10
    prec_counter = 1
    while prec_counter < precision:
        x = findX(board, acc)
        digits.append(x)
        acc += x
        board = (board - acc*(digits[-1]))*100
        if board == 0:
            return digits
        prec_counter += 1
        acc = (int(str(acc)[:-1])*10+int(str(acc)[-1])*2)*10
    return digits

tot = 0
for n in range(1, 100):
    digits = sqrt_digits(n)
    if len(digits) == 2:
        continue
    tot += sum(digits)
print(tot)
