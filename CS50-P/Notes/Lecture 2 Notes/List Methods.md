---
tags:
  - harvard
  - datascience
  - python
  - lecture2
  - supplemental_video
university: Harvard
year: "2022"
link: https://cs50.harvard.edu/python/shorts/list_methods/
cover: listmethods.png
description: Supplemental video on list methods like pop and clear.
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
label: "Next: Short - String Slicing"
icon: "arrow-right"
hidden: true
class: worksheet-button
tooltip: ""
id: "next"
style: primary
actions:
  - type: open
    link: "[[String Slicing]]"

```
```meta-bind-button
label: "Previous: Short - List & Dictionary Comprehensions"
icon: "arrow-left"
hidden: true
class: navigation-buttons
tooltip: ""
id: "previous"
style: primary
actions:
  - type: open
    link: "[[Lists and Dictionary Comprehensions]]"

```
# Supplemental Video: List Methods
---

<iframe width="560" height="315" 
src= "https://video.cs50.io/sBaB1bcOgVE"
title="YouTube video player" 
frameborder="0" 
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
allowfullscreen></iframe>

```python
### POP and CLEAR

def main():
	history = []
	
	while True:
		action = input("Action: ")
		if action == "Undo":
			undone = history.pop() #remove last action
			print(f"Undone: {undone}") #print what we undid
		elif action == "Restart":
			history.clear() #clear all actions
			print(f"Game restarted!")
		else:
			history.append(action)
		print(history)

main()
```


`BUTTON[previous]` `BUTTON[next]`


