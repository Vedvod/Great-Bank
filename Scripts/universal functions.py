#all the universally applicable functions for all my projects
from random import choice, randint
import time
import sys
import math
import datetime as dt
import os

global endbreak
global charbreak
global screensize
global endbreak
global score #game score?
global divi #used for divi
global path_to_directory #path to project folder
divi={"1":"Please divi values", "2":"It would be so great", "3":"Please!"}

'''
#list of functions:
Implemented Working Functions

  1 #t(time_to_sleep_for) - a shorthand for the time.sleep function
        #time_to_sleep_for is the time to sleep for
            #if time_to_sleep_for is not floatable, error message sent and code continues

  2 #r(first_value, second_value=""): - a shorthand/autoselector for random.randint or random.choice.
        #if first_value is a list, run random.choice(first_value) and return value
        #otherwise, sort a and b into ascending order
            #then, run random.randint(first_value, second_value) and return value

  3 #pimport(directory, mode="r") - using path determined from path findind sequence, open a file in the specified mode
        #adds path and directory together
            #then, opens file at path+directory in given mode
                #if mode is r, .read() the file
                #then, return file

  4 #correctcaps(string, modlist=[]): - a function to correct the capitalisation of a given string, typically multi-sentence, use '~' to mark capital letters.
        #adds markers to locate punctuations, '!', '.', and '?'
            #then, it splits on the puncuations, splitting the string into its sentences, if possible
                #for every letter in each sentence
                    #iterates through letters, if a '~', then it is removed, and the next letter is capitalised.
                    #additionally, if the letter is an ' i ', it is capitalised
                        #after iterating through every letter, the process is repeated for other sentences, and they are all combined
                            #finally, the code scans the final string for punctuation markers, and then replaces them with the original punctuations.   

  5 #txtfile(directory) - open a file at directory specified and execute or print per line
        #add path and directory together, then open file at location
            #then, try and execute the line
                #if execepts, run tline(line.strip("\n"))

  6 #clear() - using callibrated screensize variable, clear screen by printing lines
        #get screensize
            #try using screensize, set remainder of screensize divided by 5 as variable remain
                #if excepts (screensize not defined), print error message and set screensize to 64
                #then, try to divide remain by itself, filters out 0
                    #then, save repetitions as the quotient of screensize-remain and 5
                    #if excepts, save repetitions as quotient of screensize and 5
                        #then, print 5 newlines repetitions times, then print the remainder lines
        
  7 #start(name_of_script) - startup sequence
        #print a countup of progress, where each step is randomised until 100%
            #then, print "\n"+name_of_script+" initialised. Enjoy"
                #then, run local(), which bridges universal startup and local

  8 #liststring(label, first_value, separator, list_of_values) - print the contents of a list as a string, in form pre  sep lis1  sep lis2  sep lis3...

  9 #checkinput(input_string, comparison_list) - gets an input using given string, then compares this with a comparison list, if not in list, ask again
        #asks for input for input_string
            #if answer is in comparison_list, return answer
            #otherwise, print fail message and print result of liststring on comparison_list
                #then, run again

 10 #checktype(value) - tries to turn value into float or int 
        #first, tries to turn into float
            #if success, program goes to the last step
            #if exception, tries to turn into an integer
                #if success, program goes to the last step
                #if exception, nothing happens, value is a string
                    #returns valye

 11 #checkintype(input_string, list_of_types) - get an input from a string, if this input's type is in list_of_types, return input, otherwise, ask again
        #run checktype on answer to input_string
            #then, checks if type of answer is in list_of_types
            #while doing this, turn each value in list_of_types into a string
                #if answer in list_of_types, return answer
                #otherwise, print error message and liststring list_of_types
                    #then, run again

 12 #listfile(directory) - replace last value of a list in a given file with given value
        #save pimport(directory, "r") as a variable
            #then, strip the brackets and split on the ", "s
                #then, run checktype on each value in list
                    #then, return this list
    
 13 #listup(value, directory) - removes first value from list and adds given value to last position  
        #save listfile(directory) as a variable
            #remove first value and add [value]
                #run pimport(directory, "w")
                    #write list to file
                        #close file

 14 #listrep(value, directory, position): #uses listfile and then replaces value at given position in list with given value
        #listfile(directory) as variable
            #set position of list as value
                #run pimport(directory, "w")
                    #write list to file
                        #close file

 15 #avefind(directory) - get average of values in file
        #listfile at location
            #add all values and divide by length, then return

 16 #triangle(triangle_size=16, angle1="A", side1="a", angle2="B", side2="b", angle3="C", side3="c") - draws a triange, where the sides and angles are default labelled

 17 #romget(Hindu_Arabic_Numeral) - turn a hindu-arabic numeral into a roman numeral
        #keep subtracting highest possible number until 0 and join letters

 18 #fail() - to be triggered upon fail, prints death and score
        #does stuffs like print score
        #calls tryagain()

 19 #tryagain() - asks player if they should continue
        #if yes, calls local()
        #if no, exits

 20 #div(x) - divides sections
        #use of global dictionary divi
            #divi must be defined locally
        #x is integer, checked for if in divi

 21
    #wipe() - clears the screen 
        #first, searches for the noclear file, which indicates that the function should link to clear()
            #if it finds it, it clears screen with clear()
            #otherwise, it checks if the os.name is posix (unix) or nt (Windows NT 3.1+)
                #if posix, os.system('clear')
                #otherwise, os.system('cls')

 22
    #testforvalue(variable, default_value, replace="no") - checks if the given variable has a value, if not it gives it the specified value
        #first, it tries to get the value
            #if this fails, it sets the variable to the given value
 23
    #fprint(input_string, slow="", words_letters_or_lines="letters", newline="yes") - formatted print, [will have] several parameters that aid in modified printing
        #first, checks if the string is to be printed by words, lines, or letters. Depending on, it splits the string and changes the value of variable 'space'
            #then, it runs testforvalues for charbreak and endbreak
                #it iterates through every element in the list and prints them
                #if slow is True, it waits based on the length of the element.
                #if newline is 'yes', then it prints a newline.

 23b
    #tline (input_string, words_or_letters="letters", newline="yes") - support for new tline (sprint)
        #calls sprint, kept for legacy (old projects) reasons
    #sprint (input_string, words_or_letters="letters", newline="yes") - slow printing calling fprint
        #calls fprint with the parameters given, and with the slow parameter specified as True

 23c
    #tinput(input_string, letters="") - sprints an input, then a blank input on the same line
        #sprint the input_string with no newline
            #then, print a blank input 

 24
    #varcheck(var="") - debug command, prints if a variable is defined, and, if so, value and type of a variable
        #first, if var is predefinined, then it checks it for definition, value, and type
            print(f"""The value of {var} is {eval(var)}, type {str(type(eval(var)))[8:].strip("'>")}
        except:
            print(f"The value of {var} is undefined!")
        return
            
    var=checkintype("What variable will you check? Type 'contine' to exit: ", [str])
    if var=="continue":
        return
    else:
        try:
            print(f"""The value of {var} is {eval(var)}, type {str(type(eval(var)))[8:].strip("'>")}
        except:
            print(f"The value of {var} is undefined!")
    var=""
    print("")
    varcheck()

'***25***'
    #filler(string, space, beforemidafter="after", tline="n"):
    bma=beforemidafter #for easier
    string=str(string) #turn the variable into a string for concat, ects
    extraspace=space-len(string) #determine how much space is left over
    if tline in ["no", "n"]: #if not tlining
        if bma in ["before", "b", "start"]:
            return (extraspace*" "+string)
        elif bma in ["middle", "mid", "m"]:
            return ((extraspace-int((extraspace/2)))*" "+string+int((extraspace/2))*" ")
        elif bma in ["after", "a", "end"]:
            return (string+extraspace*" ")
 
Legacy functions (redundant/no longer in use, but still interesting/stupid)

 L1 #tline (old) - print line and time.sleep charbreak times the length of line

 L2 #start (old) - Old system of start, ask user for directory of main folder
'''



