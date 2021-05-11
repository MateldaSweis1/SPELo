# SPELo

Data Structures Preternship Project

Authors: Katie Greed, Jesus Robles, Marcelo Carrasquillo-Vilaró, Matelda Sweis

# Preternship Project - *SPELo*

**SPELo** is a simplified spelling and grammar checker.

This project centers around building a text processing software targeted towards educators and students in grades K-3 that corrects spelling and grammar errors in submitted text. A user will be able to input ‘.txt’ formatted files and choose to have the program output a version in PDF format with suggested edits and corrections. Implementing libraries, the program will be able to store a simplified dictionary that can be edited by the user. The spelling will be checked by running a comparison algorithm with a prerecorded dynamic array of english language words, and the program will search for words with the most similarities to the misspelled word. As for grammar, the program will include specific algorithms that will take in the text sentence by sentence and identify grammatical errors. The program may also have options like implementing the corrections or outputting the text with the recommended corrections to a PDF, which may allow teachers to grade assignments much more easily, but still allow students to implement the changes themselves to improve their spelling and writing skills.

Time spent: **32** hours spent in total

# SPELo - Part UI

The code in this repository uses the WSGI web application framework called Flask. Details on how to setup Flask in a project folder can be found [here](https://flask.palletsprojects.com/en/1.1.x/installation/). In order to see the working site, setup up Flask in the respective folder in Bash and then run the command **python "server.py"**. This will allow you to access the site by typing a url that will look something like **"http://127.0.0.1:5000"**.

Time spent: **32** hours spent in total

## Features

The following **functionality** is completed:

- [x] User can enter text into UI website.
- [x] Program runs immediately when all text is entered.
- [x] Text is returned in a subsequent box. 
- [x] Text is turned into txt file for user to manipulate. 

## Video Walkthrough

Here's a walkthrough of implemented user stories:

![SPELO_demo](https://media.giphy.com/media/alFvyiNCfOpbg1uLEl/giphy.gif)
