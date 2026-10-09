import function as func
import sys
    
command = sys.argv[1].lower()
expenses = []
if len(sys.argv) < 2:
    print("Usage: <main.py> <add|update|delete|view|summary|category|month>")
    sys.exit()

if command == "add":
    func.add_expenses()
        
elif command == "update":
    func.update_expenses()

elif command == "delete":
    func.delete_expenses()

elif command == "view":
    func.view_all_expenses()

elif command == "summary":
    func.total_expenses()

elif command == "category":
    func.view_category()

elif command == "month":
    func.view_month()

elif command == "budget":
    func.set_budget()
elif command == "exit":
    sys.exit()
else:
    print(f"Unknown command: {command}")
   