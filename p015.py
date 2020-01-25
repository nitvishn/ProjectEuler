def pascalTriangle(row,column):
    triangle=[[1],[1,2]]
    n=2
    k=2
    for i in range(row**2):
        k+=1
        if(n==k-1):
            triangle[n-1].append(1)
            n+=1
            k=2
            triangle.append([1,])
        triangle[n-1].append(triangle[n-2][k-2]+triangle[n-2][k-1])
    try:
        return triangle[row-1][column-1]
    except:
        return "Sorry, wrong row and column"

def version_one():
    n=int(input("N: "))
    k=int(input("K: "))
    print(pascalTriangle(n,k))


# def version_two():


if __name__ == "__main__":
    version_one()
