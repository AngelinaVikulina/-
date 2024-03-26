
#Из последовательности на n целых чисел создать новую последовательность, в
# которой каждый последующий элемент равен квадрату суммы двух соседних элементов.
def create_new_sequence(sequence):
    return [(sequence[i+1]**2 if i == 0 else sequence[i-1]**2 if i == len(sequence) - 1 else (sequence[i-1] + sequence[i+1])**2) for i in range(len(sequence))]

input_sequence = [1, 2, 3, 4, 5]
new_sequence = create_new_sequence(input_sequence)
print(new_sequence)


