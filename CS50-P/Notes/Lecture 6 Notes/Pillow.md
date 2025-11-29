---
tags:
  - harvard
  - datascience
  - python
  - lecture6
  - supplemental_video
university: Harvard
year: "2022"
link: https://cs50.harvard.edu/python/shorts/pillow/
cover: pillow.jpg
description: Supplemental video on pillow from sys library.
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
label: "Next: Short - Reading & Writing CSVs"
icon: "arrow-right"
hidden: true
class: worksheet-button
tooltip: ""
id: "next"
style: primary
actions:
  - type: open
    link: "[[Reading and Writing CSVs]]"

```
```meta-bind-button
label: "Previous: Lecture 6 - File I/O"
icon: "arrow-left"
hidden: true
class: navigation-buttons
tooltip: ""
id: "previous"
style: primary
actions:
  - type: open
    link: "[[File IO]]"

```
# Supplemental Video: Pillow
---

<iframe width="560" height="315" 
src="https://video.cs50.io/9m1FCOHIIcA" 
title="YouTube video player" frameborder="0" 
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
allowfullscreen></iframe>

```python
import sys
from PIL import Image
from PIL import ImageFilter

def main():
    with Image.open("in.jpeg") as img:
        # print(img.size)
        # print(img.format)
        img = img.rotate(180)
		# img = img.filter(ImageFilter.BLUR)
        img = img.filter(ImageFilter.FIND_EDGES)
        img.save("out.jpeg")

main()


```


`BUTTON[previous, next]`
