import random
from datetime import datetime

tickets = {}

while True:
    print("1. Выдача талона")
    print("2. Сдача талона")
    print("3. Выход")

    choice = input("Ваш выбор: ")

    if choice == "1":
        car_number = input("Введите номер машины: ")

        if not car_number.isalnum():
            print("Ошибка: Неверный формат номера машины")
            continue
        if not car_number.isdigit():
            print("Ошибка: Неверный формат номера машины")
            continue

        ticket_number = random.randint(100000, 999999)

        tickets[ticket_number] = {"car": car_number,"time": datetime.now()}

        print("\nТалон выдан:")
        print("Номер талона:", ticket_number)
        print("Номер машины:", car_number)
        print("Время выдачи:", tickets[ticket_number]["time"])

    elif choice == "2":
        try:
            ticket = int(input("Введите номер талона: "))
            if ticket not in tickets:
                print("Талон не найден!")
                continue

            entry_time = tickets[ticket]["time"]
            exit_time = datetime.now()

            seconds = (exit_time - entry_time).total_seconds()
            hours = int(seconds // 3600)

            if hours < 1:
                price = 100
            else:
                price = 100 + hours * 50

            print("\nсчет к оплате:")
            print("номер талона:", ticket_number)
            print("Машина:", tickets[ticket]["car"])
            print("Время въезда:", entry_time)
            print("Время выезда:", exit_time)
            print("Стоимость:", price, "сом")

            del tickets[ticket]
        except ValueError:
            print("введите номер талона только цифрами!")


    elif choice == "3":
        print("программа завершина")
        break

    else:
        print("неверный выбор")

