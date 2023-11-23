#Дано вещественное число - цена 1 кг конфет. Вывести стоимость 1.2, 1.4, ..., 2 кг
# конфет
price_per_kg = input("Введите цену 1 кг конфет: ")
while type(price_per_kg) != int:
    try:
        price_per_kg = int(price_per_kg)
    except ValueError:
        print('Ввели неправильно!')
        price_per_kg = input("Введите цену 1 кг конфет: ")
for kg in range(12, 21, 2):
    total_price = price_per_kg * (kg / 10)
    print(f"Стоимость {kg / 10} кг конфет: {total_price} рублей")