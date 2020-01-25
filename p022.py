def getScore(name):
    sumall=0
    for character in name:
        sumall+=ord(character)-64
    return sumall
file=open("p22_names.txt","r")
names=""
for line in file:
    names+=line
names=names.replace('"','')
names=names.split()
names.sort()
total=0
for i in range(len(names)):
    total+=getScore(names[i])*(i+1)
print(total)