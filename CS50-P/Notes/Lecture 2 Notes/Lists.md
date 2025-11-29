---
tags:
  - harvard
  - datascience
  - python
  - lecture2
  - supplemental_video
university: Harvard
year: "2022"
link:
cover: lists.jpg
description: Supplemental video on lists including append, remove, insert, and reverse.
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
label: "Next: Short - Lists & Dictionary Comprehensions"
icon: "arrow-right"
hidden: true
class: worksheet-button
tooltip: ""
id: "next"
style: primary
actions:
  - type: open
    link: "[[Lists and Dictionary Comprehensions]]"

```
```meta-bind-button
label: "Previous: Short - For Loops"
icon: "arrow-left"
hidden: true
class: navigation-buttons
tooltip: ""
id: "previous"
style: primary
actions:
  - type: open
    link: "[[For Loops]]"

```
# Supplemental Video: Lists
---

<iframe width="560" height="315" 
src="https://video.cs50.io/xdpABsJZQYU" 
title="YouTube video player" 
frameborder="0" 
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
allowfullscreen></iframe>

```python

## APPEND, REMOVE from List
results = ["Mario", "Luigi"]

#to add additional items to list
results.append("Princess")

results.append(["Bowser", "Donkey Kong Jr."]) #this adds entire list as grouped LIST
results.remove(["Bowser", "Donkey Kong Jr."]) #let's remove and try another way

results.extend(["Bowser", "Donkey Kong Jr."]) #this adds multiple items correctly  

print(results)


  

### INSERT and REVERSE in List
results = ["Mario", "Luigi", "Princess", "Yoshi", "Koopa Troopa", "Toad", "Bowser", "Donkey Kong Jr."]

results.remove("Bowser") #remove's first instance of bowser
# results.append("Bowser") #adds to end of list - not what we want
results.insert(0, "Bowser") #specify location to add him

results.reverse() #to reverse list
  
print(results)
```


`BUTTON[previous, next]`
