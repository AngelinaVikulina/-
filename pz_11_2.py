# 2.Из предложенного текстового файла (text18-5.txt) вывести на экран его содержимое,
# количество символов в тексте. Сформировать новый файл, в который поместить текст в
# стихотворной форме предварительно заменив символы нижнего регистра на верхний.

with open('text18-5.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    print("Содержимое файла text18-5.txt:")
    print(text)



    char_count = len(text)
    print("\nКоличество символов в тексте:", char_count)


with open('poem.txt', 'w') as new_file:
    poem_text = text.upper()
    new_file.write(poem_text)

print("\nФайл poem.txt успешно создан.")
