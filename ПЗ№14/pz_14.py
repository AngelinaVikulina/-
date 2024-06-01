# Из исходного текстового файла (ip_address.txt) из раздела «Частоупотребимые
# маски» перенести в первый файл строки с нулевым четвертым октетом, а во второй
# – все остальные. Посчитать количество полученных строк в каждом файле.
with open("ip_address.txt", "r") as file:
    lines = file.readlines()

with open("file1.txt", "w") as file1, open("file2.txt", "w") as file2:
    for line in lines:
        line = line.strip()
        if line and line.count('.') == 3:
            octets = line.split('.')
            if octets[3] == '0':
                file1.write(line + '\n')
            else:
                file2.write(line + '\n')

with open("file1.txt", "r") as file1:
    count_file1 = len(file1.readlines())

with open("file2.txt", "r") as file2:
    count_file2 = len(file2.readlines())

print(f"Количество строк в file1.txt: {count_file1}")
print(f"Количество строк в file2.txt: {count_file2}")
