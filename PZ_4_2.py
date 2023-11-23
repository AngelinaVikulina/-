#Дано целое число N (>0). Используя операции деления нацело и взятия
# остатка от деления,найти количество и сумму его цифр.
N = input("Введите целое число:\n")
while type(N) != int:
    try:
        N = int(N)
    except ValueError:
        print('Ввели неправильно!')
        N = input("Введите целое число:\n ")

sum_of_digits = 0
count_of_digits = 0

while N > 0:
    digit = N % 10
    sum_of_digits += digit
    count_of_digits += 1
    N //= 10

print("Количество цифр:", count_of_digits)
print("Сумма цифр:", sum_of_digits)