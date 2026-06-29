# #модуль (библеотека, dependancy) - это код наптсанный другим разработчиком и доступный к использованию
#
# #функция help используется для обращение технической документации
# # help("modules")
#
# # help("math")
#
# #ИМПОРТ ЦЕЛОЙ БИБЛЕОТЕКИ
# # import math
#
# from math import floor, pi, ceil as maximize
#
# import area
# from area import areaofRectangle
#
# #floor: 15.99 -> 15
# #ceil: 22.03 -> 23
# #пример импорта своей библеотеки
# #import area *
#
#
# # def circumference(radius):
# #     return maximize(2*radius*pi)
#
# print("длина окружности с радиусом 4 см:",circumference(4))
# print("площадь окружности с радиусом 4 см:",area.areaOfCircle(4),"см2")
import random
from ctypes import HRESULT


#task1
# num1 = int(input("введите первое число"))
# num2 = int(input("введите второе число"))
# choice = input("выберите операцию(+, -, *, /):")
# if choice == "+":
#     print(f"результат: {num1 + num2}")
# elif choice == "-":
#     print(f"результат: {num1 - num2}")
# elif choice == "*":
#     print(f"результат: {num1 * num2}")
# elif choice == "/":
#     print(f"результат: {num1 / num2}")

#task2
# def plus(a, b):
#     result = a + b
#     return result
# def minus(a, b):
#     result = a - b
#     return result
# def multiply(a, b):
#     result = a * b
#     return result
# def divide(a, b):
#     result = a / b
#     return result
#
# num1 = float(input("введите первое число"))
# num2 = float(input("введите второе число"))
# choice = input("выберите операцию(+, -, *, /): ")
#
# if choice == "+":
#     print("результат:", plus(num1, num2))
# elif choice == "-":
#     print("результат:", minus(num1, num2))
# elif choice == "*":
#     print("результат:", multiply(num1, num2))
# elif choice == "/":
#     print("результат:", divide(num1, num2))
# else:
#     print("Ошибка")

#task3
# import random
# user = input("введите ваш выбор:камень, ножницы или бумага: ")
# computer = random.choice(["камень", "ножницы", "бумага"])
# print("ваш выбор", user)
# print("КОМП выбрал:", computer)
# if user == computer:
#     print("ничья")
# elif user == "камень" and computer == "ножницы":
#     print(f"вы выиграли")
# elif user == "ножницы" and computer == "бумага":
#     print(f"вы выиграл")
# elif user == "бумага" and computer == "камень":
#     print(user, "вы выиграли")
# else:
#     print(computer, "комп выиграл")


#task4
# import random
# guess = random.randint(1, 20)
# print("я загадал число от 1 до 20,угадай")
# user_guess = 0
# while user_guess != guess:
#     user_guess = int(input("твой ответ"))
#     if user_guess < guess:
#         print("мое число больше")
#     elif user_guess > guess:
#         print("мое число меньше")
#     else:
#         print(f"ты угадал мое загаданное число: чилсо было {guess}")


