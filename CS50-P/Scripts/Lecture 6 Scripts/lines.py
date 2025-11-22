"""
GOALS:
- implement a program that expects exactly one command-line argument, the name or path of a python file
- outputs the number of lines of code in that file
- excluding comments and blank lines
- exit via sys.exit if:
    - if user does not specify exactly one command-line argument
    - if user does not end in .py
    - if files does not exist
- assume any line that starts with # is a comment
"""
import sys

def main():
    if len(sys.argv) < 2:
        sys.exit("ERROR: Missing file pathway.")
    elif len(sys.argv) > 2:
        sys.exit("Too many arguments.")

    file = sys.argv[1]

    try:
        if not file.endswith(".py"):
            sys.exit("ERROR: Must enter python file pathway as argument.")
        else:
            with open(file, "r") as file:
                contents = file.readlines()
                count = 0
                for line in contents:
                    if not line.startswith('\n') and not line.startswith('#'):
                        count += 1

            print(count)
            
    except FileNotFoundError:
        sys.exit(f"ERROR: '{file}' not found")

main()