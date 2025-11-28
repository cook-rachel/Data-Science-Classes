---
tags:
  - harvard
  - datascience
  - python
  - lecture2
  - supplemental_video
university: Harvard
year: "2022"
link: https://cs50.harvard.edu/python/shorts/while_loops/
cover: whileloops.jpg
description: Supplemental video on while loops in functions.
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
label: "Next: Problem Set - camelCase"
icon: "arrow-right"
hidden: true
class: worksheet-button
tooltip: ""
id: "next"
style: primary
actions:
  - type: open
    link: "[[camelCase]]"

```
```meta-bind-button
label: "Previous: Short - Tuples"
icon: "arrow-left"
hidden: true
class: navigation-buttons
tooltip: ""
id: "previous"
style: primary
actions:
  - type: open
    link: "[[Tuples]]"

```
# Supplemental Video: While Loops
---

<iframe width="560" height="315" 
src="https://video.cs50.io/CYobbeiGgp8" 
title="YouTube video player" 
frameborder="0" 
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
allowfullscreen></iframe>

```python
from soil import sample

def main():
	moisture = sample()
	days = 0
	print(f"Day {days}: Moisture is {moisture}%")
	
	while moisture > 20:
		moisture = sample()
		days += 1 #add one day each time
		print(f"Day {days}: Moisture is {moisture}%")
		print("Time to water!") #exit loop when <= 20

main()

```


`BUTTON[previous]` `BUTTON[next]`
