def get_matrix(n, m, value):
    matrix = []
    if n <= 1 and m <= 1:
        return []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(value)
        matrix.append(row)
        print(matrix)
    return matrix

n = int(input('Введите количество строк: '))
m = int(input('Введите количество столбцов: '))
value = int(input('Введите значение матрицы: '))
matrix = get_matrix(n, m, value)
if not matrix:
    print('Пустая матрица ')
for i in matrix:
        print(*i)









#def get_diagonal_matrix(n, value):
#     matrix = []
#     for i in range(n):
#         row = []
#         for j in range(n):
#             if i == j:
#                 row.append(value)
#             else:
#                 row.append(0)
#         matrix.append(row)
#     return matrix
#
# n = int(input('Введите размер матрицы: '))
# value = int(input('Введите значение для диагонали: '))
# matrix = get_diagonal_matrix(n, value)
# for row in matrix:
#     print(*row)