import os
import sys

if not os.path.exists("file.csv"):
    task = []

if len(sys.argv) < 2:
    print("Usage: <main.py> add|update|delete|View")
    sys.exit()

command = sys.argv[1].lower()

if command == "Add":
    if len(sys.argv) < 3:
        print("Usage: <main.py> <Add> <Item> <amount>")
        sys.exit()
    