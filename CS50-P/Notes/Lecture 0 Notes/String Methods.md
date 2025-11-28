---
tags:
  - harvard
  - datascience
  - python
  - lecture0
  - supplemental_video
university: Harvard
year: "2022"
link: https://cs50.harvard.edu/python/shorts/string_methods/
cover: stringmethods.jpg
description: Python offers a rich set of built-in methods for manipulating and transforming strings such as strip( ), replace( ), upper( ), etc.
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
label: "Next: Problem Set - Indoor Voice"
icon: "arrow-right"
hidden: true
class: worksheet-button
tooltip: ""
id: "next"
style: primary
actions:
  - type: open
    link: "[[Indoor Voice]]"

```
```meta-bind-button
label: "Previous: Short - Side Effects"
icon: "arrow-left"
hidden: true
class: navigation-buttons
tooltip: ""
id: "previous"
style: primary
actions:
  - type: open
    link: "[[Side Effects]]"

```
# Supplemental Video: String Methods
---
<iframe width="560" height="315" 
src="https://video.cs50.io/f4_ZPwvKF5g" 
title="YouTube video player" 
frameborder="0" 
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
allowfullscreen></iframe>

```python
SHOWS = [
	" Avatar: the last airbender",
	"Ben 10",
	"Arthur",
	" Spongebob Squarepants",
	"Phineas and ferb",
	"Kim possible",
	"Jimmy Neutron",
	"the Proud family"
]


def main():
	cleaned_shows = []    # create empty list
	for show in SHOWS:
		cleaned_shows.append(show.title().strip())    #put in new list
	
	print(', '.join(cleaned_shows)) #join list elements with comma between




main()
```


`BUTTON[previous]` `BUTTON[next]`
