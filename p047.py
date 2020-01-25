from addmath import *
num=210
while(True):
    if(num_factors(num)!=4):
        num+=1
        continue
    print(num)
    if(num_factors(num+1)==4 and num_factors(num+2)==4 and num_factors(num+3)==4):
        print(num, "= ANSWER")
        break
    num+=1