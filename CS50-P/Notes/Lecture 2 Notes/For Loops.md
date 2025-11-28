---
tags:
  - harvard
  - datascience
  - python
  - lecture2
  - supplemental_video
university: Harvard
year: "2022"
link: https://cs50.harvard.edu/python/shorts/for_loops/
cover: forloops.jpg
description: Supplemental video on for loops and using items in a dictionary.
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
label: "Next: Short - Lists"
icon: "arrow-right"
hidden: true
class: worksheet-button
tooltip: ""
id: "next"
style: primary
actions:
  - type: open
    link: "[[Lists]]"

```
```meta-bind-button
label: "Previous: Short - Dictionary Methods"
icon: "arrow-left"
hidden: true
class: navigation-buttons
tooltip: ""
id: "previous"
style: primary
actions:
  - type: open
    link: "[[Dictionary Methods]]"

```
# Supplemental Video: For Loops
---

<iframe width="560" height="315" 
src="https://video.cs50.io/iTRBRXOMzeM" 
title="YouTube video player" 
frameborder="0" 
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
allowfullscreen></iframe>

```python
## USING ITEMS in DICTIONARY

invitees = {
	"Mario":"Princess Peach", "Luigi":"Princess Peach", "Daisy":"Princess Peach", "Yoshi":"Princess Peach"
	}

def main():
	for receiver, sender in invitees.items():
	print(write_letter(receiver, sender))
	
def write_letter(receiver, sender):
	return f"""

	+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
	
		Dear {receiver},
		
		  
		
		You are cordially invited to a ball at Peach's
		
		Castle this evening, 7:00 PM.
		
		  
		
		Sincerely,
		
		{sender}
	
	+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
	
	"""
	
main()


  

## FOR LOOP
names = ["Mario", "Luigi", "Daisy", "Yoshi"]

def main():

for i in range(len(names)):
	print(write_letter(names[i], "Princess Peach"))

def write_letter(receiver, sender):
	return f"""

	+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
	
		Dear {receiver},
		
		  
		
		You are cordially invited to a ball at Peach's
		
		Castle this evening, 7:00 PM.
		
		  
		
		Sincerely,
		
		{sender}
	
	+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
	
	"""
  
main()



## SIMPLFY FOR LOOP
names = ["Mario", "Luigi", "Daisy", "Yoshi"]

def main():
	for name in names:
	print(write_letter(name, "Princess Peach"))

def write_letter(receiver, sender):
	return f"""

	+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
	
		Dear {receiver},
		
		  
		
		You are cordially invited to a ball at Peach's
		
		Castle this evening, 7:00 PM.
		
		  
		
		Sincerely,
		
		{sender}
	
	+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
	
	"""
	
main()
```


`BUTTON[previous]` `BUTTON[next]`
