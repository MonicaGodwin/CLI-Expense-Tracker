import os, csv, sys, datetime

expenses_field = {
    "id": "Id",
    "item": "Item",
    "amount": "Amount",
    "date": "Date",
    "category": "Category"
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
    if new_item:
        option = input(
            f"\n=== SELECT CATEGORY TO ADD ITEM TO ===\n\n"
            f"1. Food\n"
            f"2. Clothing\n"
            f"3. Utilities\n\n"
        )   
        category = ""
        if option == "1":
            category = "Food"
        elif option == "2":
            category = "Clothing"
        elif option == "3":
            category = "Utilities"
        else:
            print("please select a category to add item")
            
            
    item_id = len(expenses) + 1
    dated = datetime.date.today()
    new_expense = {
        "id": item_id,
        "item": new_item,
        "amount": item_amount,
        "date": dated,
        "category": category
    }
    expenses.append(new_expense)
    with open("file.csv", "a") as data:
        writer = csv.DictWriter(
            data,
            fieldnames=["id", "item", "amount", "date", "category"]
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


def delete_expenses():
    if len(sys.argv) < 3:
        print("USage:<main.py> <delete> <id>") 
        sys.exit()
    elif len(sys.argv) > 3:
        print("Too many arguments")
        sys.exit()
    deleted = False
    item_id = sys.argv[2]
    for expense in expenses:
        if expense["id"] == item_id:
            expenses.remove(expense)
            deleted = True
            print("Expense deleted")
    if deleted:
        for number, exp in enumerate(expenses, start=1):
            exp["id"] = number
        with open("file.csv", "w") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=["id", "item", "amount", "date"]
            )
            writer.writeheader()
            for rows in expenses:
                writer.writerow(rows)
    else:
        print("Item id not found")

def view_all_expenses():
    if len(sys.argv) < 2:
        print("Usage: <main.py> <view>")
        sys.exit()
    if len(sys.argv) > 2:
        print("Too many arguments")
        sys.exit()
    if len(expense) == 0:
        print("No expenses to display")
    for expense in expenses:
        print(
            f"{expense["id"]} - {expense["item"]} - {expense["amount"]} - {expense["date"]}"
        )

def total_expenses():
    if len(sys.argv) < 2:
        print("Usage: <main.py> <summary>")
        sys.exit()
    elif len(sys.argv) > 2:
        print("Too many arguments")
        sys.exit()
    total_amount = 0
    for expense in expenses:
        amount = expense["amount"]
        num = int(amount)
        total_amount += num
    print(
        f"Total expenses: ₦{total_amount}"
        )

def view_category():
    if len(sys.argv) < 3:
        print("Usage: <main.py> <category> <month>")
        sys.exit()
    elif len(sys.argv) > 3:
        print("Too many arguments") 
        sys.exit()
    category = sys.argv[2]
    total_amount = 0
    for expense in expenses:
        if expense["date"] == category:
            num = int(expense)
            total_amount += num
    print(
        f"Total expenses for {category}: {total_amount}"
    )
