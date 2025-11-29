---
tags:
  - harvard
  - datascience
  - python
  - lecture4
  - supplemental_video
university: Harvard
year: "2022"
link: https://cs50.harvard.edu/python/shorts/style/
cover: style.jpg
description: Supplemental video on style using PEP 8.
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
label: "Next: Problem Set - Emojize"
icon: "arrow-right"
hidden: true
class: worksheet-button
tooltip: ""
id: "next"
style: primary
actions:
  - type: open
    link: "[[Emojize]]"

```
```meta-bind-button
label: "Previous: Short - random"
icon: "arrow-left"
hidden: true
class: navigation-buttons
tooltip: ""
id: "previous"
style: primary
actions:
  - type: open
    link: "[[random]]"

```
# Supplemental Video: Style
---

<iframe width="560" height="315" 
src="https://video.cs50.io/nbkWuDrl3UI" 
title="YouTube video player" 
frameborder="0" 
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
allowfullscreen></iframe>
```python
"""
Style: PEP 8 (peps.python.org/pep-0008/)
"""
## SEE students_rs.py script
  
# pylint #style guide checker, but is a bit intense
# pycodestyle #auto reformats your style
# black # opinionated format style
	# run black by typing "black students_rs.py"
	# reformats scripts (can undo but can't redo with control + z)


students = {"Hermione": "Gryffindor", "Harry": "Gryffindor", "Ron": "Gryffindor", "Draco": "Slytherin"}

for student in students:
  print(student)
```


`BUTTON[previous, next]`