#В матрице элементы второго столбца возвести в квадрат
import random
matrix = [[random.randint(1, 10) for _ in range(3)] for _ in range(3)]
def square(x):
    return x ** 2

result_matrix = [row[:1] + list(map(lambda x: square(x), row[1:2])) + row[2:] for row in matrix]

print("Исходная матрица:")
for row in matrix:
    print(row)

print("\nРезультат:")
for row in result_matrix:
    print(row)
