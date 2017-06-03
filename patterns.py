rule = {
    '111': '0',
    '110': '1',
    '101': '0',
    '100': '1',
    '011': '1',
    '010': '0',
    '001': '1',
    '000': '0'
}

rows = 40
cols = rows * 2 + 1

matrix = []

for i in range(rows):

    row = []

    for j in range(cols):
        if i == 0 and j == cols // 2:
            row.append(1)
        else:
            row.append(0)

    matrix.append(row)

for i in range(1, rows):
    for j in range(1, cols - 1):
        parents = [matrix[i - 1][j - 1], matrix[i - 1][j], matrix[i - 1][j + 1]]

        if parents == [1, 1, 1]:
            matrix[i][j] = 0
        elif parents == [1, 1, 0]:
            matrix[i][j] = 1
        elif parents == [1, 0, 1]:
            matrix[i][j] = 0
        elif parents == [1, 0, 0]:
            matrix[i][j] = 1
        elif parents == [0, 1, 1]:
            matrix[i][j] = 1
        elif parents == [0, 1, 0]:
            matrix[i][j] = 0
        elif parents == [0, 0, 1]:
            matrix[i][j] = 1
        elif parents == [0, 0, 0]:
            matrix[i][j] = 0
        else:
            print("error")

print("\n")

for row in matrix:
    for item in row:
        if item == 0:
            print(" ", end="")
        elif item == 1:
            print("#", end="")
        else:
            print("error")
    print()