'***1***'
def t(time_to_sleep_for): #shorthand for my sanity
    try:
        time_to_sleep_for=float(time_to_sleep_for) #it just is
        time.sleep(time_to_sleep_for) #sleep
    except: #if fail
        tline("Value can not be converted to floating point!") #fail message

'***2***'
def r(a, b=""): #shorthand for random
  if b=="":
    try:
        return choice(a)
    except:
        return "the value must be a list."
  else:
    try:
        return randint(int(a), int(b))
    except:
        return f"""the first value, a(n) {str(type(a))[8:].strip("'>")} and the second value, a(n) {str(type(b))[8:].strip("'>")} must both be type int!"""

'***3***'
def pimport(directory, mode="r"): #open file in specified mode and return contents if read mode
    m=path_to_directory+directory #path_to_directory is calibrated at start, dire leads from path to file, m is now whole path
    m=open(m, str(mode)) #open file at m in given mode
    if mode=="r": #if read mode, add .read()
        m=m.read()
    return m

'***4***'
def correctcaps(string, modlist=[]): #a function to correct the capitalisation of a given string, typically multi-sentence.
    final="" #define final as a string
    dotsplit=string.lower().replace(".", "*.").replace("?", "^?").replace("!", "@!").replace(" ", "`` ").split(".") #add markers for punctuation, then split on dots
    quesplit=[]
    if "all" in modlist:
        plasplit=[]
        for split in dotsplit:
            split=split.strip().split(" ")[:len(split)]
            plasplit+=split
        dotsplit=plasplit
    for split in dotsplit:
        split=split.strip().split("?")[:len(split)]
        quesplit+=split
    excasplit=[]
    for split in quesplit:
        excasplit+=split.strip().split("!")[:len(split)]
    for split in excasplit:
        if split=="":
            continue
        split=split.strip()
        finsentence=split[0].upper()
        capital=False
        count=1
        for letter in split[1:]:
            count+=1
            if capital:
                letter=letter.upper()
                capital=False

            if letter=="~":
                capital=True
                continue
            try:
                if split[count]+split[count+1]=="i ":
                    capital=True
            except:
                ""
            finsentence+=letter
        final+=finsentence
        if finsentence.endswith("^"):
            final=final.rstrip("^")
            final+="? "
        elif finsentence.endswith("*"):
            final=final.rstrip("*")
            final+=". "
        if finsentence.endswith("``"):
            final=final.rstrip("``")
            final+=" "
        elif finsentence.endswith("@"):
            final=final.rstrip("@")
            final+="! "
    return (final.strip())

