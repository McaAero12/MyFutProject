# #пример как создать set.
# numbers = [1, 2, 2, 3, 4, 4, 5]
# unique_numbers = set(numbers)
# print(unique_numbers)  # - (1, 2, 3, 4, 5)
#
# fruits = {"яблоко", "банан"}
# fruits.add("груша")
# fruits.remove("яблоко")
# print(fruits)
#
from enum import unique

# set1 = {"Alex", "Gordon", "Natalie"}
# set1.add("Bob")
# set1.discard("Tom")
# print(set1)

# students = {"Андрей", "Олег", "Алексей"}
# print("Катя" in students)
# print("Олег" in students)

# set1 = {"Alex", "Gordon", "Natalie"}
# set2 = {"Alex", "Rachel", "Natalie"}
# print(set1 | set2)
# print(set1.union(set2)) - обьединение
# print(set1 & set2)
# print(set1.intersection(set2)) - пересечение
# print(set2 - set1)
# print(set1.symmetric_difference(set2)) - симметричная разность

#task1
# numbers = input("введите числа:").split()
# unique_numbers = set(numbers)
# print(f"уникальные числа:", unique_numbers)

#task2
# names = set(input("ведите имена:" ).split())
# name = input("кого ищем?")
# if name in names:
#     print("есть в списке")
# else:
#     print("такого нету")

#task3
# favourite = set(input("Любимые").split())
# school = set(input("В школе").split())
# print("Совпадают", favourite & school)

# #task4
# s = set(input("Ожидались").split())
# come = set(input("Пришли").split())
# print("не пришли", s - come)

#task5
# text = input("ведите текст")
# words = text.split()
# unique_words = set(words)
# print("уникальные слова", unique_words)