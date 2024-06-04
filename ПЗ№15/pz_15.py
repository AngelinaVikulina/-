# -*- coding: utf-8 -*-
# Приложение БАНК для отслеживания накапливаемых на счетах клиентов банка
# сумм. Таблица Клиент должна содержать следующую информацию: Код клиента,
# Клиент (Ф.И.О.), Периодический платеж, Годовой %, Срок вклада, Пластиковая карта
# (логическое поле), Конечная сумма.
import sqlite3

# Создание подключения к базе данных
conn = sqlite3.connect('bank.db')
cursor = conn.cursor()

# Создание таблицы
cursor.execute('''CREATE TABLE IF NOT EXISTS Clients
                (ClientCode INTEGER PRIMARY KEY, FullName TEXT, Payment REAL, AnnualInterestRate REAL, DepositTerm INTEGER, HasCreditCard INTEGER, FinalAmount REAL)''')

# Ввод данных в БД
def add_client(client_data):
    cursor.execute("INSERT INTO Clients VALUES (?,?,?,?,?,?,?)", client_data)
    conn.commit()

# Готовые данные для ввода
clients_data = [
    (1, "Иванов Иван Иванович", 10000.0, 5.0, 12, 1, 120000.0),
    (2, "Петров Петр Петрович", 15000.0, 4.5, 24, 0, 180000.0),
    (3, "Сидоров Алексей Васильевич", 20000.0, 6.0, 36, 1, 240000.0),
    (4, "Иванов Николай Максимович", 10000.0, 5.0, 12, 1, 120000.0),
    (5, "Алексеев Алексей Петрович", 15000.0, 4.5, 24, 0, 180000.0),
    (6, "Владиславов Владислав Васильевич", 20000.0, 6.0, 36, 1, 240000.0),
    (7, "Васильева Ангелина Николаевна", 10000.0, 5.0, 12, 1, 120000.0),
    (8, "Викулина Катерина Ивановна", 15000.0, 4.5, 24, 0, 180000.0),
    (9, "Иванова Катерина Петровна", 20000.0, 6.0, 36, 1, 240000.0),
    (10, "Максимов Максим Иванович", 10000.0, 5.0, 12, 1, 120000.0),


]

# Добавление данных в БД
for data in clients_data:
    add_client(data)

# Вывод информации о таблице
def show_table_info():
    cursor.execute("SELECT * FROM Clients")
    table_data = cursor.fetchall()
    for row in table_data:
        print(row)

print("\nИнформация о таблице:")
show_table_info()

# Поиск клиента по коду клиента
def search_by_client_code(client_code):
    cursor.execute(f"SELECT * FROM Clients WHERE ClientCode={client_code}")
    return cursor.fetchall()

# Поиск клиента по Ф.И.О.
def search_by_full_name(full_name):
    cursor.execute(f"SELECT * FROM Clients WHERE FullName='{full_name}'")
    return cursor.fetchall()

# Удаление клиента по коду клиента
def delete_by_client_code(client_code):
    cursor.execute(f"DELETE FROM Clients WHERE ClientCode={client_code}")
    conn.commit()

# Удаление клиента по Ф.И.О.
def delete_by_full_name(full_name):
    cursor.execute(f"DELETE FROM Clients WHERE FullName='{full_name}'")
    conn.commit()



# Редактирование данных клиента по коду клиента
def edit_client_data(client_code, new_final_amount):
    cursor.execute(f"UPDATE Clients SET FinalAmount={new_final_amount} WHERE ClientCode={client_code}")
    conn.commit()




client_code_to_search = 2
client_code_to_search1 = 3
client_code_to_search2 = 4
full_name_to_search = "Сидоров Алексей Васильевич"
full_name_to_search1 = "Петров Петр Петрович"
full_name_to_search2 = "Иванова Катерина Петровна"


print("\nПоиск клиента по коду клиента:")
print(search_by_client_code(client_code_to_search))
print(search_by_client_code(client_code_to_search1))
print(search_by_client_code(client_code_to_search2))


print("\nПоиск клиента по Ф.И.О.:")
print(search_by_full_name(full_name_to_search))
print(search_by_full_name(full_name_to_search1))
print(search_by_full_name(full_name_to_search2))

#редактирование

print("\n Обновим данные для 1, 2 , 3 клента")
client_code_to_edit = 1
new_final_amount = 130000.0
edit_client_data(client_code_to_edit, new_final_amount)
client_code_to_edit1 = 2
new_final_amount = 160000.0
edit_client_data(client_code_to_edit1, new_final_amount)
client_code_to_edit2 = 3
new_final_amount = 190000.0
edit_client_data(client_code_to_edit2, new_final_amount)


print("\nИнформация о таблице после операций:")
show_table_info()


#удаление по коду
print("\nУдалим клиентов 4, 5 , 6 по коду:")
client_code_to_delete = 4
client_code_to_delete1 = 5
client_code_to_delete2 = 6
delete_by_client_code(client_code_to_delete)
delete_by_client_code(client_code_to_delete1)
delete_by_client_code(client_code_to_delete2)


print("\nИнформация о таблице после операций:")
show_table_info()

#удалим по фио
print("Удалим Петрова Петра Петровича,Максимова Максима Ивановича, Иванову Катеринау Петровну ")
full_name_to_delete = "Петров Петр Петрович"
delete_by_full_name(full_name_to_delete)
full_name_to_delete1 = "Максимов Максим Иванович"
delete_by_full_name(full_name_to_delete1)
full_name_to_delete2 = "Иванова Катерина Петровна"
delete_by_full_name(full_name_to_delete2)


print("\nИнформация о таблице после операций:")
show_table_info()


conn.close()
