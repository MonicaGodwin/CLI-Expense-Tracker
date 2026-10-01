import os
import sys

if not os.path.exists("file.csv"):
    task = []

if len(sys.argv) < 2:
    print("Usage: <main.py> add|update|delete|View")
    sys.exit()

