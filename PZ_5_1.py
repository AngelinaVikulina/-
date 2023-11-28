# С помощью функций получить вертикальную и горизонтальную линии. Линия
# проводится многократной печатью символа. Заключить слово в рамку из
# полученных линий
def vertical_line(length):
    print("| " + word + " |")


def horizontal_line(length):
    print("_" * length)


word = "Hello"
lenght = len(word)
horizontal_line(lenght + 4)
vertical_line(word)
horizontal_line(lenght + 4)


