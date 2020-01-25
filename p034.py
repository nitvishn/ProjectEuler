memo=[1, 1]
import addmath
def factorial():
    current=1
    number=1
    while(True):
        current*=(number+1)
        number+=1
        memo.append(current)
        yield current, number

for i in factorial():
    if(i[1]>10):
        break

totalsum=0
for number in range(3, 999999):
    factsum=0
    for digit in addmath.get_digits(number):
        factsum+=memo[digit]
    if(factsum==number):
        print(number)
        totalsum+=number
print(totalsum)