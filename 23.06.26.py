# class House:
#     def __init__(self, name, price):
#         self.name =  name
#         self.price = price
#
#
# home = House("ЖК Vela", "Цена за кв 1500$")
# print(home.name)
# print(home.price)
from logging import FileHandler


# class Robot:
#     def __init__(self, name, battery, hp=100):
#         self.name = name
#         self.battery = battery
#         self.hp = hp
#
#     def say_hi(self):
#         print(f"Привет, я {self.name}!")
#
#     def charge(self, amount):
#         self.battery += amount
#         print(f"{self.name} подзарядился на {amount}%. Теперь заряд: {self.battery}%")
#
#     def distance(self, distance):
#         print(f"{self.name} проехал {distance} метров")
#
#     def attack(self, target):
#         target.hp -= 10
#         print(f"{self.name} атаковал {target.name}! у {target.name} осталось {target.hp} HP")
#
# r1 = Robot("ROBOMAX", 80, 70)
# r2 = Robot("Void", 70, 50)
# r1.say_hi()
# r1.charge(10)
# r1.distance(9)
# r1.attack(r2)












#
# class Pet:
#     def  __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def greet(self):
#         print(f"Привет! меня зовут {self.name}, мне {self.age} года")
# P1 = Pet("Барсик", "3")
# P1.greet()
#
# class Player:
#     def __init__(self, player):
#         self.player = player
#
#     def jump(self):
#         print(f"игрок {self.player} прыгает!")
#
# P1 = Player("DragonX")
# P1.jump()
#
#
# class Fighter:
#     def __init__(self, name, hp=100):
#         self.name = name
#         self.hp = hp
#     def attack(self, target):
#         print(f"{self.name} атакует {target.name}! у MAX осталось {target.hp} HP")
#
# F1 = Fighter("Sam", 70)
# F2 = Fighter("MAX", 90)
# F1.attack(F2)
#
#
# class BankAccount:
#     def __init__(self, balance):
#         self.balance = balance
#
#     def deposit(self, amount):
#         self.balance += amount
#         print(f"Пополнение на {amount} сом. Новый баланс: {self.balance} сом")
# b1 = BankAccount(5000)
# b1.deposit(2000)
# b1.deposit(3000)
#
#
#
# class Phone:
#     def __init__(self, battery_level):
#         self.battery_level = battery_level
#
#     def check_battery(self):
#         if self.battery_level <= 20:
#             print(f"внимание! низкий заряд: {self.battery_level}%")
# phone1 = Phone(15)
# phone1.check_battery()


#homework
# class Pet:
#     def __init__(self, name):
#         self.name = name
#         self.satiety = 50
#         self.happiness = 50
#     def feed(self):
#         self.satiety += 20
#         self.happiness -= 5
#
#         if self.satiety > 100:
#             self.satiety = 100
#
#         if self.happiness <= 0:
#             print(f"{self.name} очень грустит")
#     def play(self):
#         self.happiness += 25
#         self.satiety -= 15
#
#         if self.happiness > 100:
#             self.happiness = 100
#
#         if self.satiety <= 0:
#             print(f"{self.name} очень голоден")
#
#     def get_status(self):
#         print(f"\nПитомец: {self.name}")
#         print(f"Сытость: {self.satiety}")
#         print(f"Счастье: {self.happiness}")
#
#
# pet = Pet("Барсик")
#
# pet.play()
# pet.play()
#
# pet.get_status()
#
# pet.feed()
#
# pet.get_status()