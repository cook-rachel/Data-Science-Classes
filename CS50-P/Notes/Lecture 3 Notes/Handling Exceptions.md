---
tags:
  - harvard
  - datascience
  - python
  - lecture3
  - supplemental_video
university: Harvard
year: "2022"
link: https://cs50.harvard.edu/python/shorts/handling_exceptions/
cover: handingexceptions.jpg
description: Supplemental video on handling exceptions with try and except.
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
label: "Next: Short - Raising Exceptions"
icon: "arrow-right"
hidden: true
class: worksheet-button
tooltip: ""
id: "next"
style: primary
actions:
  - type: open
    link: "[[Raising Exceptions]]"

```
```meta-bind-button
label: "Previous: Short - Debugging"
icon: "arrow-left"
hidden: true
class: navigation-buttons
tooltip: ""
id: "previous"
style: primary
actions:
  - type: open
    link: "[[Debugging]]"

```
# Supplemental Video - Handling Exceptions
---

<iframe width="560" height="315" 
src="https://video.cs50.io/wjWMOYLNK_E"
title="YouTube video player" 
frameborder="0" 
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
allowfullscreen></iframe>

```python
##add try/except
distances = {
"Voyager 1": "163",
"Voyager 2": "136",
"Pioneer 10": "80 AU",
"New Horizons": "58",
"Pioneer 11": "44 AU"
}

def main():
	spacecraft = input("Enter a spacecraft: ")
	try:
		au = float(distances[spacecraft])
	except ValueError:
		print("Can't convert '{distances[spacecraft]}' to a float")
		return

	m = convert(au)
	print(f"{m} m away")

def convert(au):
	return au * 14959780700

main()


#add second except
distances = {
"Voyager 1": "163",
"Voyager 2": "136",
"Pioneer 10": "80 AU",
"New Horizons": "58",
"Pioneer 11": "44 AU"
}

def main():
	spacecraft = input("Enter a spacecraft: ")
	try:
		au = float(distances[spacecraft])
	except KeyError:
		print(f"'{spacecraft}' is not in dictionary")
		return
	except ValueError:
		print(f"Can't convert '{distances[spacecraft]}' to a float")
		return

	m = convert(au)
	print(f"{m} m away")

def convert(au):
	return au * 14959780700

main()
```



`BUTTON[previous, next]`