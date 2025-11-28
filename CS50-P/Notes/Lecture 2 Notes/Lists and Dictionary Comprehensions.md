---
tags:
  - harvard
  - datascience
  - python
  - lecture2
  - supplemental_video
university: Harvard
year: "2022"
link: https://cs50.harvard.edu/python/shorts/list_dictionary_comprehensions/
cover: listsdictionarycomp.jpg
description: Supplemental video on list comprehension with and without filter.
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
label: "Next: Short - List Methods"
icon: "arrow-right"
hidden: true
class: worksheet-button
tooltip: ""
id: "next"
style: primary
actions:
  - type: open
    link: "[[List Methods]]"

```
```meta-bind-button
label: "Previous: Short - Lists"
icon: "arrow-left"
hidden: true
class: navigation-buttons
tooltip: ""
id: "previous"
style: primary
actions:
  - type: open
    link: "[[Lists]]"

```
# Supplemental Video: List & Dictionary Comprehensions
---

<iframe width="560" height="315" 
src="https://video.cs50.io/AK3HbkbgiQA" 
title="YouTube video player" 
frameborder="0" 
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
allowfullscreen></iframe>

```python
### USE LIST COMPREHENSION
from helpers import get_words, save_counts

def main():
	counts = {}
	words = get_words("address.txt")
	lowercase_words = [word.lower() for word in words] #list comprehension to turn all words to lower case

	for word in lowercase_words:
		if word in counts:
		counts[word] += 1
	else:
		counts[word] = 1

	save_counts(counts)

main()



### USE LIST COMPREHENSION with filter
from helpers import get_words, save_counts

def main():
	counts = {}
	words = get_words("address.txt")
	lowercase_words = [word.lower() for word in words if len(word) > 4] #list comprehension to turn all words to lower case, keep words greater than 4 letters

	for word in lowercase_words:
		if word in counts:
		counts[word] += 1
	else:
		counts[word] = 1

	save_counts(counts)

main()


### USE DICTIONARY COMPREHENSION with filter
from helpers import get_words, save_counts

def main():
	words = get_words("address.txt")
	lowercase_words = [word.lower() for word in words if len(word) > 4] #list comprehension to turn all words to lower case, keep words greater than 4 letters
	counts = {word: words.count(word) for word in lowercase_words}

	save_counts(counts)

main()
```


`BUTTON[previous]` `BUTTON[next]`
