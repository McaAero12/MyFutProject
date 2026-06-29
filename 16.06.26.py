# try:
#     a = int(input("введите число"))
#     print(1/0)
# except:
#     print("Что-то пошло не так,но программа не рухнула!")
#
# try:
#     a = int(input("введите первое число"))
#     b = int(input("введите второе число"))
#     print(a / b)
# except TypeError:
#     print("введите число а не букву")
# except Exception as e:
#     print(f"произошла неизвестная ошибка {e} ")
# except ValueError:
#     print("пожалуйста ввeдите только числа")
# except ZeroDivisionError:
#     print("на ноль делить нельзя,это математика!")



# try:
#     f = open("myfile.txt")
#     data = f.read()
# except FileNotFoundError:
#     print("файл не найден,проверь имя!")
# else:
#     print("файл прочитан успешно!")
# finally:
#     print("работа с файлом завершина(даже если был провал).")

# age = int(input("сколько тебе лет?"))
# if age < 0:
#     raise ValueError("возраст не может быть отрицательным!")


#task1
# try:
#     a = int(input("введите первое число"))
#     b = int(input("введите второе число"))
#     print(a / b)
# except ValueError:
#     print("пожалуйста ввeдите только числа")
# except ZeroDivisionError:
#      print("на ноль делить нельзя!")

#task2
# try:
#     f = open("diary.txt")
#     data = f.read()
# except FileNotFoundError:
#     print("файл не найден!")

#task3
# try:
#     operation = input("выберите операцию(+, -, *, /):")
#     a = float(input("введите первое число"))
#     b = float(input("введите второе число"))
#     if operation == "+":
#         print(a + b)
#     elif operation == "-":
#         print(a - b)
#     elif operation == "*":
#         print(a * b)
#     elif operation == "/":
#         print(a / b)
#     else:
#         print("Ошибка:неизвестная операция")
# except ZeroDivisionError:
#     print("на ноль делит нельзя")
# except Exception as e:
#     print(f"Ошибка: некорекктный ввод! ")
#task4
# try:
#     with open("arc.txt", "w", encoding="utf-8") as file:
#         file.write("Адилет")
#         print("строка успешно записано!")
# finally:
#     print("работа завершина")

#task5
# try:
#     age = int(input("введите ваш возраст"))
#     if age < 0:
#         raise ValueError("возраст не может быть отрицательным!")
#     print(f"ваш возраст: {age}")
# except ValueError as e:
#     print(f"ошибка, {e}")