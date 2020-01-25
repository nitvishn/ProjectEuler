def load_matrix():
    matrix = []
    for line in open('p082_matrix.txt', 'r'):
        L = []
        for string in line.replace('\n', '').split(','):
            L.append(int(string))
        matrix.append(L)
    return matrix

minimum_sum_memo = {}
def minimum_sum(matrix, i, j, prohibited=()):
    if j == len(matrix[i]) - 1:
        return matrix[i][j]

    if i == len(matrix[i]) - 1:
        prohibited = prohibited + ('Down', )
    elif i == 0:
        prohibited = prohibited + ('Up', )

    if (i, j, prohibited) in minimum_sum_memo:
        return minimum_sum_memo[(i, j, prohibited)]

    minVal = minimum_sum(matrix, i, j+1)
    if 'Down' not in prohibited:
        minVal = min([minVal, minimum_sum(matrix, i+1, j, prohibited=('Up', ))])
    if 'Up' not in prohibited:
        minVal = min([minVal, minimum_sum(matrix, i-1, j, prohibited=('Down', ))])

    minimum_sum_memo[(i, j, prohibited)] = matrix[i][j] + minVal
    return matrix[i][j] + minVal
#
matrix = [
    [131, 673, 234, 103, 18],
    [201, 96, 342, 965, 150],
    [630, 803, 746, 422, 111],
    [537, 699, 497, 121, 956],
    [805, 732, 524, 37, 331]
]
matrix = load_matrix()
minVal = minimum_sum(matrix, 0, 0)
for i in range(1, len(matrix)):
    minVal = min([minVal, minimum_sum(matrix, i, 0)])
print(minVal)
