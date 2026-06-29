# import this
from enum import unique

# squares = [x**2 for x in range(1, 11) if x % 2 == 0]
# print(squares)
#
# list1 = [x for x in range(1, 11)]
# print(list1)
#
# words = ["python", "is", "awesome"]
# long = [w for w in words if len(w) > 5]
# #вывод: python awesome
# text = "hello"
# letters = {ch for ch in text}
# # h,e,l,l,o
# codes = {ch: ord(ch) for ch in "abc"}
# #a:97, b:98, c:99

# numbers = [1, 2, 3, 4, 5]
# squares = [x**2 for x in numbers]
# print(squares)
#
# even = [x for x in range(10) if x % 2 == 0]
# print(even)
#
# labels = ["четное" if x % 2 == 0 else "нечетное" for x in range(5)]
# print(labels)
#
# with open("numbers.txt") as f:
#     positives = [int(line) for line in f if int(line) > 0]
# print(positives)
#
# names = ["oleg", "borya", "vlad", "oleg"]
# unique_names = {name for name in names}
# print(unique_names)
#
# words = ["python", "is", "cool"]
# lentgh = {w: len(w) for w in words}
# print(lentgh)

#task1
# squares = [x**2 for x in range(1, 11) if x % 2 == 0]
# print(squares)

#task2
# text = input("введите строку")
# letters = {ch for ch in text}
# unique_words = letters
# print(f"уникал буквы", unique_words )

#task3
# words = ["hello", "python"]
# lentgh = {w: len(w) for w in words}
# print(lentgh)

#task4
# list1 = [[1, 2], [3, 4], [5]]
# flat = [x for lst in list1 for x in lst]
# print(flat)

#task5
# names = ["ivan", "katya"]
# emails = [f"{name}@school.com" for name in names]
# print(emails)