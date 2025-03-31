import random
N = 32

matrix_a = [[random.randint(1, 10)] * N for _ in range(N)]
matrix_b = [[random.randint(1, 10)] * N for _ in range(N)]
matrix_c = [[0] * N for _ in range(N)]

for lin in range(N):
    for col in range(N):
        matrix_c[lin][col] = matrix_a[lin][col] + matrix_b[lin][col] 

print(matrix_c)