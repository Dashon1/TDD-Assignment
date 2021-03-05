# TDD-Assignment
My first attempt at test driven development

#Environment
This was developed in python version 3.9.2 on Arch Linux
The instructions to run however will be presented for windows 10

Download link here - https://www.python.org/downloads/


#Notes about downloading. When installing make sure to add python to PATH if it does not do, so already.
This will avoid you having to manually locate the full path of the python interpreter in order to run these files.



#Running the unit tests

All unit tests are in the same directories as the functions that they test. 
This made it easier to import the functions
This repository contains a few folders.
One folder for each set of functions and unit tests, as well as screenshots of all tests passing.
Which admittedly isn't very useful.
The other folder contains all the functions minus the unit tests as well as the main program.
The main program should be named calc.py




#Run the main program from the command line like so:

C:\User\Example> python C:\User\path\to\calc.py

Powershell or cmd should be fine.



#Usage
The program will prompt you to type the number "1" or "2" without the quotes.
Choose the number corresponding to the type of calculator you would like to use.
Follow the prompts unti your result is printed.





#Exiting
You may gracefully exit the program at any time by pressing Control + C
The program is designed to catch the keyboardInterrupt event.
