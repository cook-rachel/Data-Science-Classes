---
tags:
  - harvard
  - datascience
  - python
  - lecture1
  - supplemental_video
university: Harvard
year: "2022"
link: https://cs50.harvard.edu/python/shorts/conditionals/
cover: conditionals_short.jpg
description: A supplemental video on conditionals used in functions.
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
label: "Next: Short - Boolean Expressions"
icon: "arrow-right"
hidden: true
class: worksheet-button
tooltip: ""
id: "next"
style: primary
actions:
  - type: open
    link: "[[Boolean Expressions]]"

```
```meta-bind-button
label: "Previous: Lecture 1 - Conditionals"
icon: "arrow-left"
hidden: true
class: navigation-buttons
tooltip: ""
id: "previous"
style: primary
actions:
  - type: open
    link: "[[Conditionals]]"

```
# Supplemental Video: Conditionals
---
<iframe width="560" height="315" 
src="https://video.cs50.io/vGr1tvjqWs0" 
title="YouTube video player" 
frameborder="0" 
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
allowfullscreen></iframe>


```python
### GOAL: recommend games based on difficulty and number of players

def main():
	difficulty = input("Difficult or Causal? ") 
	players = input("Multiplayer or Single-player? ")
	
	if difficulty == "Difficult":
		if players == "Multiplayer":
			recommend("Poker")
		elif players == "Single-player":
			recommend("Klondike")
		else:
			print("Recommend a valid number of players")
	elif difficulty == "Casual": 
		if players == "Multiplayer":
			recommend("Hearts")
		elif players == "Single-player:
			recommend("Clock")
		else:
			print("Recommend a valid number of players")
	else:
		print("Enter a valid difficulty")




def recommend(game):
	print("You might like", game)

main()
```


`BUTTON[previous]` `BUTTON[next]`
