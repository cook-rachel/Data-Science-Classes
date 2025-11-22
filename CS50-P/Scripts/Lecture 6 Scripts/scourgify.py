"""
GOALS:
- implement a program that expects user to provide two command-line arguments
    - the name of csv file to input with two columns: name, house
     - the name of a new csv file to write as output, with columns: first, last, house
- convert that input to that output, splitting each name into first and last
- if user does not list two command line arguments or if first cannot be read, exit via sys.exit
"""

import csv
import sys

def main():
    if len(sys.argv) < 3:
        sys.exit("ERROR: Missing pathway for output.")
    elif len(sys.argv) > 3:
        sys.exit("ERROR: Too many arguments")
    
    inputfile = sys.argv[1]
    outputfile = sys.argv[2]

    updated_contents = []

    try:
        with open(inputfile, "r") as before, open(outputfile, "w") as after:
                reader = csv.DictReader(before)
                writer = csv.DictWriter(after, fieldnames = ["first", "last", "house"])
                writer.writeheader()
                for row in reader:        
                    last, first = row["name"].strip().split(",")
                    row["first"] = first
                    row["last"] = last
                    house = row["house"]

                    # updated_contents.append({"first": first, "last": last, "house": house}) #don't need unless using these columns in program
                    writer.writerow({"first": first, "last": last, "house": house})
    
    except FileNotFoundError:
        sys.exit("ERROR: File not found")

main()