'***5***'
def txtfile(directory, modifier_list): #for printing text files line by line at reading pace
    mods=set(modifier_list)
    if len(mods.intersection({"?", "modlist"}))>0:
        sprint("?, modlist - Opens this menu")
        sprint("w, words - Prints by words.")
        sprint("nl, newline - Prints text on a new line.")
    for line in open(path_to_directory+directory): #per line in file given
        try: #try and execute the line
            exec(line)
        except: #if not executable, tline it, and strip the newline character
            if len(mods.intersection({"no-tline", "ntl"}))==0:
                if len(mods.intersection({"w", "words"}))>0:
                    letters="words"
                if len(mods.intersection({"nl", "newline"}))>0:
                    newline="yes"
                tline(line.strip("\n", letters, newline))
            
'***6***'
def clear(number_of_clears=1): #to clear screen without os.system(clr) or whatever
    global screen_height #global variable
    try: #attempt to use screensize, fails if not defined
        screen_height*=number_of_clears
        remain=screen_height%5 #find remainder lines
    except: #if screensize not defined
        print("Screensize is not defined!")
        print("Defaulting to 64 lines.")
        screen_height=64*number_of_clears
        remain=screen_height%5
    try: #if remainder ≠ 0
        (remain)/(remain) #0 not divisible by 0
        reps=int((screen_height-remain)/5) #get nearest (lower) multiple of 5
    except: #if remainder = 0
        reps=int(screen_height/5)
    for i in range(reps): #print screensize lines (5*reps + remain)
        print("", end=5*"\n") #print the multiples
    print("", end=remain*"\n") #print the extra

