import function as func
import sys
    
expenses = []

command = sys.argv[1].lower()

if command == "add":
    func.add_expenses()
elif command == "update":
    func.update_expenses()

