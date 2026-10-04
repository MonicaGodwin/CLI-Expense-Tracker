import os
import sys
import csv
import time

expenses = {
    "id": "Id",
    "item": "Item",
    "amount": "Amount",
    "date": "Date"
}

if not os.path.exists("file.csv"):
    expense = []
    with open("file.csv", "w") as file:
        writer = csv.writer(file)

if len(sys.argv) < 2:
    print("Usage: <main.py> add|update|delete|View")
    sys.exit()
elif len(sys.argv) > 2:
    print("Too many arguments")
    sys.exit()

command = sys.argv[1].lower()


if command == "Add":
    if len(sys.argv) < 3:
        print("Usage: <main.py> <Add> <Item> <amount>")
        sys.exit()
    elif len(sys.argv) > 3:
        print("Too many arguments")
        sys.exist()

    new_item = sys.argv[2]
    item_amount = sys.argv[3]
    item_id = len(expense) + 1
    dated = time.ctime
    new_expense = {
        "id": item_id,
        "item": new_item,
        "amount": item_amount,
        "date": dated
    }
    expense.append(new_expense)
    with open("file.csv", "w") as data:
        writer = csv.DictWriter(
            data,
            fieldnames=["id", "item", "amount", "date"]
        )
        writer.writeheader()
        writer.writerow(new_expense)
    print("Expense added successfully")
