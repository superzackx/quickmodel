# ⏩ Quick Model ⏩

Quick Model is a simple program which creates tensorflow image classifcation models from the input given. No changing code every 1 model!

## Requirements

1. Python3 and Pip3
2. Git
3. A linux/unix enviorment(or something with sh and chmod)


## Installation

1. Run ```wget https://raw.githubusercontent.com/superzackx/quickmodel/main/scripts/installer.sh``` to download the installer file.(or just download it)
2. Run ```sh installer.sh``` to run the installer.
3. You can now run ```./quickmodel.py``` to check.

### Windows Help

For Windows 10, there are two options.

1. WSL
2. Git Bash

You can run the commands for a Linux installation in these enviorments as they provide the tools needed. 

## Arugements

You can currently enter two arguements:

```-new``` : This creates a new model by taking input from the terminal and then saving it to the config file. <br>
```-noinput```: This directly reads from the config file and generates a model. 

## How it works

The file takes input from the console and saves it to a JSON file called gen.json. This must be created from before. The interactive.py has all the tensorflow code in it which actually runs and creates the model for you. 

## New Features

1. I'll be releasing new scripts each month + packaging the scripts into one Windows 10 executable. 

