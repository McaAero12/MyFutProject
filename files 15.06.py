# file = open("notes.tst", "r")
# content = file.read()
# print(content)
# file.close()  #"r" - читает
#
# with open("notes.tst", "r") as file:
#     for line in file:
#         print(line.strip()) #strip - убирает лишние пробелы
#


# with open("notes.tst", "r") as file:
#     lines = file.readlines()
#     print(lines[:3])


# file = open("notes.tst", "w")
# file.write("hello",)
# file.close()       # "W" = перезаписывает готовый файл!
#
#
# with open("notes.tst", "a") as file:
#     file.write(" Adilet")     #"a"- ДОБАВЛЯЕТ НОВЫЙ ЭЛЕМЕНТ!

# lines = ["string1\n", "string2\n", "string3\n"]
# with open("notes.tst", "w") as file:
#     file.writelines(lines)


# def save_history(history, filename = "history.txt"):
#     with open(filename, "w") as file:
#         for record in history:
#             file.write(record + "\n")
#                                                         # добваление элементов в истории
#
# story = ["first", "second", "third", "fourth"]
# save_history(story, "history.txt")


#TASK1
# with open("myfile.txt", "r", encoding="utf-8") as file:
#     content = file.read()
#     print(content)

#task2
# with open("output.txt", "w", encoding="utf-8") as file:
#     for i in range (1, 4):
#         line = input(f"введите строку {i}")
#         file.write(line + "\n")

#task3
# with open("todo.txt", "w", encoding="utf-8") as file:
#     while True:
#         task = input("Добавьте задачу(или 'стоп' для выхода):")
#         if task == 'стоп':
#             break
#         file.write(task + "\n")
#
# print(f"ваши задачи:")
# with open("todo.txt", "r", encoding="utf-8") as file:
#     for line in file:
#         print(line.strip())
#
# task4
# with open("source.txt", "r", encoding="utf-8") as file:
#     content = file.read()
#
# with open("copy.txt", "w", encoding="utf-8") as file:  #скопировать из одного в другой
#     file.write(content)



# # #task5
with open("data.txt", "r", encoding="utf-8") as file:
    content = file.read()

with open("data.upper.txt", "w", encoding="utf-8") as file_upper:
    file_upper.write(content.upper())
