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
    try:
        new_item = str(sys.argv[2])
        item_amount = int(sys.argv[3])
    except ValueError:
        print("Invalid input: item must be a string and amount should be an integer")
        sys.exit()
    if new_item:
        option = input(
            f"\n=== SELECT CATEGORY TO ADD ITEM TO ===\n\n"
            f"Select option(1-3)\n"
            f"1. Food\n"
            f"2. Clothing\n"
            f"3. Utilities\n\n"
        )   
        category = ""
        if option == "1":
            category = "food"
        elif option == "2":
            category = "clothing"
        elif option == "3":
            category = "utilities"
        else:
            print("please select a category to add item")
            sys.exit()
            
    item_id = len(expenses) + 1
    dated = datetime.date.today()
    new_expense = {
        "id": item_id,
        "item": new_item,
        "amount": item_amount,
        "category": category,
        "date": dated
    }
    expenses.append(new_expense)
    with open("file.csv", "a") as data:
        writer = csv.DictWriter(
            data,
            fieldnames=["id", "item", "amount", "category", "date"]
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
    try:
        item = str(sys.argv[3])
        item_amount = int(sys.argv[4])
    except ValueError:
        print("Invalid input: item must be a string and amount should be an integer")
        sys.exit()
    if item:
        option = input(
            f"\n=== SELECT CATEGORY TO UPDATE ITEM ===\n\n"
            f"Select option(1-3)\n"
            f"1. Food\n"
            f"2. Clothing\n"
            f"3. Utilities\n\n"           
        )
    category = ""
    if option == "1":
        category = "food"
    elif option == "2":
        category = "clothing"
    elif option == "3":
        category = "utilities"
    else:
        print("please select a category to add item")
        sys.exit()
    dated = datetime.date.today()
    for expense in expenses:
        if expense["id"] == item_id:
            expense["item"] = item
            expense["amount"] = item_amount
            expense["category"] = category
            expense["date"] = dated
            update = True
            print("expense updated")
    if update:
        with open("file.csv", "w") as updated_file:
            writer = csv.DictWriter(
                updated_file,
                fieldnames=["id", "item", "amount", "category", "date"]
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
                fieldnames=["id", "item", "amount", "category", "date"]
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
    if len(expenses) == 0:
        print("No expenses to display")
    for expense in expenses:
        print(
            f"{expense['id']} - {expense['item']} - {expense['amount']} - {expense['category']} - {expense['date']}"
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
        print("Usage: <main.py> <category> <food|clothing|utilities>")
        sys.exit()
    elif len(sys.argv) > 3:
        print("Too many arguments") 
        sys.exit()
    category = sys.argv[2]
    found = False
    total_amount = 0
    for expense in expenses:
        if expense["category"].lower() == category.lower():
            found = True
            print(f"{expense['id']}-{expense['item']}-{expense['amount']}-{expense['category']}-{expense['date']}")
            amount = expense["amount"]
            num = int(amount)
            total_amount += num
    if not found:
        print(f"No expenses record for {category}")
        sys.exit()
    print(
        f"Total expenses for {category} category: {total_amount}"
    )

def view_month():
    if len(sys.argv) < 3:
        print("Usage: <main.py> <month> <month_num>")
        sys.exit()
    elif len(sys.argv) > 3:
        print("Too many arguments") 
        sys.exit()
    total = 0
    found = False
    for expense in expenses:
        dated = expense["date"]
        splitted = dated.split("-")
        month_num = splitted[1]
        if sys.argv[2] == month_num:
            print(f"{expense['id']}-{expense['item']}-{expense['amount']}-{expense['date']}-{expense['category']}")
            amount = expense["amount"]
            num = int(amount)
            total += num
            found = True
    if not found:
        print("Month not found in expense")
        sys.exit()
    print(
        f"\nTotal expenses for month {month_num}: {total}"
    )

def set_budget():
    if len(sys.argv) < 3:
        print("Usage: <main.py> <budget> <budget_amount>")
        sys.exit()
    elif len(sys.argv) > 3:
        print("Too many arguments") 
        sys.exit()
    try:
        budget = int(sys.argv[2])
    except ValueError:
        print("Must be an integer")
        sys.exit()
    if budget <= 0:
        print("Budget should be greater than zero")
        return
    total = 0
    for expense in expenses:
        try:
            amount = int(expense["amount"])
            total += amount
        except ValueError:
            print("Must be an integer")
    percentage = (total / budget) * 100
    print(
        f"Total expenses: ₦{total}\n"
        f"Budget: ₦{budget}\n"
        f"Budget used: {percentage:.0f}%"
    )

    if total > budget:
        print("You have exceeded your budget")
    elif percentage >= 80:
        print(f"Warning: You've spent {percentage:.0f}% of your budget")
    else:
        print("Still within the budget")

        