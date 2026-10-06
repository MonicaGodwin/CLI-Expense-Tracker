import os, csv, sys, datetime

expenses_field = {
    "id": "Id",
    "item": "Item",
    "amount": "Amount",
    "date": "Date"
}


if not os.path.exists("file.csv"):
    with open("file.csv", "w") as file:
        writer = csv.writer(file)

def load_expenses():
    expenses = []
    if os.path.exists("file.csv"):
        with open("file.csv", "r") as data:
            reader = csv.DictReader(data)
            for rows in reader:
                expenses.append(rows)
    return expenses

expenses = load_expenses()

def add_expenses():
    if len(sys.argv) < 4:
        print("Usage: <main.py> <Add> <Item> <amount>")
        sys.exit()
    elif len(sys.argv) > 4:
        print("Too many arguments")
        sys.exit()

    new_item = sys.argv[2]
    item_amount = sys.argv[3]
    item_id = len(expenses) + 1
    dated = datetime.date.today()
    new_expense = {
        "id": item_id,
        "item": new_item,
        "amount": item_amount,
        "date": dated
    }
    expenses.append(new_expense)
    with open("file.csv", "a") as data:
        writer = csv.DictWriter(
            data,
            fieldnames=["id", "item", "amount", "date"]
        )
        if data.tell() == 0:
            writer.writeheader()
        # for row in new_expense:
        writer.writerow(new_expense)
    print("Expense added successfully")


def update_expenses():
    if len(sys.argv) < 5:
        print("Usage: <main.py> <update> <id> <item> <amount>")
        sys.exit()
    elif len(sys.argv) > 5:
        print("Too many argument")
        sys.exit()
    update = False
    item_id = sys.argv[2]
    item = sys.argv[3]
    item_amount = sys.argv[4]
    dated = datetime.date.today()
    for expense in expenses:
        if expense["id"] == item_id:
            expense["item"] = item
            expense["amount"] = item_amount
            expense["date"] = dated
            update = True
            print("expense updated")
    if update:
        with open("file.csv", "w") as updated_file:
            writer = csv.DictWriter(
                updated_file,
                fieldnames=["id", "item", "amount", "date"]
            )
            writer.writeheader()
            for row in expenses:
                writer.writerow(row)
    else:
        print("expense id not found")