'***7a**'
def calibsize(): #function to get user to calibrate their screen size for later usage
    if checkinput("Do you want to quick calibrate the screen size? ") in ["y", "yes"]: #negative response
        chose_size=checkinput("Choose a screen default from 'small', 'medium', and 'large': ", ["small", "s", "medium", "m", "large", "l"])
        global screen_height
        screen_height=64
        wipe()
        if chose_size in ["small", "s"]:
            screen_height=37 #default height
            screen_width=32*4 #default width
        elif chose_size in ["medium", "m"]:
            screen_height=44 #default height
            screen_width=40*4 #default width
        elif chose_size in ["large", "l"]:
            screen_height=52 #default height
            screen_width=48*4 #default width
        print("0") #reference
        for i in range(screen_height, 4, -1): #script to callibrate screensize
            print("") #space on screen
        for i in range(screen_width+1):
            print("0", end="") #print a bunch of 0s
        print("\nAdjust the screen height until the top zero is fully on the screen.")
        print("Then, adjust the screen width until all the bottom zeroes are on one line.")
        input('Press Enter when done, or type "cancel" to pick another size')
        return screen_width, screen_height #end
    for i in range(91, 0, -1): #script to callibrate screensize
        print(i) #countdown on screen
    global charbreak #
    olc=charbreak #preserve
    charbreak=0.001
    global endbreak
    ole=endbreak
    endbreak=0.09
    while True:
        screen_height=int(checkintype("What is the largest number on the screen right now? Part of the number showing is counted. ", [int], "", False))+1 #ask for calibration
        if screen_height<32: #height minimum
            sprint("This is too small a size, please adjust your window until at least 32 is visible when the line above is the bottom of the window. ") #retry message
            continue
        tline("Your screen height has been callibrated to "+str(screen_height-1)+" lines. Please do not change the screen size or text size unless prompted.") #confirm message
        break
    wipe() #clear
    for i in range(1, 80):
        print(filler(i, 4, "before"), end="")
    print("")
    while True:
        screen_width=int(checkintype("What is the last number on the first line? If part of the number shows, or the number is immediately on the next line, add 0.5 to the previous number. ", [int, float])*4) #ask for calibration
        if screen_width/4<32:
            sprint("This is too small a size. Please adjust your window width until at a width of at least 32.")
        else:
            sprint("Your screen width has been callibrated to "+str(screen_width)+" spaces. Please do not change the screen size or text size unless prompted.") #confirm message
            break
    charbreak=olc
    endbreak=ole
    return screen_width, screen_height

'***7b**'
def start(name_of_script="A nameless script, which you forgot to enter a name value for, has been", screen_w=0, screen_h=0): #pre-script
    global screen_width
    global screen_size
    if screen_w!=0 and screen_h!=0:
       screen_width, screen_height=screen_w, screen_h
    else:
        screen_width, screen_height=calibsize()
    score=0 #idk
    wipe()
    print("Loading...") #of course
    i=0 #to set i as 0
    while i<100: #while "percent loaded" less than 100
        m=r(1, 63) #choose random number between 1 and 37 to be "loaded" percentage
        if i+m>=100: #if "loaded" percent plus already loaded is over 100
            m=100-i #m becomes value required to reach 100
            i=100 #i becomes 100
        else: #if m plus i is not greater/equal to 100
            i+=m #add m to i
        t(m/100) #wait a for a time that is proportional to m
        print(str(i)+"%") #print percentage loaded
    tline("\n"+str(name_of_script)+" initialised. Enjoy!\n\n") #loaded message
    local() #call locally defined function that acts as an intepreter between universal and local functions

'***8***'
def liststring(label, first_value, separator, list_of_values): #label: pre  sep lis1  sep lis2  sep lis3...
    return str(label)+": "+str(first_value)+str(separator).join(list_of_values) #return format

'***9***'
def checkinput(input_string, comparison_list=["y", "yes", "n", "no"], modifier_list=[""]): #asks for input until given input is in given list of accepted
    mods=set(modifier_list)
    if "modlist" in modifier_list:
        sprint("modlist - Opens this menu")
        sprint("pc, preserve, preservecaps - Preserves Capitals")
        sprint("db, dev, debug, developer - Activates Debug Mode")
    inn=tinput(str(input_string)) #input of given string
    innn=inn
    if len(mods.intersection({"pc", "preserve", "preservecaps"}))==0:
        innn=innn.lower()
    if len(mods.intersection({"db", "debug", "dev", "developer"}))>0:
        print(innn)
        print(innn in comparison_list)
    if innn in comparison_list: #if input is in list given, then return it
        return innn #return input
    else: #if input is not in given list
        charbreak=0.01
        endbreak=0.05
        tline(str(inn)+" is not a valid response.") #print that it is not in list
        tline(liststring("Valid","",", ",comparison_list)) #print what's valid
        return checkinput(input_string, comparison_list) #run again

'***10**'
def checktype(value): #makes input type into int or float if possible
    try:
        if float(value)==float(int(value)):
            value=int(value)
    except:
        try:
            value=float(value)
        except: #if integer is not a float (is a string)
            '' #do nothing, it's a string
    return value

