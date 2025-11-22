
<iframe width="560" height="315" 
src="https://video.cs50.io/LsW1lL6-ELU" 
title="YouTube video player" 
frameborder="0" 
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
allowfullscreen></iframe>
```python
"""
Capture Groups
"""
import re

locations = {"+1": "Unites State and Canada", "+62": "Indonesia", "+505": "Nicaragua"}

def main():
    pattern = r"(?P<country_code>\+\d{1,3}) \d{3}-\d{3}-\d{4}" #?P<country_code> to name capture group
    number = input("Number: ")

    match = re.search(pattern, number)
    if match:
        country_code = match.group("country_code") #call named capture group here
        print(f"Valid. Country: {locations[country_code]}")
    else:
        print("Invalid")

main()

```