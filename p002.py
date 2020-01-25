high=4000000
numbers=[]
numbers.append(2)
num1=1
num2=2
new=num1+num2
while not new>high:
    numbers.append(new)
    buffer1=num2
    num2=new
    num1=buffer1
    new=num1+num2
sum=0
for n in numbers:
    if n%2==0:
        sum+=n
print(sum)
