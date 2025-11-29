---
tags:
  - harvard
  - datascience
  - python
  - lecture0
  - supplemental_video
university: Harvard
year: "2022"
link: https://cs50.harvard.edu/python/shorts/variables/
cover: variables.jpg
description: Supplemental video on variable types like int, str, etc.
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
label: "Next: Short - Return Values"
icon: "arrow-right"
hidden: true
class: worksheet-button
tooltip: ""
id: "next"
style: primary
actions:
  - type: open
    link: "[[Return Values]]"

```
```meta-bind-button
label: "Previous: Short - Functions"
icon: "arrow-left"
hidden: true
class: navigation-buttons
tooltip: ""
id: "previous"
style: primary
actions:
  - type: open
    link: "[[Functions]]"

```
# Supplemental Video: Variables
---

<iframe width="560" height="315" 
src="https://video.cs50.io/MyWf3zyyvjc" 
title="YouTube video player" 
frameborder="0" 
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
allowfullscreen></iframe>

### Variable types
- when using `input("Enter a guess: ")`, this grabs a string. Need int in front if you want an integer
```python
def get_guess():
	guess = int(input("Enter a guess: "))
	return guess

def main():
	guess = get_guess() # not referring to same guess as above
	if guess == 50:
		print("Correct!")
	else:
		print("Incorrect!")
	print(guess)

main()
	
```


`BUTTON[previous, next]`