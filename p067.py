def loadTriangle():
    file = open("p067_triangle.txt", "r")
    triangle = []
    for line in file:
        line = line.replace('\n', '')
        line = line.split()
        triangle.append([])
        for num in line:
            triangle[-1].append(int(num))
    return triangle

def choices(i, j, triangle):
    if i >= len(triangle) - 1:
        raise ValueError
    if j >= len(triangle[i]):
        raise ValueError
    return (triangle[i+1][j], triangle[i+1][j+1])

def layer(n, triangle):
    place = len(triangle) - n - 1
    if n == 0:
        return triangle[place]
    layerBefore = layer(n - 1, triangle)
    L = []
    for i in range(len(triangle[place])):
        item = triangle[place][i] + max(layerBefore[i], layerBefore[i+1])
        L.append(item)
    return L

triangle = loadTriangle()
print(layer(len(triangle) - 1, triangle)[0])
