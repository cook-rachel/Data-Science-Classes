---
tags:
  - harvard
  - datascience
  - python
  - lecture0
  - supplemental_video
university: Harvard
year: "2022"
link: https://cs50.harvard.edu/python/shorts/return_values/
cover: returnvalues.jpg
description: Supplemental video on return values used in functions.
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
label: "Next: Short - Side Effects"
icon: "arrow-right"
hidden: true
class: worksheet-button
tooltip: ""
id: "next"
style: primary
actions:
  - type: open
    link: "[[Side Effects]]"

```
```meta-bind-button
label: "Previous: Short - Variables"
icon: "arrow-left"
hidden: true
class: navigation-buttons
tooltip: ""
id: "previous"
style: primary
actions:
  - type: open
    link: "[[Variables]]"

```
# Supplemental Video: Return Values
---

<iframe width="560" height="315" 
src="https://video.cs50.io/Jt1p_qQYeUU" 
title="YouTube video player" 
frameborder="0" 
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
allowfullscreen></iframe>

```python
def greet(input):
	if "hello" in input:
		return "hello, there"
	else:
		return "I'm not sure what you mean"

greeting = greet("hello, computer") #fill this out differently to test
print("Hm, " + greeting)
```


`BUTTON[previous]` `BUTTON[next]`
