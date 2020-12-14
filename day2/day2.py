#Define variables
l = 0 #Line counter
n = 0 #Output
f = 0 #False Output
pn = 0 #Part 2 Output
pf = 0 #Part 2 False Output

#Get file
filename = input("Input full path to file, then press return. \n") #Prompt for file path
try:
    y = open(filename) #File
except: #Handle error
    print("Could not access file. Please check that your input is a full path to a valid file.")
    exit()

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

#Main Code
for x in y:
    l += 1 #Increment line number

    if l == 1001: #If the script has already searched the whole file
        break

    #Find values
    a = findcharsbefore(x, ":", 0) #Everything before the : symbol
    b1 = findcharsbefore(a[1], "-", 0) #Number before the -
    b2 = findcharsbefore(a[1], " ", b1[0]+1) #Number after the -
    b = [int(b1[1]), int(b2[1])] #b1 and b2 in one easy variable
    c = x[a[0]-1] #Letter
    d = findcharsbefore(x, "\n", a[0]+2) #Everything after the : symbol

    #Proccess Output
    tt = """ Letter is {0}
    {2}: {3}
    {4}: {5}
    {6}: {7}
    {8}: {9}
    String is {1} """
    t = tt.format(c, d, "a", a, "b1", b1, "b2", b2, "b", b) #Format skeleton with values
    print("\n")
    showoutput(x,l,t)

    #Check conditions (Part 1)
    i = 0 #Counter
    ni = 0 #How many times a character = letter
    for i in d[1]: #Iterate through characters in d (the text after : in x)
        if i == c: #If the current character = letter
            ni += 1
    if ni >= b[0] and ni <= b[1]: #If ni is between b1 and b2
        n += 1
    else:
        f += 1
    print("ni is", ni)
    print("n is currently", n)

    #Check conditions (Part 2)
    pni = 0
    if str(d[1])[b[0]-1] == c:
        if str(d[1])[b[1]-1] != c:
            pni += 1
    else:
        if str(d[1])[b[1]-1] == c:
            pni += 1
    if pni > 1 or pni < 1:
        print(pni, "occurrences of", c, "found, wanted 1!")
        pf += 1
    else:
        print("Found", pni, "occurrences of", c, "!")
        pn += 1

#Print data and exit
exittext = """ \n
<<[Done looping over file!]>>

-----Stats-----
Worked on {0} lines
Found {1} true lines (Part 1)
Found {2} false lines (Part 1)
Found {3} true lines (Part 2)
Found {4} false lines (Part 2)
-----Credits-----
Script: Eli Nero
Advent of code: Eric Wastl
Python: Python Software Foundation
=====GoodBye!===== """

showexit = exittext.format(l, n, f, pn, pf) #Fill in stats
print(showexit)

#Clean up and exit
y.close()
exit()