'***11**'           
def checkintype(input_string, list_of_types, letter="", slow=True): #repeat until an input is of required type
    stringlist=[]
    if slow==True:
        iner=checktype(tinput(input_string, letter)) #make iner a float or int if possible
    else:
        iner=checktype(input(input_string))
    for value in list_of_types:
        if type(iner)==value: #if type of input matches requirement
            return iner #return and end strings
        stringlist.append(str(value).strip("<cla>").replace("s", "", 2).replace(" ", "").replace("'", "")) #turn types into
    if float in list_of_types and int not in list_of_types:
        if type(iner)==int:
            return float(iner)
    print(str(type(iner)).strip("<cla>").replace("s", "", 2).replace(" ", "").replace("'", "")+" is incorrect type!") #print fail
    tline(liststring("Valid","",", ",stringlist)) #fail
    return checkintype(input_string, list_of_types, letter, slow) #run again

'***12**'
def listfile(directory): #replace last value of a list in a given file with given value
    a=pimport(directory, "r") #open file in read (this also adds .read() to it due to pimport functionality)
    a=(a.strip("][")).split(", ") #turn list string into a list of the values in it
    x=0 #count for position
    for e in a:
        a[x]=checktype(e) #turn each value into an integer or float of that value if possible
        x+=1 #next position
    return a

'***13**'
def listup(value, directory): #removes first value from list and adds given value to last position  
    a=listfile(directory) #run listfile and get list from file
    a=str(a[1:]+[value]) #make into string with first value removed and given value added to end
    b=pimport(directory, "w") #open file in write
    b.write(a) #write to file
    b.close() #close

'***14**'   
def listrep(value, directory, position): #uses listfile and then replaces value at given position in list with given value
    a=listfile(directory) #run
    a[position-1]=value #value to position specified (minus one to match counting from 0)
    a=str(a) #turn list into string of list
    b=pimport(directory, "w") #open file in write
    b.write(a) #write to file
    b.close() #close

'***15**'
def avefind(directory): #get the average of values given
    scorelist=listfile(directory) #open scores file
    total=0
    for a in scorelist: #for each score
        total+=int(a) #add the score to sjka
    total=total/len(scorelist) #divide sum of all scores by number of scores
    return total

'***16**'
def triangle(triangle_size=16, anglea="a", angleb="b", anglec="c", sideA="A", sideB="B", sideC="C"):
    def function(variable, default):
        if not variable==default:
            global vare
            exec("global vare\nvare=' which is '+variable+', '")
            if default.islower():
                vare=","+vare
            return vare
        else:
            if default=="C":
                return ""
            else:
                return " "
    anglea=str(anglea)  
    A_value=function(anglea, "a")

    sideA=str(sideA)
    a_value=function(sideA, "A")

    angleb=str(angleb)
    B_value=function(angleb, "b")


    sideB=str(sideB)
    b_value=function(sideB, "B")

    anglec=str(anglec)
    C_value=function(anglec, "c")

    sideC=str(sideC)
    c_value=function(sideC, "C")
    
    if triangle_size>10:
        x=4
    else:
        x=3
    if len(anglea)%2==0:
        anglea=anglea[:int(len(anglea)/2)]+" "+anglea[int(len(anglea)/2):]
    if len(sideA)%2==0:
        sideA=sideA[:int(len(sideA)/2)]+" "+sideA[int(len(sideA)/2):]
    print((triangle_size)*" "+"A")
    for i in range(1, triangle_size):
        a="     /"
        b=chr(92)
        c=(i*2-1)*" "
        if i==4:
            c=(" "*int((7-len(anglea))/2))+anglea+(" "*int((7-len(anglea))/2))
        if i==int(triangle_size/2):
            a, b=((5-x)*" ")+sideC+(x-len(sideC))*" "+"/", chr(92)+((4-x)*" ")+(x-len(sideB))*" "+sideB
        if triangle_size-i==4:
            a="    /"
        if triangle_size-i==3:
            a="   /"
        if triangle_size-i==2:
            a="  /"
            c="    "+angleb+((2*(i-4)-1-len(angleb)-len(anglec))*" ")+anglec+"    "
        if triangle_size-1==i:
            a=" /"
        print(((triangle_size-i-5)*" ")+a+c+b) 
    print("B"+((2*i+1)*"-"+"C")) 
    print((1+i-(int(len(sideA)/2)))*" "+sideA)
    print("*not to scale!")
    print("Observe here triangle ABC, where angle a"+A_value+"is opposite side A,"+a_value+"angle b"+B_value+"is opposite side B,"+b_value+"and angle c"+C_value+"is opposite side C"+c_value+".\n")
    t(3)  

