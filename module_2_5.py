def get_matrix(n, m, value):
    matrix = list()
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    return matrix

n = int(input('Rows: '))
m = int(input('Columns: '))
value = int(input('Value of matrix elements: '))

print(get_matrix(n, m, value))