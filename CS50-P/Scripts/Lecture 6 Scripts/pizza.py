"""
GOALS:
- implement a program that expects one command-line argument, the name (or path) of a csv file
- outputs a table formatted as ASCII art using tabulate
- format table using grid format
- exit via sys.exit if:
    - if user does not specify eactly one command-line argument
    - file name does not end in .py
    - if file does not exist
"""

from tabulate import tabulate
import sys
import csv

def main():
    if len(sys.argv) < 2:
        sys.exit("ERROR: Missing file pathway.")
    elif len(sys.argv) > 2:
        sys.exit("Too many arguments.")

    file = sys.argv[1]

    try:
        if not file.endswith(".csv"):
            sys.exit("ERROR: Must enter CSV file pathway as argument.")
        else:
            with open(file, "r") as file:
                reader = csv.DictReader(file)
                contents = list(reader)
            
            print(tabulate(contents, headers="keys", tablefmt="grid"))
            
    except FileNotFoundError:
        sys.exit(f"ERROR: '{file}' not found")

main()