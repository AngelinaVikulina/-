
# 2. Сгенерировать матрицу, в которой нечетные элементы заменяются на 0.
import random

matrix = [[random.randint(1, 10) for _ in range(3)] for _ in range(3)]
result_matrix = [[0 if x % 2 != 0 else x for x in row] for row in matrix]

print("Исходная матрица:")
for row in matrix:
    print(row)

print("\nРезультат:")
for row in result_matrix:
    print(row)
