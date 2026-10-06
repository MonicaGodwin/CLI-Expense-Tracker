import os, sys, csv, datetime

expenses = {
    "id": "Id",
    "item": "Item",
    "amount": "Amount",
    "date": "Date"
}

if not os.path.exists("file.csv"):
    with open("file.csv", "w") as file:
        writer = csv.writer(file)
    
expense = []

command = sys.argv[1].lower()


if command == "add":
    if len(sys.argv) < 4:
        print("Usage: <main.py> <Add> <Item> <amount>")
        sys.exit()
    elif len(sys.argv) > 4:
        print("Too many arguments")
        sys.exit()

    new_item = sys.argv[2]
    item_amount = sys.argv[3]
    item_id = len(expense) + 1
    dated = datetime.date.today()
    new_expense = {
        "id": item_id,
        "item": new_item,
        "amount": item_amount,
        "date": dated
    }
    expense.append(new_expense)
    with open("file.csv", "a") as data:
        writer = csv.DictWriter(
            data,
            fieldnames=["id", "item", "amount", "date"]
        )
        if data.tell() == 0:
            writer.writeheader()
        for row in expense:
            writer.writerow(row)
    print("Expense added successfully")
