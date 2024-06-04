#Создайте класс «Банк», который имеет атрибуты суммы денег и процентной ставки.
# Добавьте методы для вычисления процентных начислений и снятия денег
#
# Для задачи из блока 1 создать две функции, save_def и load_def, которые позволяют
# сохранять информацию из экземпляров класса (3 шт.) в файл и загружать ее обратно.
# Использовать модуль pickle для сериализации и десериализации объектов Python в
# бинарном формате.
import pickle

class Bank:
    def __init__(self, money, interest_rate):
        self.money = money
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.money * self.interest_rate / 100

    def withdraw_money(self, amount):
        if amount <= self.money:
            self.money -= amount
        else:
            print("Not enough money in the account.")

def save_def(objects, filename):
    with open(filename, 'wb') as file:
        pickle.dump(objects, file)

def load_def(filename):
    with open(filename, 'rb') as file:
        objects = pickle.load(file)
    return objects


bank1 = Bank(1000, 2)
bank2 = Bank(5000, 3)
bank3 = Bank(200, 1.5)


banks_to_save = [bank1, bank2, bank3]
save_def(banks_to_save, 'banks.pkl')


loaded_banks = load_def('banks.pkl')


for bank in loaded_banks:
    print("Initial amount in the account:", bank.money)
    print("Interest for the account:", bank.calculate_interest())
    bank.withdraw_money(100)
    print("Amount in the account after withdrawal:", bank.money)
    print()
