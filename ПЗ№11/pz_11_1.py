# Вариант 5.
# 1. Средствами языка Python сформировать текстовый файл (.txt), содержащий
# последовательность из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Исходные данные:
# Количество элементов:
# Сумма элементов:
# Элементы, умноженные на минимальный элемент:

import random


sequence = [random.randint(-50, 50) for i in range(20)]

count = len(sequence)
total = sum(sequence)
min_element = min(sequence)
multiplied = [i * min_element for i in sequence]
import random


with open('numbers.txt', 'w') as file:
    file.write(' '.join(map(str, sequence)))

print('Файл numbers.txt успешно создан.')

with open('output.txt', 'w') as f:
    f.write('Исходные данные: {}\n'.format(sequence))
    f.write('Количество элементов: {}\n'.format(count))
    f.write('Сумма элементов: {}\n'.format(total))
    f.write('Элементы, умноженные на минимальный элемент: {}\n'.format(multiplied))
