max_solutions=0
p=0
for N in range(0, 1000, 12):
    solutions=0
    for x in range(1,N):
        y = x+1
        z = y+1
        while z <= N:
            while z * z < x * x + y * y:
                z = z + 1
            if z * z == x * x + y * y and z <= N and z+x+y==N:
                solutions+=1
            y = y + 1
    if(solutions>max_solutions):
        max_solutions=solutions
        p=N
        print(p)
print(p)