'***17**'
def romget(Hindu_Arabic_Numeral=509): #romget(hinar)
    hinar=Hindu_Arabic_Numeral
        #hinar is the hindu-arabic input
        #translates to roman, then returns roman
    b=hinar #save a
    rom=[] #empty list to store
    while hinar>0: #until all a translated
        if hinar-1000==abs(hinar-1000): #if over/equal 1000
            hinar-=1000 #subtract
            rom.append("M") #add letter
        elif hinar-900==abs(hinar-900): #if over/equal 900
            hinar-=900 #subtract
            rom.append("CM") #add the letter combo
        elif hinar-500==abs(hinar-500): #if over/equal 500
            hinar-=500 #subtract
            rom.append("D") #add letter
        elif hinar-400==abs(hinar-400): #if over/equal 400
            hinar-=400 #subtract
            rom.append("CD") #add the letter combo
        elif hinar-100==abs(hinar-100): #if over/equal 100
            hinar-=100 #subtract
            rom.append("C") #add letter
        elif hinar-90==abs(hinar-90): #if over/equal 90
            hinar-=90 #subtract
            rom.append("XC") #add the letter combo
        elif hinar-50==abs(hinar-50): #if over/equal 50
            hinar-=50 #subtract
            rom.append("L") #add letter
        elif hinar-40==abs(hinar-40): #if over/equal 40
            hinar-=40 #subtract
            rom.append("XL") #add the letter combo
        elif hinar-10==abs(hinar-10): #if over/equal 10
            hinar-=10 #subtract
            rom.append("X") #add letter
        elif hinar-9==abs(hinar-9): #if over/equal 9
            hinar-=9 #subtract
            rom.append("IX") #add the letter combo
        elif hinar-5==abs(hinar-5): #if over/equal 5
            hinar-=5 #subtract
            rom.append("V") #add letter
        elif hinar-4==abs(hinar-4): #if over/equal 4
            hinar-=4 #subtract
            rom.append("IV") #add the letter combo
        elif hinar-1==abs(hinar-1): #if over/equal 1
            hinar-=1 #subtract
            rom.append("I") #add letter
    return "".join(rom) #join all the letters into a string

'***18**'
def fail(): #on death trigger
    tline("You have died, your score was "+str(score)+".")
    tryagain()

'***19**'
def tryagain(): #ask if again
    againtry=checkinput("try again? (y or n): ", ["y", "n"])
    if againtry == "y":
        local()
    elif againtry == "n":
        print("That's a shame, persistence is key to victory in games (and in real life)")
        sys.exit("Please try again soon!")
    else:
        tline("Please answer with a y or an n")
        tryagain()
        
'***20**'       
def div(number): #divider
    x=number
    x=str(x)
    try:
        nam=divi[x]
    except:
        nam="Not Found!"
    print("\n\n**********************************************************************************\nChapter "+str(x)+": "+nam+"\n")

'***21**'
def wipe():
    try:
        a=open("C:/noclear/noclear.txt")
        a.close()
        clear()
    except:
        if os.name != 'posix':
            # Else Operating System is Windows (os.name = nt)
            _ = os.system('cls')
        # Check if Operating System is Mac and Linux or Windows
        else:
            _ = os.system('clear')

'***22**'
def testforvalue(variable, default_value, replace="no"):
    default_value=str(default_value)
    if replace=="rep":
        exec(f"global {variable}\n{variable}={str(default_value)}")
        return variable
    else:
        exec("global "+variable+"\ntry:\n "+variable+"\nexcept:\n "+variable+"="+str(default_value))

'***23a**'
def fprint(input_string, slow="", words_letters_or_lines="letters", newline="yes"):
    space=""
    if words_letters_or_lines.lower() in ["words", "w"]:
        input_string=input_string.split(" ")
        space=" "
    elif words_letters_or_lines.lower() in ["lines", "l"]:
        input_string=input_string.split("\n")
    testforvalue("charbreak", 0.03)
    testforvalue("endbreak", 0.8)
    slen=len(input_string)
    for i in range(0, slen):
        if words_letters_or_lines.lower() in ["lines", "l"]:
            space="\n"
        print(input_string[i], end=space)
        if input_string[i].endswith("\n"):
            if slow:
                t(endbreak)
        else:
            if slow:
                t(len(input_string[i])*charbreak)
    if slow:
        t(endbreak)
    else:
        print(endbreak)
    if newline=="yes":
        print("")

