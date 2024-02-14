
### Learning Objectives

By the end of this project, you are expected to be able to explain to anyone, without the help of Google:

**General**
- Why JavaScript programming is amazing
- How to create an object in JavaScript
- What 'this' means
- What 'undefined' means
- Why variable type and scope are important
- What is a closure
- What is a prototype
- How to inherit an object from another

### Copyright - Plagiarism

- You must come up with solutions for the tasks yourself to meet the learning objectives.
- No copying and pasting someone else’s work.
- Not allowed to publish any content of this project.
- Any form of plagiarism is strictly forbidden and will result in removal from the program.

### Requirements

**General**
- Allowed editors: vi, vim, emacs
- All your files will be interpreted on Ubuntu 20.04 LTS using node (version 14.x)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/node
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should be semistandard compliant. Rules of Standard + semicolons on top. Also as reference: AirBnB style
- All your files must be executable
- The length of your files will be tested using wc
- You are not allowed to use var

### More Info

- Install Node 14
  ```
  $ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
  $ sudo apt-get install -y nodejs
  ```
- Install semi-standard
  ```
  $ sudo npm install semistandard --global
  ```

### Quiz Questions

- Great! You've completed the quiz successfully! Keep going! (Show quiz)

## Tasks

### 0. Rectangle #0

**Mandatory**

Write an empty class Rectangle that defines a rectangle:

- You must use the class notation for defining your class

Repo:
- [GitHub repository: alx-higher_level_programming](#)
- Directory: 0x13-javascript_objects_scopes_closures
- File: 0-rectangle.js

### 1. Rectangle #1

**Mandatory**

Write a class Rectangle that defines a rectangle:

- You must use the class notation for defining your class
- The constructor must take 2 arguments w and h
- Initialize the instance attribute width with the value of w
- Initialize the instance attribute height with the value of h

Repo:
- [GitHub repository: alx-higher_level_programming](#)
- Directory: 0x13-javascript_objects_scopes_closures
- File: 1-rectangle.js

### 2. Rectangle #2

**Mandatory**

Write a class Rectangle that defines a rectangle:

- You must use the class notation for defining your class
- The constructor must take 2 arguments w and h
- Initialize the instance attribute width with the value of w
- Initialize the instance attribute height with the value of h
- If w or h is equal to 0 or not a positive integer, create an empty object

Repo:
- [GitHub repository: alx-higher_level_programming](#)
- Directory: 0x13-javascript_objects_scopes_closures
- File: 2-rectangle.js

### 3. Rectangle #3

**Mandatory**

Write a class Rectangle that defines a rectangle:

- You must use the class notation for defining your class
- The constructor must take 2 arguments: w and h
- Initialize the instance attribute width with the value of w
- Initialize the instance attribute height with the value of h
- If w or h is equal to 0 or not a positive integer, create an empty object
- Create an instance method called print() that prints the rectangle using the character X

Repo:
- [GitHub repository: alx-higher_level_programming](#)
- Directory: 0x13-javascript_objects_scopes_closures
- File: 3-rectangle.js

### 4. Rectangle #4

**Mandatory**

Write a class Rectangle that defines a rectangle:

- You must use the class notation for defining your class
- The constructor must take 2 arguments: w and h
- Initialize the instance attribute width with the value of w
- Initialize the instance attribute height with the value of h
- If w or h is equal to 0 or not a positive integer, create an empty object
- Create an instance method called print() that prints the rectangle using the character X
- Create an instance method called rotate() that exchanges the width and the height of the rectangle
- Create an instance method called double() that multiples the width and the height of the rectangle by 2

Repo:
- [GitHub repository: alx-higher_level_programming](#)
- Directory: 0x13-javascript_objects_scopes_closures
- File: 4-rectangle.js

### 5. Square #0

**Mandatory**

Write a class Square that defines a square and inherits from Rectangle of 4-rectangle.js:

- You must use the class notation for defining your class and extends
- The constructor must take 1 argument: size
- The constructor of Rectangle must be called (by using super())

Repo:
- [GitHub repository: alx-higher_level_programming](#)
- Directory: 0x13-javascript_objects_scopes_closures
- File: 5-square.js

### 6. Square #1

**Mandatory**

Write a class Square that defines a square and inherits from Square of 5-square.js:

- You must use the class notation for defining your class and