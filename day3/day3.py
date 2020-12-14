#Define variables
l = 1 #Line counter
i = 1 #Character Counter
n = 0 #Output
f = 0 #False Output

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
z = y.readlines() #Easy access to lines
ll = len(z[0]) - 1 #Length of lines
yl = len(z) #Number of lines in file

print("ll is", ll)
print("yl is", yl)

while l <= yl:
    #Increment
    i += 3 #Three characters to the right
    l += 1 #One line down
    b = int(i/ll) #Times i passes edge of line

    #Make i usable
    if i > ll: #If i past the edge of line
        c = i - (ll * b) #Set c to i minus number of chars past EOL
        if c == 0: #When c == 0 problem (_____) is encountered, fix problem.
            c = ll #Put c back at EOL
    else: #Script has not run much, so i is smaller than 31
        c = i #Set c to i

    #Find Values
    if l == yl: #If on final line
        pass
    else:
        x = z[l-1] #Get line content with y.readlines()
    x = z[l-1] #Get line content with y.readlines()
    a = x[c-1] #Get char c of line

    #Check conditions
    if a == "#": #If tree
        n += 1
        print("Is tree!")
    if a == ".": #If not tree
        f += 1
        print("Is not tree!")

    #Proccess Output
    tt = """ {0}
    Current char (i) is {1}
    Current line (l) is {2}
    Char i of line (a) is {3}
    Times current char passes line is {4}
    Current char but wrapped (c) is {5} """
    t = tt.format("Hello!", i, l, a, b, c) #Format skeleton with values
    print("\n")
    showoutput(x, l, t)

#Print data and exit
exittext = """ \n
<<[Done looping over file!]>>

-----Stats-----
Worked on {0} lines
Found {1} spaces with trees (Part 1)
Found {2} spaces without trees (Part 1)
-----Credits-----
Script: Eli Nero
Advent of code: Eric Wastl
Python: Python Software Foundation
=====GoodBye!===== """

showexit = exittext.format(l, n, f) #Fill in stats
print(showexit)

#Clean up and exit
y.close()
exit()