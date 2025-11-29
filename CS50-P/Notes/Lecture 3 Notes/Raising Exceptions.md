---
tags:
  - harvard
  - datascience
  - python
  - lecture3
  - supplemental_video
university: Harvard
year: "2022"
link: https://cs50.harvard.edu/python/shorts/raising_exceptions/
cover: raisingexceptions.jpg
description: Supplemental video on raising exceptions and specifying errors.
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
label: "Next: Problem Set - Fuel Gauge"
icon: "arrow-right"
hidden: true
class: worksheet-button
tooltip: ""
id: "next"
style: primary
actions:
  - type: open
    link: "[[Fuel Gauge]]"

```
```meta-bind-button
label: "Previous: Short - Handling Exceptions"
icon: "arrow-left"
hidden: true
class: navigation-buttons
tooltip: ""
id: "previous"
style: primary
actions:
  - type: open
    link: "[[Handling Exceptions]]"

```
# Supplemental Video: Raising Exceptions
---

<iframe width="560" height="315" 
src="https://video.cs50.io/BltXeMM96DA" 
title="YouTube video player" 
frameborder="0" 
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
allowfullscreen></iframe>

```python
# use raise exception
def main():
	pace = get_pace(miles=26.2, minutes=0)
	print(f"You need to run each mile in {round(pace, 2)} minutes.")

def get_pace(miles, minutes):
	if not minutes > 0:
		raise Exception() #or use raise ValueError to specify in error message
		return minutes / miles  

main()


## specify error
def main():
	pace = get_pace(miles=26.2, minutes=0)
	print(f"You need to run each mile in {round(pace, 2)} minutes.")

def get_pace(miles, minutes):
	if not minutes > 0:
		raise ValueError("Minutes must be greater than 0")
	return minutes / miles

main()
```


`BUTTON[previous, next]`