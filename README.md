# CLI Expense Tracker

## About the Project

CLI Expense Tracker is a simple Python command-line application that helps users record and manage their daily expenses.

The application stores expense records in a CSV file, allowing users to add, update, delete, and view expenses without using a database.

## Features

* **Add Expenses:** Record an item, its amount, category, and date.
* **Update Expenses:** Edit an existing expense using its ID.
* **Delete Expenses:** Remove an expense using its ID.
* **View Expenses:** Display all recorded expenses.
* **Expense Summary:** Calculate the total amount spent.
* **Category Filter:** View expenses by category.
* **Monthly Filter:** View expenses for a specific month.
* **Budget Tracking:** Set a budget and receive warnings when spending approaches or exceeds the limit.

## Technologies Used

* Python 3
* CSV module for storing expense records
* `sys` module for handling command-line arguments
* `datetime` module for recording expense dates
* `os` module for checking whether files exist

## Project Structure

```text
CLI-Expense-Tracker/
├── main.py
├── function.py
├── file.csv
└── README.md
```

* `main.py`: Handles commands entered by the user.
* `function.py`: Contains the functions used to manage expenses.
* `file.csv`: Stores expense records.
* `README.md`: Contains project documentation.

The CSV file is created automatically if it does not exist, provided your code includes the file-initialization logic.

## Requirements

* Python 3 installed on your computer.
* A terminal or command-line interface.

No external Python packages are required.

## How to Run the Project

**1. Clone the repository** :

```bash
git clone <https://github.com/MonicaGodwin/CLI-Expense-Tracker.git>
```

**2. Enter the project directory:**

```bash
cd CLI-Expense-Tracker
```

**3. Run a command:**

Use the commands below to manage your expenses.

## Available Commands

### 1. Add an Expense

```bash
python3 main.py add Rice 5000
```

The application asks you to select a category and then saves the expense.

Available categories:

* Food
* Clothing
* Utilities

### 2. Update an Expense

```bash
python3 main.py update 1 Rice 6000
```

Updates the expense with ID `1`, changing its item name and amount. Your function also asks you to select a category.

### 3. Delete an Expense

```bash
python3 main.py delete 1
```

Deletes the expense with ID `1`.

### 4. View All Expenses

```bash
python3 main.py view
```

Displays all recorded expenses.

### 5. View Expense Summary

```bash
python3 main.py summary
```

Displays the total amount spent across all recorded expenses.

### 6. View Expenses by Category

```bash
python3 main.py category food
```

Displays expenses belonging to the selected category and calculates their total.

Example categories: `food`, `clothing`, `utilities`.

### 7. View Expenses by Month

```bash
python3 main.py month 10
```

Displays expenses recorded in October. Use month numbers from `01` to `12`.

### 8. Set a Budget

```bash
python3 main.py budget 50000
```

Compares your recorded expenses against a budget of ₦50,000 and displays the percentage spent.

The application warns you when spending reaches 80% of the budget or exceeds the limit.

## Data Storage

Expense records are stored in `file.csv`. Each record contains:

* `id`: Unique expense identifier
* `item`: Name of the expense
* `amount`: Amount spent
* `category`: Expense category
* `date`: Date the expense was recorded or last updated

The CSV file allows expense records to remain available between program executions.

## What I Learned

Building this project helped me practise:

* Python functions and conditional statements
* Lists and dictionaries
* Reading and writing CSV files
* Command-line arguments using `sys.argv`
* Exception handling with `try` and `except`
* Working with dates using `datetime`
* File handling and basic data validation
* Breaking a program into separate Python modules

## Author

**Monica Godwin**

This project was built as part of my Python programming journey to improve my problem-solving skills and practical experience with file handling and command-line applications.
