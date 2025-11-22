"""GOAL:
IPv4 notation: #.#.#.# with each number between 0-255
- implement a function called validate that expects input as string
- return True or False if is IPv4 address or not
- additionally, implement a file called test_numb3rs.pym
    - to test 2 or more functions
    - each function begin with test_
"""

import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    # This regex breaks down each octet:
    # - 25[0-5] matches 250–255
    # - 2[0-4][0-9] matches 200–249
    # - 1[0-9]{2} matches 100–199
    # - [1-9]?[0-9] matches 0–99 (no leading zeros unless it's just "0")
    pattern = r"^(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])" + \
              r"(\.(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])){3}$"
    return re.fullmatch(pattern, ip) is not None


if __name__ == "__main__":
    main()