"""
              B(10,30)
                / \
               /   \
              /     \
             /   P   \      P'
            /         \
     A(0,0) ----------- C(20,0)
1) Calculate area of the given triangle, i.e., area of the triangle ABC in the above diagram. Area A = [ x1(y2 – y3) + x2(y3 – y1) + x3(y1-y2)]/2
2) Calculate area of the triangle PAB. We can use the same formula for this. Let this area be A1.
3) Calculate area of the triangle PBC. Let this area be A2.
4) Calculate area of the triangle PAC. Let this area be A3.
5) If P lies inside the triangle, then A1 + A2 + A3 must be equal to A.
"""

from addmath import shoelace


def contains_origin(A, B, C):
    P = (0, 0)
    A1 = shoelace([P, A, B])
    A2 = shoelace([P, B, C])
    A3 = shoelace([P, A, C])
    Area = shoelace([A, B, C])
    return A1 + A2 + A3 == Area

def get_triangles():
    file = open("p102_triangles.txt")
    triangles = []
    for line in file:
        line = line.split(',')
        points = []
        for i in range(len(line)//2):
            points.append((int(line[2*i]), int(line[2*i + 1])))
        triangles.append(points)
    return triangles

triangles = get_triangles()
n = 0
for triangle in triangles:
    if contains_origin(triangle[0], triangle[1], triangle[2]):
        n += 1
print(n)
