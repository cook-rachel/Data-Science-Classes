---
tags:
  - harvard
  - datascience
  - python
  - lecture7
  - supplemental_video
university: Harvard
year: "2022"
link: https://cs50.harvard.edu/python/shorts/capture_groups/
cover: capturegroups.jpg
description: Supplemental video on capture groups via re and match.
---

`BUTTON[cs50p, edX-CS50P]`

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
label: "Next: Problem Set - NUMB3RS"
icon: "arrow-right"
hidden: true
class: worksheet-button
tooltip: ""
id: "next"
style: primary
actions:
  - type: open
    link: "[[NUMB3RS]]"

```
```meta-bind-button
label: "Previous: Short - Patterns"
icon: "arrow-left"
hidden: true
class: navigation-buttons
tooltip: ""
id: "previous"
style: primary
actions:
  - type: open
    link: "[[Patterns]]"

```
# Supplemental Video: Capture Groups
---

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


`BUTTON[previous, next]`
