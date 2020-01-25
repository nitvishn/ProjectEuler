def digitproduct(s):
    sum=1
    for c in s:
        c=int(c)
        sum*=c
    return sum
filehandle=open("p008.txt","r")
number=""
for i in filehandle:
    number+=i
    number = number.replace("\n", "")
cursor=0
start=0
greatest=0
for i in range(1000):
    if digitproduct(number[start:start+13])>greatest:
        greatest=digitproduct(number[start:start+13])
    start+=1
print(greatest)
