---
tags:
  - harvard
  - datascience
  - python
  - lecture1
  - supplemental_video
university: Harvard
year: "2022"
link: https://cs50.harvard.edu/python/shorts/boolean_expressions/
cover: booleanexpressions.jpg
description: A supplemental video on boolean expressions and how to use them in functions.
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
label: "Next: Problem Set - Deep Thought"
icon: "arrow-right"
hidden: true
class: worksheet-button
tooltip: ""
id: "next"
style: primary
actions:
  - type: open
    link: "[[Deep Thought]]"

```
```meta-bind-button
label: "Previous: Short - Conditionals"
icon: "arrow-left"
hidden: true
class: navigation-buttons
tooltip: ""
id: "previous"
style: primary
actions:
  - type: open
    link: "[[Conditionals (short)]]"

```
# Supplemental Video: Boolean Expressions
---

<iframe width="560" height="315" 
src="https://video.cs50.io/51BNn5Ojupw?start=4" 
title="YouTube video player" 
frameborder="0" 
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
allowfullscreen></iframe>

```python
### GOAL: clean code from Conditionals (short) video
def main():
	difficulty = input("Difficult or Causal? ")
	if not (difficulty == "Difficult" or difficulty == "Casual"):
		print("Enter a valid difficulty")
		return

	players = input("Multiplayer or Single-player? ")
		if not(players == "Multiplayer" or players == "Single-player"):
			print("Enter a valid number of players")
			return
			
	if difficulty == "Difficult" and players == "Multiplayer":
		recommend("Poker")
	elif difficulty == "Difficult" and players == "Single-player":
		recommend("Klondike")
	elif difficulty == "Casual" and players == "Multiplayer":
		recommend("Hearts")
	else:
		recommend("Clock")


def recommend(game):
	print("You might like", game)

main()

```


`BUTTON[previous, next]`