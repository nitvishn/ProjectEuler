N=1000
for x in range(1,N):
    y = x+1
    z = y+1
    while z <= N:
        while z * z < x * x + y * y:
            z = z + 1
        if z * z == x * x + y * y and z <= N and z+x+y==N:
            print(x,y,z)
        y = y + 1
