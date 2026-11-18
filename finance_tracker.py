import csv
import os
from datetime import datetime

income = 0
expense = 0

def create_csv_file():

    if not os.path.exists("transactions.csv"):

        with open("transactions.csv", "w", newline="", encoding="utf-8") as file:

            writer = csv.writer(file)

            writer.writerow([
                "Date",
                "Type",
                "Category",
                "Amount"
            ])

        writer = csv.writer(file)

        writer.writerow([
            "Date",
            "Type",
            "Category",
            "Amount"
        ])

def save_transaction(transaction_type, category, amount):
    current_date = datetime.now().strftime("%Y-%m-%d")

    with open("transactions.csv", "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow([
            current_date,
            transaction_type,
            category,
            amount
        ])


def add_income():
    global income

    print("\nКатегории:")
    print("1. Salary")
    print("2. Bonus")
    print("3. Freelance")
    print("4. Other")

    category_choice = input("Избери категория: ")

    categories = {
        "1": "Salary",
        "2": "Bonus",
        "3": "Freelance",
        "4": "Other"
    }

    category = categories.get(category_choice, "Other")

    amount = float(input("Въведи приход: "))

    income += amount

    save_transaction("Income", category, amount)

    print("Приходът е добавен!")


def add_expense():
    global expense

    print("\nКатегории:")
    print("1. Food")
    print("2. Transport")
    print("3. Bills")
    print("4. Entertainment")
    print("5. Other")

    category_choice = input("Избери категория: ")

    categories = {
        "1": "Food",
        "2": "Transport",
        "3": "Bills",
        "4": "Entertainment",
        "5": "Other"
    }

    category = categories.get(category_choice, "Other")

    amount = float(input("Въведи разход: "))

    expense += amount

    save_transaction("Expense", category, amount)

    print("Разходът е добавен!")


def show_balance():
    savings = income - expense

    print("\n=== Финансов отчет ===")
    print(f"Общо приходи: {income:.2f} лв.")
    print(f"Общо разходи: {expense:.2f} лв.")
    print(f"Спестявания: {savings:.2f} лв.")

def show_transactions():

    print("\n=== Всички транзакции ===")

    try:
        with open("transactions.csv", "r", encoding="utf-8") as file:

            for line in file:
                print(line.strip())

    except FileNotFoundError:
        print("Няма намерени транзакции.")


def financial_report():

    print("\n=== Финансов отчет ===")

    total_income = income
    total_expense = expense

    print(f"Общо приходи: {total_income:.2f} лв.")
    print(f"Общо разходи: {total_expense:.2f} лв.")
    print(f"Баланс: {(total_income - total_expense):.2f} лв.")

def category_statistics():
        print("\n=== Статистика по категории ===")

        categories = {}

        try:
            with open("transactions.csv", "r", encoding="utf-8") as file:

                next(file)  # пропуска заглавния ред

                for line in file:

                    data = line.strip().split(",")

                    if len(data) == 4:

                        category = data[2]
                        amount = float(data[3])

                        if category in categories:
                            categories[category] += amount
                        else:
                            categories[category] = amount

            for category, amount in categories.items():
                print(f"{category}: {amount:.2f} лв.")

        except FileNotFoundError:
            print("Няма намерени данни.")

create_csv_file()

while True:
    print("\n=== Personal Finance Tracker ===")
    print("1. Добави приход")
    print("2. Добави разход")
    print("3. Покажи баланс")
    print("4. Покажи транзакции")
    print("5. Финансов отчет")
    print("6. Статистика по категории")
    print("7. Изход")

    choice = input("Избери опция: ")

    if choice == "1":
        add_income()

    elif choice == "2":
        add_expense()

    elif choice == "3":
        show_balance()

    elif choice == "4":
          show_transactions()


    elif choice == "5":

        financial_report()



    elif choice == "6":

        category_statistics()


    elif choice == "7":

        print("До скоро!")

        break

    else:
        print(" Невалиден избор!")