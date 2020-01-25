import addmath
constant=''
for i in range(1, 1000000):
    constant+=str(i)

def d(index):
    assert index>0
    return int(constant[index-1])

num=d(1)*d(10)*d(100)*d(1000)*d(10000)*d(100000)*d(1000000)
print(num)