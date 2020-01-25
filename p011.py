import numpy as np

def load():
    file=open("11.txt","r")
    mat=[]
    for line in file:
        temp=getIntsFromLine(line)
        mat.append(temp)
    return mat

def getIntsFromLine(line):
    ints=[]
    temp=""
    for char in line:
        if char.isdigit():
            temp+=char
        if(len(temp)==2):
            ints.append(int(temp))
            temp=""
    return ints

def findDiagonal(mat):
    def getDiagonals(matrix):
        a = np.array(matrix)
        diags = [a[::-1, :].diagonal(i) for i in range(-a.shape[0] + 1, a.shape[1])]
        diags.extend(a.diagonal(i) for i in range(a.shape[1] - 1, -a.shape[0], -1))
        return [n.tolist() for n in diags]
    maxnum=0
    for line in getDiagonals(mat):
        for cursor in range(len(line)):
            if not cursor+3>len(line)-1:
                temp = 1
                for num in line[cursor:cursor + 4]:
                    temp *= num
                if (temp > maxnum):
                    print(line[cursor:cursor + 4])
                maxnum = max(temp, maxnum)
    return maxnum

def findhorizontal(mat):
    maxnum=0
    for line in mat:
        for cursor in range(20):
            if(not cursor+3>19):
                temp=1
                for num in line[cursor:cursor+4]:
                    temp*=num
                if(temp>maxnum):
                    print(line[cursor:cursor+4])
                maxnum=max(temp, maxnum)
    return maxnum

def findvertical(mat):
    maxnum=0
    for j in range(20):
        for i in range(20):
            if not i+3>19:
                temp=1
                for k in range(3):
                    temp*=mat[i+k][j]
                maxnum=max(temp, maxnum)
    return maxnum

mat=load()
print(findDiagonal(mat))