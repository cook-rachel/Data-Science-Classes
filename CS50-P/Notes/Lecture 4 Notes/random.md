---
tags:
  - harvard
  - datascience
  - python
  - lecture4
  - supplemental_video
university: Harvard
year: "2022"
link: https://cs50.harvard.edu/python/shorts/random/
cover: random.jpg
description: Supplemental video on random, sampling with replacement, seeds.
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
label: "Next: Short - Style"
icon: "arrow-right"
hidden: true
class: worksheet-button
tooltip: ""
id: "next"
style: primary
actions:
  - type: open
    link: "[[Style]]"

```
```meta-bind-button
label: "Previous: Short - Creating Modules & Packages"
icon: "arrow-left"
hidden: true
class: navigation-buttons
tooltip: ""
id: "previous"
style: primary
actions:
  - type: open
    link: "[[Creating Modules and Packages]]"

```
# Problem Set 4: random
---

<iframe width="560" height="315" 
src="https://video.cs50.io/yec-UUauUV8" 
title="YouTube video player" 
frameborder="0" 
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
allowfullscreen></iframe>
```python

## choice --> random sampling ONE item from list
import random
cards = ["jack", "queen", "king"]

def main():
	print(random.choice(cards))

main()



# choices --> sampling with replacement
import random
cards = ["jack", "queen", "king"]

def main():
	print(random.choices(cards, k=2)) # k = how many from list to output

main()


  

# sample --> sampling without replacement
import random
cards = ["jack", "queen", "king"]

def main():
	print(random.sample(cards, k=2)) # k = how many from list to output

main()



## choices + weights -> sampling with replacement + weights
import random
cards = ["jack", "queen", "king"]

def main():
	print(random.choices(cards, weights=[75,20,5], k=2)) # weights = % of how often will get choosen

main()



## seed (random using computer time)
import random
cards = ["jack", "queen", "king"]

def main():
	random.seed() #random based on time of system
	print(random.choices(cards, k=2))

main()



## seed - using it as debugger
import random
cards = ["jack", "queen", "king"]

def main():
	random.seed(0) #set to 0 or 1 to make it stay constant so can test
	print(random.choices(cards, k=2))

main()
```


`BUTTON[previous, next]`