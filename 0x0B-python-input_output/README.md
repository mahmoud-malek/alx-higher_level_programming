# 0x0B. Python - Input/Output

![Python](https://img.shields.io/badge/Python-3.8.5-blue)

This project is part of the ALX Software Engineering program. It covers Python input and output, including working with files, JSON serialization, and deserialization.

## Table of Contents

- [Project Description](#project-description)
- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [Tasks](#tasks)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Project Description

In this project, you will work on various tasks related to Python's input and output, including reading and writing files, JSON manipulation, and more. The goal is to strengthen your understanding of Python as a programming language.

## Learning Objectives

By the end of this project, you should be able to explain to anyone:

- Why Python programming is awesome
- How to open a file
- How to write text to a file
- How to read the full content of a file
- How to read a file line by line
- How to move the cursor in a file
- How to make sure a file is closed after using it
- What the `with` statement is and how to use it
- What is JSON
- What is serialization
- What is deserialization
- How to convert a Python data structure to a JSON string
- How to convert a JSON string to a Python data structure

## Requirements

### Python Scripts

- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3.8.5
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the project folder, is mandatory
- Your code should use `pycodestyle` (version 2.8.*)
- All your files must be executable
- The length of your files will be tested using `wc`

### Python Test Cases

- Allowed editors: vi, vim, emacs
- All your files should end with a new line
- All your test files should be inside a folder named `tests`
- All your test files should be text files with the extension `.txt`
- All your tests should be executed by using this command: `python3 -m doctest ./tests/*`
- All your modules should have documentation
- All your classes should have documentation
- All your functions (inside and outside a class) should have documentation
- A documentation is not a simple word, it's a real sentence explaining the purpose of the module, class, or method

## Tasks

1. [Read file](#0-read-file)
2. [Write to a file](#1-write-to-a-file)
3. [Append to a file](#2-append-to-a-file)
4. [To JSON string](#3-to-json-string)
5. [From JSON string to Object](#4-from-json-string-to-object)
6. [Save Object to a file](#5-save-object-to-a-file)
7. [Create object from a JSON file](#6-create-object-from-a-json-file)
8. [Class to JSON](#7-class-to-json)
9. [Student to JSON](#8-student-to-json)
10. [Student to JSON with filter](#9-student-to-json-with-filter)
11. [Student to disk and reload](#10-student-to-disk-and-reload)
12. [Pascal's Triangle](#11-pascals-triangle)

## Installation

To get started with this project, follow these steps:

1. Clone the repository to your local machine using `git clone`.

```bash
git clone https://github.com/yourusername/0x0B-python-input_output.git
```

2. Change to the project directory.

```bash
cd 0x0B-python-input_output
```

3. You are now ready to work on the project!

## Usage

Each task in the project is a separate Python script. You can run them individually to test your implementation. For example:

```bash
python3 0-read_file.py
```
