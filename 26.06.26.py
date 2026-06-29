# class Robot:
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return f"{self.name}"
#
#
# r = Robot("MAX")
# print(r)
#
# class Car:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#     def __str__(self):
#         return f"{self.name}, {self.price}"
#
# c = Car("FERRARI", 1500$)
# print(c)


# class Wallet:
#     def __init__(self, amount):
#         self.amount = amount
#
#     def __add__(self, other):
#         return Wallet(self.amount + other.amount)
#     def __str__(self):
#         return f"Кошелек: {self.amount} сом"
#
#
# w1 = Wallet(1000)
# w2 = Wallet(500)
# print(w1 + w2)





#
# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return f"Кот {self.name}, {self.age}"
#
# c = Animal("Барсик", "3года")
# print(c)
#
#
# class BankAccount:
#     def __init__(self, amount):
#         self.amount = amount
#
#     def __add__(self, other):
#         return BankAccount(self.amount + other.amount)
#     def __str__(self):
#         return f"Баланс: {self.amount}"
#
# b1 = BankAccount(1000)
# b2 = BankAccount(500)
# print(b1 + b2)
#
#
# class Fighter:
#     def __init__(self, level, rank):
#         self.level = level
#         self.rank = rank
#
#     def __eq__(self, other):
#         return self.level == other.level and self.rank == other.rank
#
# f1 = Fighter(58, "ВОИН")
# f2 = Fighter(60, "ВОИН")
# print(f1 == f2)
#
#
# class Team:
#     def __init__(self, players):
#         self.players = players
#
#     def __getitem__(self, index):
#         return self.players[index]
#
#     def __len__(self):
#         return len(self.players)
#
# team = Team(["Viper", "MAX", "MINA"])
# print(team[0])
# print(len(team))