'***23b*'
def tline (input_string, words_or_letters="letters", newline="yes"):
    sprint(input_string, words_or_letters, newline)

def sprint (input_string, words_or_letters="letters", newline="yes"):
    fprint(input_string, True, words_or_letters, newline)

'***23l**'
def tinput(input_string, letters=""):
    sprint(input_string, letters, "no")
    return input("")

'***24***'
def varcheck(var=""):
    if var!="":
        try:
            print(f"""The value of {var} is {eval(var)}, type {str(type(eval(var))).strip("<cla>").replace("s", "", 2).replace(" ", "").replace("'", "")}.""")
        except:
            print(f"The value of {var} is undefined!")
        return
            
    var=checkintype("What variable will you check? ", [str])
    if var=="continue":
        return
    else:
        try:
            print(f"""The value of {var} is {eval(var)}, type {str(type(eval(var))).strip("<cla>").replace("s", "", 2).replace(" ", "").replace("'", "")}.""")
        except:
            print(f"The value of {var} is undefined!")
    var=""
    print("")
    varcheck()

'***25***'
def filler(string, space, beforemidafter="after", tline="n"):
    bma=beforemidafter #for easier
    string=str(string) #turn the variable into a string for concat, ects
    extraspace=space-len(string) #determine how much space is left over
    if tline in ["no", "n"]: #if not tlining
        if bma in ["before", "b", "start"]:
            return (extraspace*" "+string)
        elif bma in ["middle", "mid", "m"]:
            return ((extraspace-int((extraspace/2)))*" "+string+int((extraspace/2))*" ")
        elif bma in ["after", "a", "end"]:
            return (string+extraspace*" ")

'''
Legacy Functions (No longer in use)

'***L1***'
def tline(line): #prints a line and then waits for reader to read line (based on length of line)
    testforvalue("charbreak", 0.25)
    print(line) #print the line
    t(charbreak*len(line)) #wait for time based on length of line

***L2***
############################################################################
#import modules
import os 
import time

#set variables
z=[]
zel=1
dic={}
y=0
zel=0
hay=[]
#get file path
b=__file__ + "\n"

#translate windows to macOS/linux if applicable, by changing character 92 (\) to /
    #then, split on the /
a=(b.replace(chr(92),"/")).split("/")
print("\n")

for w in a:
    if y==0: #ignore first, which is a "" or D:
        y=1
        z.append("")
        continue
    z.append(w) #adds step to path
    zel+=1
    hay.append(str(zel))
    dic[str(zel)]="/".join(z) #stores path in dictionary

def findpath(): #path selection
    global pat #
    for a in dic: #for each step in path, print incrementally
        time.sleep(0.125) #small break in between each
        print(a+" "+dic[a])
    time.sleep(0.5)
    e=input("Which line leads to the project folder? ").lower() #ask user for path
    try:
        pat=dic[e] #works if user input is dictionary key
        cour() #confirmation function
    except:
        print(str(e)+" is not a valid response!\nValid: "+(", ".join(hay))+"\n\n") #occurs if user input not dictionary key
        findpath() #do again
    
def cour():
    course=input("Are you sure the folder is at "+pat+"? ") #ask for confirm
    if course in ["yes", "y","no", "n", "nah"]: #if input valid
        if course in ["yes", "y"]: #if input positive
            
            time.sleep(0.2)
            print("testing path")
            time.sleep(0.5)
            try:
                exec(open(pat+"/universal functions.py").read()) #opens universal functions
            except: #if can not open universal functions file
                print("Incorrect path!\n") #fail message
                time.sleep(1)
                findpath()
                
        else: #if input negative
            print("\n") 
            findpath() #restart path selection
    else: #if input invalid
        print("Not a valid response!") #prints fail message
        cour() #restart confirmation

findpath() #calls

path=pat #sets global path file to the user-chosen path
exec(open(pat+"/universal functions.py", "r").read())
tline(pat+" validated.", "") #confirmation message
############################################################################

#All above uses os module to locate the project folder using user input
    #It then opens universal functions using this path
'''

#L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L L 
