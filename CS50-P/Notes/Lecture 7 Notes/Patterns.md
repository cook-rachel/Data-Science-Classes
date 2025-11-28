---
tags:
  - harvard
  - datascience
  - python
  - lecture7
  - supplemental_video
university: Harvard
year: "2022"
link: https://cs50.harvard.edu/python/shorts/patterns/
cover: patterns.jpg
description: Supplemental video on patterns using match and re.search.
---

`BUTTON[cs50p]` `BUTTON[edX-CS50P]`

```meta-bind-button
label: Return to CS50-P
icon: "home"
hidden: true
class: navigation-buttons
tooltip: ""
id: cs50p
style: primary
actions:
  - type: open
    link: "[[CS50-P]]"

```
```meta-bind-button
label: CS50-P Course on edX
icon: "globe"
hidden: true
class: course-navigation-buttons
tooltip: ""
id: "edX-CS50P"
style: primary
actions:
  - type: open
    link: "https://cs50.harvard.edu/python/"

```
```meta-bind-button
label: "Next: Short - Capture Groups"
icon: "arrow-right"
hidden: true
class: worksheet-button
tooltip: ""
id: "next"
style: primary
actions:
  - type: open
    link: "[[Capture Groups]]"

```
```meta-bind-button
label: "Previous: Lecture 7 - Regular Expressions"
icon: "arrow-left"
hidden: true
class: navigation-buttons
tooltip: ""
id: "previous"
style: primary
actions:
  - type: open
    link: "[[Regular Expressions]]"

```
# Supplemental Video: Patterns
---

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


`BUTTON[previous]` `BUTTON[next]`
