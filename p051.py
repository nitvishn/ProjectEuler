import addmath
import itertools
import sys

array5=[]
array6=[]

for item in itertools.combinations([1, 2, 3, 4], 3):
    arr=[1]*5
    for index in item:
        arr[index-1]=0
    array5.append(arr)
for item in itertools.combinations([1, 2, 3, 4, 5], 3):
    arr=[1]*6
    for index in item:
        arr[index-1]=0
    array6.append(arr)

def makeTemplates(n):
    combos=[]
    num=str(n)
    arr=array6
    if(len(num)==5):
        arr=array5
    elif(len(num)!=6):
        raise NotImplementedError
    for combo in arr:
        template=""
        for i in range(len(num)):
            if(combo[i]==1):
                template+=num[i]
            else:
                template+='*'
        combos.append(template)
    return combos

def getNumberFromTemplate(temp, k):
    num=""
    for char in temp:
        if(char=='*'):
            num+=str(k)
            continue
        num+=char
    return int(num)


for i in range(100000, 1000000):
    templates=makeTemplates(i)
    for template in templates:
        count=0
        for k in range(1, 10):
            num=getNumberFromTemplate(template, k)
            if(addmath.isPrime(num)):
                count+=1
            if(count>=8):
                print('\n\n'+str(num)+"is part of the 8 prime family, but not the smallest prime. The template is "+str(template))
                for k in range(1, 10):
                    num = getNumberFromTemplate(template, k)
                    if(addmath.isPrime(num)):
                        print("The smallest of the family is "+str(num))
                        sys.exit(0)
    print(i)

