# Build a Static Site Generator with Python

## Status

**Published**

## Overview

Used Python3, pip and ran ssg.py file to execute project.

## Installation

### Windows
Open a command prompt or powershell and run the following commands, replacing 'project-root' with the path to the root folder of the project.
```
> cd 'project-root'
> python -m venv venv
> venv\Scripts\activate.bat
> pip install -r requirements.txt
```

### macOS
Open a terminal and run the following commands, replacing 'project-root' with the path to the root folder of the project.
```
$ cd 'project-root'
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```
*Note: If you've installed Python 3 using a method other than Homebrew, you might need to type `python` in the second command instead of `python3`.*

### About pip
Versions pip updates frequently, but versions greater than 10.x.x should work with this project.

## Verify Setup

In order to verify that everything is setup correctly, run the following command from the project root.
```
pytest
```

## Previewing Your Work
You can preview your work by running the command `python ssg.py` after the first module.
