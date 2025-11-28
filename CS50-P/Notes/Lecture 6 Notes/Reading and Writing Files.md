---
tags:
  - harvard
  - datascience
  - python
  - lecture6
  - supplemental_video
university: Harvard
year: "2022"
link: https://cs50.harvard.edu/python/shorts/reading_writing_files/
cover: readingandwritingfiles.jpg
description: Supplemental videos on reading and writing files with open.
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
label: "Next: Problem Set - Lines of Code"
icon: "arrow-right"
hidden: true
class: worksheet-button
tooltip: ""
id: "next"
style: primary
actions:
  - type: open
    link: "[[Lines of Code]]"

```
```meta-bind-button
label: "Previous: Short - Reading & Writing CSVs"
icon: "arrow-left"
hidden: true
class: navigation-buttons
tooltip: ""
id: "previous"
style: primary
actions:
  - type: open
    link: "[[Reading and Writing CSVs]]"

```
# Supplemental Video: Reading & Writing Files
---

<iframe width="560" height="315" 
src="https://video.cs50.io/0bCWJjW7SgA" 
title="YouTube video player" frameborder="0" 
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
allowfullscreen></iframe>

```python
"""
Reading and Writing Files
"""

def main():
    with open("src_readwritefiles/alice.txt", "r") as f:
        # contents = f.read() #read whole thing
        contents = f.readlines()

    chapter1 = contents[52:271]
    with open("chapter1.txt", "w") as f:
        f.writelines(chapter1)
    

main()


```


`BUTTON[previous]` `BUTTON[next]`
