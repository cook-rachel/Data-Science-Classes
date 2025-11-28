---
tags:
  - harvard
  - datascience
  - python
  - lecture4
  - supplemental_video
university: Harvard
year: "2022"
link: https://cs50.harvard.edu/python/shorts/creating_modules_packages/
cover: creatingmodules.png
description: Supplemental video on packages and modules using _init_,py
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
label: "Next: Short - random"
icon: "arrow-right"
hidden: true
class: worksheet-button
tooltip: ""
id: "next"
style: primary
actions:
  - type: open
    link: "[[random]]"

```
```meta-bind-button
label: "Previous: Short - API Calls"
icon: "arrow-left"
hidden: true
class: navigation-buttons
tooltip: ""
id: "previous"
style: primary
actions:
  - type: open
    link: "[[API Calls]]"

```
# Supplemental Video: Creating Modules & Packages
---

<iframe width="560" height="315" 
src="https://video.cs50.io/imrloYMePL0" 
title="YouTube video player" 
frameborder="0" 
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
allowfullscreen></iframe>
```python
## ARTWORK
from artwork_rs import get_artwork

def main():
	artwork = input("Artwork: ")
	artworks = get_artwork(query=artwork, limit=3)
	
	for artwork in artworks:
		print(f"- {artwork}")

main()

## ARTIST
from artists_rs import get_artists

def main():
	artist = input("Artist: ")
	artists = get_artists(query=artist, limit=3)

	for artist in artists:
		print(f"- {artist}")

main()


### PACKAGES (collection of multiple modules) - create a folder to put all of the modules in
# create file called "__init__.py" which can be empty

from museum_rs.artists_rs import get_artists
#from museum_rs.artwork_rs import get_artwork

def main():
	artist = input("Artist: ")
	#artwork = input("Artwork: ")
	artists = get_artists(query=artist, limit = 3)
	#artworks = get_artwork(query=artwork, limit=3)
	
	for artist in artists:
		print(f"ARTIST: {artist}")
		#print(f"ARTWORK: {artworks}")
  
main()



```


`BUTTON[previous]` `BUTTON[next]`
