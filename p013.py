file=open("13.txt","r")
sumall=0
for line in file:
    sumall+=int(line)
print(str(sumall)[0:10])