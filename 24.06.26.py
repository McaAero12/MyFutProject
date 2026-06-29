# class Phone:
#     def __init__(self, name, battery):
#         self.name = name
#         self.battery = battery
#
#     def charge(self):
#         print(f" процент вашего {self.name} {self.battery}!")
#
# p1 = Phone("iphone" , "91")
# p1.charge()

# class Animal:
#     def info(self):
#         print("это животное.")
#
# class Dog(Animal):
#     def bark(self):
#         print("Гав!")
#
# dog = Dog()
# dog.info()
# dog.bark()
#
# class Transport:
#     def move(self):
#         print("транспорт движется")
#
# class Car(Transport):
#     def honk(self):
#         print("БИП БИП!")
#
# car = Car()
# car.move()
# car.honk()

# class Device:
#     def turn_on(self):
#         print("включаюсь")
#
# class Smartphone(Device):
#     def use_app(self):
#         print("открываю приложение.")
#
# phone = Smartphone
# phone.turn_on()
# phone.use_app()

# class Words:
#     def __init__(self):
#         self._recipe = "Apple"
#         self.__pin = 1234
#
# class Secret(Words):
#     def reveal(self):
#         print(self._recipe)
#         print(self.__pin)
#
# r1 = Secret()
# r1.reveal()
# r1.__pin()

# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance
#
#     def deposit(self, amount):
#         self.__balance += amount
#
#     def get_balance(self):
#         return self.__balance
#
# acc = BankAccount("Айгуль", 1000)
# print(acc.__balance)
# print(acc.get_balance())

# class Animal:
#     def __init__(self):
#         print("я животное")
#
#
# class Dog(Animal):
#     def __init__(self):
#         super().__init__()
#         print("я собака")
#
# Dog()

# class Phone:
#     def __init__(self, brand, price):
#         self.brand = brand
#         self.price = price
#
# class Iphone(Phone):
#     def __init__(self, brand, price, color):
#         super().__init__(brand, price)
#         self.color = color
#
# p1 = Phone("айфон", "1500$"a)
# Iphone()




#task1
# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def info(self):
#         print("Это животное по кличке", self.name)
#
#
# class Cat(Animal):
#     def sound(self):
#         print(self.name, "говорит: Мяу!")
#
#
# class Dog(Animal):
#     def sound(self):
#         print(self.name, "говорит: Гав!")
#
#
# cat = Cat("Том")
# dog = Dog("Бобик")
#
# cat.info()
# cat.sound()
#
# dog.info()
# dog.sound()

class Transport:
    def __init__(self):
        self._mileage = 0

    def add(self, km):
        self._mileage += km

    def show(self):
        print("текущий пробег:", self._mileage)

class Car(Transport):
    pass

car = Car()

car.add(100)

print("машина проехала 100 км")
car.show()


class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, money):
        self.__balance += money
        print("пополнение на:", money)
        print("новый баланс:", self.__balance)

    def withdraw(self, money):
            self.__balance -= money

    def get_balance(self):
        print("баланс", self.__balance)

acc = BankAccount(2000)
acc.deposit(2000)

acc.get_balance()