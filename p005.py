def legit(n,number):
    if(number==1):
        return True
    elif n%number==0:
        return legit(n,number-1)
    else:
        return False

num=1
while(not legit(num,20)):
    num+=1
print(num)
