AirBnb Clone- The console. 
![airbnb image](https://user-images.githubusercontent.com/106445167/215116809-f1433630-c4ee-4dee-95e9-cbe9c10bd509.png)

DESCRIPTION:  
An Airbnb like web-service built with Python, MySQL, Flask, HTML, and Javascript. The goal of the project is to deploy a recreation of the AirBnB website.

LEARNING OBJECTIVE :
How to create a Python package
How to create a command interpreter in Python using the cmd module
What is Unit testing and how to implement it in a large project
How to serialize and deserialize a Class
How to write and read a JSON file
How to manage datetime
What is an UUID
What is *args and how to use it
What is **kwargs and how to use it
How to handle named arguments in a function

COMMAND INTERPRETER:
![the console](https://user-images.githubusercontent.com/106445167/215117023-000bc02d-e853-4954-8b3d-daaee19291e1.png)
Command interpreter is similar to shell but limited to a specific use-case. In this case, we want to be able to manage the objects of our project:
Create a new object (ex: a new User or a new Place)
Retrieve an object from a file, a database etc…
Do operations on objects (count, compute stats, etc…)
Update attributes of an object
Destroy an object


USING THE CONSOLE:

The console can be run both interactively and non-interactively. To run the console in interactive mode, pipe any command(s) into an execution of the file console.py at the command line.
 
 $ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$


 To use the console in non-interactive mode;
 
 $ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
 
