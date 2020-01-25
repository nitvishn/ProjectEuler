file=open("p067_triangle_test.txt","r")
triangle=[]
for line in file:
    nums=line.split(' ')
    for index in range(len(nums)):
        nums[index]=int(nums[index])
    triangle.append(nums)

def problem(triangle):
    for row in range(len(triangle)-2,-1,-1):
        for number in range(len(triangle[row])):
            triangle[row][number]+=max(triangle[row+1][number],triangle[row+1][number+1])
    return triangle[0][0]

print(problem(triangle))
