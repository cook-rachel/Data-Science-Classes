"""
RE
"""
# import re

# email = input("What's your email? ").strip()

# username, domain = email.split("@")

# if re.search(".+@.+", email): # .+ means multiple at beginning of @ and after
#     print("Valid")
# else:
#     print("Invalid")

# if re.search(r".+@.+\.edu", email): #\. means . as character (vs pattern syntax)
#     print("Valid")
# else:
#     print("Invalid")

# if re.search(r"^.+@.+\.edu$", email): #^ means start of string, $ means end of string
#     print("Valid")
# else:
#     print("Invalid")

# if re.search(r"^[^@]+@[^@]+\.edu$", email): #instead of dot, [^@]+@[^@] means any char except @, then @, then any char except @, then finally .edu, end of string
#     print("Valid")
# else:
#     print("Invalid")

# if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email): #instead of excluding @, can specify what to use
#     print("Valid")
# else:
#     print("Invalid")

"""
Case Sensitivity
"""

# if re.search(r"^\w+@\w+\.(com|edu|gov|net|org)$", email, re.IGNORECASE): #flags can also be added to account for case sensitivity
#     print("Valid")
# else:
#     print("Invalid")


# if re.search(r"^\w+@(\w+\.)?\w+\.(com|edu|gov|org)$", email, re.IGNORECASE): #(\w+\.)? means subdomain is optional (? makes it optional)
#     print("Valid")
# else:
#     print("Invalid")

#to account for everything
# if re.search(r"^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$", email, re.IGNORECASE): 
#     print("Valid")
# else:
#     print("Invalid")

"""
Cleaning up user input
"""
# name = input("What's your name? ").strip()
# if "," in name:
#     last,first = name.split(", ")
#     name = f"{first} {last}"
# print(f"hello, {name}")

import re

# name = input("What's your name? ").strip()
# matches = re.search(r"^(.+), (.+)$", name) # accounts for space or not between comma; parentheses will capture group so can save as sections because set to variable on left
# if matches:
#     last, first = matches.groups() #two variables to assign because 2 sets of parentheses
#     name = first + " " + last
# print(f"hello, {name}")

# name = input("What's your name? ").strip()
# matches = re.search(r"^(.+), (.+)$", name) 
# if matches:
#     last = matches.group(1) #can also break down into groups
#     first = matches.group(2)
#     name = f"{first} {last}"  
# print(f"hello, {name}")

# name = input("What's your name? ").strip()
# matches = re.search(r"^(.+), (.+)$", name)  
# if matches:
#     name = matches.group(2) + " " + matches.group(1) #can simplfy further
# print(f"hello, {name}")

# name = input("What's your name? ").strip()
# matches = re.search(r"^(.+), *(.+)$", name)  #add * to account for potential additional spaces
# if matches:
#     name = matches.group(2) + " " + matches.group(1) 
# print(f"hello, {name}")

# name = input("What's your name? ").strip()
# if matches := re.search(r"^(.+), *(.+)$", name):  #:= walrus operator allows us to ask a boolean question (if this then go to next time)
#     name = matches.group(2) + " " + matches.group(1) 
# print(f"hello, {name}")

"""
Extracting user input
"""
# url = input("URL: ").strip()
# username = url.replace("https://twitter.com/", "") #can replace with ""
# print(f"Username: {username}")

# url = input("URL: ").strip()
# username = url.removeprefix("https://twitter.com/") #can remove it this way
# print(f"Username: {username}")

# import re

# url = input("URL: ").strip()
# username = re.sub(r"https://twitter.com/", "", url)  #use re to substitute
# print(f"Username: {username}")

# import re

# url = input("URL: ").strip()
# username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url) #use regular patterns
# print(f"Username: {username}")

#(https?://)? means optional https://, optional http://
#(www\.)? means optional www.
#twitter\.com/ means twitter.com required for substitute (\. not . as to mean any char)
#don't need $ at end because we want to parse out ending as username

# import re

# url = input("URL: ").strip()
# matches = re.search(r"^https?://(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE) #change to search, now add capture for username, end with $, add flag
# if matches:
#         print(f"Username:", matches.group(2)) #add if statement so can look for match, otherwise print input as is - must be group 2 b/c www is group 1

# import re

# url = input("URL: ").strip()
# matches = re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE) #add ?: before www to ignore capture; do same for https:// to make optional
# if matches:
#         print(f"Username:", matches.group(1)) #change to group 1

# import re

# url = input("URL: ").strip()
# if matches := re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE): #be specific on what username chars are allowed through twitter, update to walrus for efficiency 
#     print(f"Username:", matches.group(1)) 


"""
Patterns Shorts
"""
## Hexcadecimal code for color: RRGGBB
## Hexadecimal codes can have A-F and 0-9 (case insensitive)
## must be 6 characters

# import re

# def main():
#     code = input("Hexadecimal color code: ").strip()
    
#     pattern = r"^#[a-f0-9]{6}$" #set 6 to count how many times [] should be included
#     match = re.search(pattern, code, re.IGNORECASE)
#     if match:
#         print(f"Valid. Matched with {match.group()}")
#     else:
#         print("Invalid.")

# main()


"""
Capture Groups
"""
# import re

# locations = {"+1": "Unites State and Canada", "+62": "Indonesia", "+505": "Nicaragua"}

# def main():
#     pattern = r"(?P<country_code>\+\d{1,3}) \d{3}-\d{3}-\d{4}" #?P<country_code> to name capture group
#     number = input("Number: ")

#     match = re.search(pattern, number)
#     if match:
#         country_code = match.group("country_code") #call named capture group here
#         print(f"Valid. Country: {locations[country_code]}")
#     else:
#         print("Invalid")

# main()
