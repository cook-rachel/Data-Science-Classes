---
tags:
  - harvard
  - datascience
  - python
  - lecture3
  - supplemental_video
university: Harvard
year: "2022"
link: https://cs50.harvard.edu/python/shorts/debugging/
cover: debugging.jpg
description: Supplemental video on debugging using the debugger.
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
label: "Next: Short - Handing Exceptions"
icon: "arrow-right"
hidden: true
class: worksheet-button
tooltip: ""
id: "next"
style: primary
actions:
  - type: open
    link: "[[Handling Exceptions]]"

```
```meta-bind-button
label: "Previous: Lecture 3 - Exceptions"
icon: "arrow-left"
hidden: true
class: navigation-buttons
tooltip: ""
id: "previous"
style: primary
actions:
  - type: open
    link: "[[Exceptions]]"

```
# Supplemental Video - Debugging
---


<iframe width="560" height="315" 
src="https://video.cs50.io/2hsn7AxXKmg" 
title="YouTube video player" 
frameborder="0" 
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
allowfullscreen></iframe>

```python
##use print to debug
def main():
	height = int(input("Height: "))
	pyramid(height)

def pyramid(n):
	for i in range(n):
		print(i, end="")
		print("#" * (i+1))

if __name__ == "__main__": #for larger files where you only want to run main?
main()

  
  

##use debugger
def main():
	height = int(input("Height: ")) #step over (don't need to look at int function as we didnt write it)
	pyramid(height) #step into

def pyramid(n):
	for i in range(n): #step over
		print("#" * i) #step over

if __name__ == "__main__": #for larger files where you only want to run main?
main() ## set breakpoint here, step into

```


`BUTTON[previous, next]`