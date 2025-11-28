---
tags:
  - harvard
  - datascience
  - python
  - lecture7
  - problem_set
university: Harvard
year: "2022"
link: https://cs50.harvard.edu/python/psets/7/response/
cover: reponsevalidation.jpg
description: In a file called `response.py`, using either [validator-collection](https://pypi.org/project/validator-collection/) or [validators](https://github.com/kvesteri/validators) from PyPI, implement a program that prompts the user for an email address via `input` and then prints `Valid` or `Invalid`, respectively, if the input is a syntatically valid email address. You may not use `re`. And do not validate whether the email address’s domain name actually exists.
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
label: "Next: Lecture 8 - Object-Oriented Programming"
icon: "arrow-right"
hidden: true
class: worksheet-button
tooltip: ""
id: "next"
style: primary
actions:
  - type: open
    link: "[[Object-Oriented Programming]]"

```
```meta-bind-button
label: "Previous: Problem Set - Regular,um,Expressions"
icon: "arrow-left"
hidden: true
class: navigation-buttons
tooltip: ""
id: "previous"
style: primary
actions:
  - type: open
    link: "[[Regular,um,Expressions]]"

```
# Problem Set 7: Response Validation
---

When creating a [Google Form](https://www.google.com/forms/about/) that prompts users for a short answer (or paragraph), it’s possible to enable [response validation](https://support.google.com/docs/answer/3378864) and require that the user’s input match a [regular expression](https://support.google.com/a/answer/1371415). For instance, you could require that a user input an email address with a regex like [this one](https://html.spec.whatwg.org/multipage/input.html#valid-e-mail-address):

```
^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$
```

Or you could more easily use Google’s built-in support for validating an email address, per the screenshot below, much like you could use a library in your own code:

![Google Form](https://cs50.harvard.edu/python/2022/psets/7/response/form.png)

In a file called `response.py`, using either [validator-collection](https://pypi.org/project/validator-collection/) or [validators](https://github.com/kvesteri/validators) from PyPI, implement a program that prompts the user for an email address via `input` and then prints `Valid` or `Invalid`, respectively, if the input is a syntatically valid email address. You may not use `re`. And do not validate whether the email address’s domain name actually exists.

#### Hints
- Note that you can install validator-collection with:
    
    ```
    pip install validator-collection
    ```
    
    Click **Homepage** to find your way to the library’s documentation.
    
- Note that you can install validators with:
    
    ```
    pip install validators
    ```
    
    Click **Homepage** to find your way to the library’s documentation.
    

## Demo
```
$ python response.py
What's your email address? malan
Invalid
$ python response.py
What's your email address? malan at harvard dot edu
Invalid
$ python response.py
What's your email address? malan@harvard.edu
Valid
$
```

## Before You Begin

Log into [cs50.dev](https://cs50.dev/), click on your terminal window, and execute `cd` by itself. You should find that your terminal window’s prompt resembles the below:

```
$
```

Next execute

```
mkdir response
```

to make a folder called `response` in your codespace.

Then execute

```
cd response
```

to change directories into that folder. You should now see your terminal prompt as `response/ $`. You can now execute

```
code response.py
```

to make a file called `response.py` where you’ll write your program.

## How to Test

Here’s how to test your code manually:

- Run your program with `python response.py`. Ensure your program prompts you for an email, then type `malan@harvard.edu`, followed by Enter. Your program should output `Valid`.
- Run your program with `python response.py`. Type your own email, followed by Enter. Your program should output `Valid`.
- Run your program with `python response.py`. Type `malan@@@harvard.edu`, followed by Enter. Your program should output `Invalid`.
- Run your program with `python response.py`. Mistype your own email, including an extra `.` before `.com`, for example. Press enter and your program should output `Invalid`.

You can execute the below to check your code using `check50`, a program that CS50 will use to test your code when you submit. But be sure to test it yourself as well!

```
check50 cs50/problems/2022/python/response
```

Green smilies mean your program has passed a test! Red frownies will indicate your program output something unexpected. Visit the URL that `check50` outputs to see the input `check50` handed to your program, what output it expected, and what output your program actually gave.

## How to Submit

In your terminal, execute the below to submit your work.

```
submit50 cs50/problems/2022/python/response
```


`BUTTON[previous]` `BUTTON[next]`
