---
tags:
  - harvard
  - datascience
  - python
  - lecture4
  - supplemental_video
university: Harvard
year: "2022"
link: https://cs50.harvard.edu/python/shorts/api_calls/
cover: apicalls.jpg
description: Supplemental video on api calls.
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
label: "Next: Short - Creating Modules & Packages"
icon: "arrow-right"
hidden: true
class: worksheet-button
tooltip: ""
id: "next"
style: primary
actions:
  - type: open
    link: "[[Creating Modules and Packages]]"

```
```meta-bind-button
label: "Previous: Lecture 4 - Libaries"
icon: "arrow-left"
hidden: true
class: navigation-buttons
tooltip: ""
id: "previous"
style: primary
actions:
  - type: open
    link: "[[Libraries]]"

```
# Supplemental Video: API Calls
---

<iframe width="560" height="315" 
src="https://video.cs50.io/cyURNr9LZdM" 
title="YouTube video player" 
frameborder="0" 
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
allowfullscreen></iframe>
```python
import requests

def main():
	print("Search the Art Institute of Chicago!")
	artist = input("Artist: ")
	try:
		response = requests.get(
			"https://api.artic.edu/api/v1/artworks/search",
			{"q": artist} #from museum documentation
		)
		# print(response) #200 means api connected correctly
		response.raise_for_status()
	except requests.HTTPError:
		print("Couldn't complete API request")
		return
		
	content = response.json()
	for artwork in content["data"]: #content[data] from museum documentation
		print(f"- {artwork['title']}") #artwork[title] from museum documentation

main()
```


`BUTTON[previous, next]`