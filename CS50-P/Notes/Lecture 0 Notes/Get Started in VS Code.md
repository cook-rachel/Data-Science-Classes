---
tags:
  - extra
  - datascience
  - python
  - lecture0
  - notes
university: Harvard
year: "2022"
link:
cover: installpython.jpg
description: A quick-start guide for installing Python, configuring Conda, and setting up VS Code to run code smoothly. It also includes essential terminal commands and notes on basic Python concepts like functions and parameters.
---

`BUTTON[cs50p]` `BUTTON[edX-CS50P]`

# Lecture 0: Get Started in VS Code
---
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
label: "Next: Submitting Assignments"
icon: "arrow-right"
hidden: true
class: worksheet-button
tooltip: ""
id: "next"
style: primary
actions:
  - type: open
    link: "[[Submitting Assignments]]"

```
```meta-bind-button
label: "Previous: Functions & Variables"
icon: "arrow-left"
hidden: true
class: navigation-buttons
tooltip: ""
id: previous
style: primary
actions:
  - type: open
    link: "[[Functions & Variables]]"

```
## Set Up Python & Conda
- To install function code:
	- Press **Cmd + Shift + P**
	- Type and select `Shell Command: Install 'code' command in PATH`
- To install python
	- download python
	- **Cmd + Shift + P** --> `Python: Select Interpreter`
	- Paste this path: */Library/Frameworks/Python.framework/Versions/3.13/bin/python3*
	- Select *conda* for environment
- To install conda
	- download and install anaconda
	-` nano ~/.zshrc`
	- `conda deactivate`
	- `conda --version`
	- *(base)* is added before folder to show it is active
	- possibly some other steps between but finally got it to work
	
## Connecting VS Code Directory to Sharkology
- **To change directory:** 
- **To list files in that folder**: ls
- **To run**: python hello.py
- **Clear terminal screen**: Command (⌘) + K
- **To save**: Command (⌘) + S (white circle on file name shows changes have been made that need to be saved)
- **Annotate**: Command (⌘) + /
- **Comments**: """ instead of #
- Tab to finish typing
- Control + C to exit action in terminal if stuck


### Code Language
- example of a *function* is print
- functions can take in *arguments*, written using *parameters* (same thing, different viewpoint)
	- ex) sep and end in print function = parameters



`BUTTON[previous]` `BUTTON[next]`