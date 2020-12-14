#Function definitions
def findcharsbefore(input, char, start): #Return all text before char, starting at start
    FCBa = start #Set FCB to start at start
    FCBb = "" #Used for output
    while input[FCBa] != char: #While current character != char
        FCBb = FCBb + input[FCBa] #Set FCBb to itself and current character
        FCBa += 1 #Change current character by one
    return [FCBa, FCBb] #Return output

def showoutput(lc, ln, txt): #Display a formatted output
    print("=====") #Beggining of output
    print(lc, "Line #",ln) #Print line info
    print("-----") #Divider
    print(txt) #Print input
    print("=====") #Ending of output

def repeatdata(data, recurse): #Repeat data recurse times
    infiniteI = 1
    infiniteA = ""
    while infiniteI < recurse + 1:
        infiniteA = infiniteA + data
        infiniteI += 1
    return infiniteA

#Program info
launcher = """ \n
<<[ Advent Of Code - Solver Program]>>

Welcome to AOC-Solver! AOC-S is a collection of Proof-Of-Concept code samples for Advent Of Code.
These programs are NOT to be used to complete Advent Of Code. Instead, learn from these code samples.
The code samples for each day can be found in there respective folders. Day 1 was solved without code.
To test these scripts, you will need to copy your puzzle input for each day into a file.
Once you have copied your puzzle input into files, you will need to type the path to those files.
Opening launcher.py (You are here now!) and pressing Enter will open a basic menu. Use help for help.
-----Credits-----
Script: Eli Nero
Advent of code: Eric Wastl
Python: Python Software Foundation
===== Press Enter To Continue ===== """
print(launcher)
input("")

#Clean up and exit
exit()