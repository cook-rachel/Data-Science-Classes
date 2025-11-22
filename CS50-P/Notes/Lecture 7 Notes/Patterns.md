
<iframe width="560" height="315" 
src="https://video.cs50.io/h_kGwBANynQ" 
title="YouTube video player" 
frameborder="0" 
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
allowfullscreen></iframe>

```python
"""
Patterns Shorts
"""
## Hexcadecimal code for color: RRGGBB
## Hexadecimal codes can have A-F and 0-9 (case insensitive)
## must be 6 characters

import re

def main():
    code = input("Hexadecimal color code: ").strip()
    
    pattern = r"^#[a-f0-9]{6}$" #set 6 to count how many times [] should be included
    match = re.search(pattern, code, re.IGNORECASE)
    if match:
        print(f"Valid. Matched with {match.group()}")
    else:
        print("Invalid.")

main()

```