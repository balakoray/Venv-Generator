# Venv Generator
#
# Version: 1.0
# Coded by Koray Bala - https://github.com/balakoray
#
# Venv Generator is an automated Python 3 virtual environment
# generator that asks for Venv name and creates the virtual environment.
#
# In case of missing path, it creates the Development folder in Desktop
# and creates additional development folders as the initial setup.

import os
import sys
import time
import re

# Base path for looking up Development Environment
devPathLookup = "~/Desktop/Development/"
pythonDevPathLookup = devPathLookup + "Python/"
venvsPathLookup = pythonDevPathLookup + "virtualEnvs/"

def PathCheck(pathStr):
    return os.path.isdir(os.path.expanduser(pathStr))

PathCheck(devPathLookup)

# Countdown for quiting.
def countDown(number):

    print("Venv Generator will quit in {} seconds".format(str(number)))

    while number != 0:
        print(str(number))
        time.sleep(1)
        number = number - 1

def decisionCheck(childFolder, parentFolder, pathStr, commandEntry):
    print("{child} folder cannot be found on {parent}.".format(child = childFolder, parent = parentFolder))
    
    qText = "Would you like Venv-Generator to Create {child} folder as following path?\n\n".format(child = childFolder)
    qQuestion = "\n\n[Yes/No]: "
        
    while True:
        # Input decision
        decision = input(qText + "{pathFolder}".format(pathFolder = pathStr) + qQuestion)

        if decision in ["Yes", "yes", "YES", "y", "Y"]:
            os.system(commandEntry)
            break

        elif decision in ["No", "no", "NO", "n", "N"]:
            countDown(3)
            sys.exit()

        else:
            print("You entered incorrect value. Please try again.")

def PathControl(pathStr, cmdType):

    directory = pathStr.split("/")
    childFolder = directory[len(directory)-2]
    parentFolder = directory[len(directory)-3]
    
    # Check if path exists
    # If it doesn't
    if PathCheck(pathStr) == False:

        if cmdType == "Folder":
            commandEntry = "mkdir {}".format(pathStr)

        elif cmdType == "venv":
            commandEntry = "python3 -m venv {}".format(pathStr)

        # Ask for decision and then run the command for creating directory
        decisionCheck(childFolder,parentFolder,pathStr,commandEntry)

    # If exists
    else:
        print("{child} folder found on {parent}".format(child = childFolder, parent = parentFolder))
        print("Skipping {child} folder's creation.".format(child = childFolder))

# Check Dev Folder
PathControl(devPathLookup, "Folder")

# Check Python Folder
PathControl(pythonDevPathLookup, "Folder")

# Check Venvs Folder
PathControl(venvsPathLookup, "Folder")

# venv Path
print("\nVenv Generator will create a Virtual Environment with your desired name.")

while True:
    venvPathInput = str(input("\n\nPlease enter name for your virtual envrionment: "))
    
    if re.match("^[A-Za-z0-9_-]*$", venvPathInput):
        venvPath = venvsPathLookup + venvPathInput + "/"
        break
    else:
        print("You entered invalid folder name. Please only use letters, numbers, dash and underscore")

# Check Python Folder
PathControl(venvPath, "venv")

print("Success!")
countDown(3)