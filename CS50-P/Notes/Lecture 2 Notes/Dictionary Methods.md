---
tags:
  - harvard
  - datascience
  - python
  - lecture2
  - supplemental_video
university: Harvard
year: "2022"
link: https://cs50.harvard.edu/python/shorts/dictionary_methods/
cover: dictionarymethods.jpg
description: Supplemental video on dictionary methods, including using keys, pop, clear, and items.
---

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
label: "Next: Short - For Loops"
icon: "arrow-right"
hidden: true
class: worksheet-button
tooltip: ""
id: "next"
style: primary
actions:
  - type: open
    link: "[[For Loops]]"

```
```meta-bind-button
label: "Previous: Short - Dictionaries"
icon: "arrow-left"
hidden: true
class: navigation-buttons
tooltip: ""
id: "previous"
style: primary
actions:
  - type: open
    link: "[[Dictionaries]]"

```
# Supplemental Video: Dictionary Methods
---

<iframe width="560" height="315" 
src="https://video.cs50.io/3zJoCpvKhx4" 
title="YouTube video player" 
frameborder="0" 
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
allowfullscreen></iframe>

```python
### USING KEYS and POP and CLEAR
WORDS = {"PAIR": 4, "HAIR": 4, "CHAIR": 5, "GRAPHIC": 7}

def main():
	print("Welcome to Spelling Bee!")
	print("Your letters are: A I P C R H G")

	while len(WORDS) > 0:
		print(f"{len(WORDS)} words left!")
		guess = input("Guess a word: ")

		#TO DO: Check if guess in dictionary
		#TO DO: end game early if guess GRAPHIC
		if guess == "GRAPHIC":
			WORDS.clear()
			print("You've won!")
		if guess in WORDS.keys():
			points = WORDS.pop(guess) #to remove word from key
			print(f"Good job! You scored {points} points.")


print("That's the game!")

main()

```

``` python
## USING ITEMS
WORDS = {"PAIR": 4, "HAIR": 4, "CHAIR": 5, "GRAPHIC": 7}

def main():
	print("Welcome to Spelling Bee!")
	for word, points in WORDS.items(): #can also use key, value
		print(f"{word} was worth {points} points.")

main()
```


`BUTTON[previous]` `BUTTON[next]`
