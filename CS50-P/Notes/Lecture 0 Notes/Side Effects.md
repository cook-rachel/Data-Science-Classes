---
tags:
  - harvard
  - datascience
  - python
  - lecture0
  - supplemental_video
university: Harvard
year: "2022"
link: https://cs50.harvard.edu/python/shorts/side_effects/
cover: sideeffects.jpg
description: Supplemental video on side effects, which are things that get changed while a function is running but are NOT return values.
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
label: "Next: Short - String Methods"
icon: "arrow-right"
hidden: true
class: worksheet-button
tooltip: ""
id: "next"
style: primary
actions:
  - type: open
    link: "[[String Methods]]"

```
```meta-bind-button
label: "Previous: Short - Return Values"
icon: "arrow-left"
hidden: true
class: navigation-buttons
tooltip: ""
id: "previous"
style: primary
actions:
  - type: open
    link: "[[Return Values]]"

```
# Supplemental Video: Side Effects
---

<iframe width="560" height="315" 
src="https://video.cs50.io/a002hwAqLDw" 
title="YouTube video player" 
frameborder="0" 
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
allowfullscreen></iframe>
- *side effects* are not the return value, but anything that gets changed while function is running
	- ex) printing to terminal
	- ex) change emotional state as side effect by **modifying** using global
- *global variable*  = emoticon because at top
	- it is **accessible** but not **modifiable** unless call global in function
- *local variable* = phase because stuck in "say" function

```python
emoticon = "v.v"


def main():
	global emoticon
	say("Is anyone there?")
	emoticon = ":D"
	say("Oh, hi!")
	
def say(phrase):
	print(phrase + " " + emoticon)


main()
```


`BUTTON[previous, next]`