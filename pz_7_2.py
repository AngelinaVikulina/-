#Дана строка-предложение на русском языке и число K (0 < K < 10). Зашифровать
#строку, выполнив циклическую замену каждой буквы на букву того же регистра,
#расположенную в алфавите на K-й позиции после шифруемой буквы (например, для
#K = 2 «А» перейдет в «В», «а» — в «в», «Б» — в «Г», «я» — в «б» и т. д.). Букву «ё»
#в алфавите не учитывать, знаки препинания и пробелы не изменять.

sentence = input("Введите предложение на русском языке: ")
k = int(input("Введите число K: "))

encrypted_sentence = ""

for letter in sentence:
    if letter.isalpha() and letter != "ё":
        if letter.isupper():
            encrypted_letter = chr((ord(letter) - ord('А') + k) % 26 + ord('А'))
        else:
            encrypted_letter = chr((ord(letter) - ord('а') + k) % 26 + ord('а'))
    else:
        encrypted_letter = letter
    encrypted_sentence += encrypted_letter

print("Зашифрованное предложение:", encrypted_sentence)