---
tags:
  - harvard
  - datascience
  - python
  - lecture2
  - supplemental_video
university: Harvard
year: "2022"
link: https://cs50.harvard.edu/python/shorts/string_slicing/
cover: stringslicing.jpg
description: Supplemental video on string slicing using indexes.
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
label: "Next: Short - Tuples"
icon: "arrow-right"
hidden: true
class: worksheet-button
tooltip: ""
id: "next"
style: primary
actions:
  - type: open
    link: "[[Tuples]]"

```
```meta-bind-button
label: "Previous: Short - List Methods"
icon: "arrow-left"
hidden: true
class: navigation-buttons
tooltip: ""
id: "previous"
style: primary
actions:
  - type: open
    link: "[[List Methods]]"

```
# Supplemental Video: String Slicing
---

<iframe width="560" height="315" 
src="https://video.cs50.io/COWxTAPkr_k" 
title="YouTube video player" 
frameborder="0" 
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
allowfullscreen></iframe>

```python
  

def main():
	phone = "617-495-1000"
	print(phone[0:3]) #can use indexes to find area code (3 b/c up to but not including last number)
	print(phone[:3]) #also works if want first index
	print(phone[8:]) #last four digits through last index
	print(phone[-4:]) #last 4

main()

```


`BUTTON[previous, next]`