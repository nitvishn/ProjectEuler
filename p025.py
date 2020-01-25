import addmath
count=0
for i in addmath.fib():
    count+=1
    if(len(str(i))==1000):
        print(i)
        print(count)
        break