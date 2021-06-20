import os  # imports os module
from os import get_terminal_size
import sys  # imports sys module
import time  # imports time module
from datetime import datetime as dm

######################################################################### Code for Universal Functions
try: #when a function is called and it is
     #not defined inside the code
     #then this program will execute the
     #findpath() function

    exec(findpath()) #This executes find path

except: #if an error is thrown when the findpath()
        #function is trying to be executed
        #then the code under the except
        #statement will run

    def findpath(): #define the findpath() function

        #set variables
        segment=[] #set segment to a list
        count=0 #sets count to 0
        dic={} #set dic to a dictionary
        y=0 #sets y to comment
        filepath=__file__ + "check universal functions" #get file path



        modfilepath=(filepath.replace(chr(92),"/")).split("/") #translate windows to
                                                               #macOS/linux if applicable,
                                                               #by changing character 92 (\) to /
                                                               #then, split on the /

        for step in modfilepath: #increment directory to locate
                                 # which one universal functions is in

            if count==0: #ignore first, which
                         # is a "" or a "D:"

                count=1 #stop ignoring

                segment.append("") #adds an extra / to the start of the path
                
                continue #if count does not
                         #equal 1
                         #then the rest of
                         #the code will be
                         #skipped

            segment.append(step) #Each step is the next
                                 #/ in the path to the
                                 #script
                                 #These parts iterated and
                                 #appended to the list 'segment'

            try: #attempts to find and run
                 #universal functions in
                 #the given directory

                exec(open(str("/".join(segment)+"/universal functions.py")).read()) #tries to open
                                                                               #universal functions

                global path_to_directory #sets global path file
                                         #to the user-chosen path

                path_to_directory="/".join(segment) #joins every element of segment
                                                    #which is a list with a / character
                                                    #and this creates a path to main
                                                    #directory


                break #if the universal functions file
                      # is found then the loop will end

            except: #if it is not found the the
                    #code will continue inside the loop

                continue #this makes the code continue
                         #the next try and except
                         #statement

        try: #if the path to directory is not defined
             #then an exception will be thrown by python
             #when this exception is thrown then the
             #code under the except statement will run

            open(path_to_directory+"/universal functions.py", "r").read() #opens it

            return open(path_to_directory+"/universal functions.py", "r").read() #return the opened file,
                                                                                 #since function is executed
        except: #This is the code which will run when
                #either universal functions does not
                #exist or cannot be run
            sys.exit("It seems that the universal functions file cannot run!") #this exits the code and displays
                                                                               #"It seems that the universal
                                                                               #functions file cannot run!"#defines function to find path#defines function to find path

    exec(findpath()) #if the universal functions file
                     #has been found then the findpath()
                     #function will be executed

#All above uses os module to locate
#the project folder using user input
#It then opens universal functions
#using this path
global charbreak #makes charbreak global
global endbreak  #makes endbreak global
charbreak=0.025

###########################################################################



############################################################################ Class for Balance
userlist = open("users.txt") #open the user.txt file

userdic = {} #creates a dictionary for user name and password

usernum = {} #and a dictionary for username and user number

for combo in userlist: #combo is user name + pin
  try: #tries the code underneath

    name, pin, nextmark = combo.strip("\n").split(",") #split username and pin
                                                       #on the basis of a comma
    userdic[name] = pin.strip() #removes spaves the pin

    nextmark=int(nextmark) #next mark is the
                           #variable for the next id

    usernum[name] = nextmark #Gives user a user
                             #number

    nextmark+=1 #Makes it so that the next
                #user registered will obtain
                #the next number

  except: #If the code under the try
          #statement throws an error
          #or exception the code
          #below will run This 
          #except statement catches
          #all the lines in the users.txt
          #file which are not user
          #credentials

   "" #Except must run something
      #as such to avoid an error
      #an empty string must be
      #run which will not effect
      #the rest of the code

charbreak=0.025 #set charbreak for slow
endbreak=0.065 #set endbreak for slow

def getbal(marker, mode="read", value=0): #Defines the function
                                          #getbal - which means
                                          #get balance

                                          #It sets the parameters:
                                          #marker, which will be equal to
                                          #balance=getbal(usernum[user])
                                          #the index inputed later on
                                          #This index will be from the
                                          #dictionary usernum and will
                                          #be equal to the user id
                                          #mode = "read" is the parameter
                                          #which will specify which
                                          #mode to open the balance in
                                          #value is a parameter which will
                                          #be the value of the balance
                                          #which will be overwritten

                                          #To use the function in combination
                                          #with these parameters then it
                                          #will look like - getbal(2, "write", 5000)
                                          #The first argument in the parameter
                                          #makes marker = 2
                                          #the second argument makes
                                          #the mode = "write"
                                          #the third argument overwrites the
                                          #balance to 5000



    balances=open("balances.txt") #Opens the balances.txt file

    if mode in ["r", "read"]: #Mode is thte optional parameter
                              #for the open() function.
                              #If no parameter is set then it
                              #will default to open and
                              #read the file

        for line in balances: #Balanes is balances.txt file
                              #check through every line to
                              #see if it has an
                              #actual balance attatched to it

            try: #When there is a balance
                 #attatched to the line the
                 #code below the try
                 #statement will run as
                 #there will no error
                 #or exception

                line=line.split(": ")[1] #this will split balance
                                         #and user idfrom
                                         #the Username in the
                                         #balances.txt file on the
                                         #basis of the colon

            except: #if there is no balance
                    #on that line of the
                    #balances.txt file then
                    #an exception or error
                    #will be thrown
                    #When this happens the
                    #code below the except
                    #statement will run

                "" #Except must run something
                   #as such to avoid an error
                   #an empty string must be
                   #run which will not effect
                   #the rest of the code

            line=line.strip("\n") #gets rid of the new
                                  #line character - \n -
                                  #from the lines
                                  #This is neccesary as in
                                  #the following code the user
                                  #id and balance will be
                                  #split and put into a list as
                                  #such the \n which is
                                  #attached to the balance
                                  #must be removed
                                  #Because we want the balance
                                  #to returned as an integer the
                                  #/n must be removed in this
                                  #process otherwise an exception
                                  #will be thrown and the code
                                  #will not run

            number, amount=line.split(",") #This split the user id and
                                           #the balance on the basis
                                           #of , and seperates them
                                           #into two different lists

            number=int(number) #This converts the user
                               #id into an integer

            print(int(number), int(marker))
            if int(number)==int(marker): #This checks if the user id is equal
                                         #to the marker parameter which is
                                         #defined in the function parameters
                                         #above
                amount=amount.replace(".00", "") #clear a double decimal if existent
                return int(amount)  #When the two variables are
                                    #equal the coresponding balance
                                    #will be returned
                                    #the amount variable is the balance
        
    elif mode in ["w", "write"]: #This checks if the getbal() fuctions
                                 #mode parameter has been set to
                                 #"w" or "write"
                                 #When this is the case the code below will run
                                 #This will be neccessary when we set the mode
                                 #parameter for the getbal() function inside
                                 #the definition of the deposit() function
                                 #def deposid():
                                 #........
                                 #getbal(usernum[user], "write", balance+int(choice))

        baldic={} #Creates a dictionary called
                  #baldic which means balance
                  #dictionary

        for line in balances: #This iterates throgh the
                              #lines in the balances.txt
                              #file

            try: #This runs the code below when there
                 #are no exceptions or error thrown

                line=line.split(": ")[1] #This splits the line on the
                                         #basis of ": " and takes the values
                                         #and ingnore the ones on the left

            except: #The code indented inside
                    #the except statement will run
                    #if an exception or error is
                    #thrown when the code
                    #indented inside the try
                    #statement is run

                "" #The except statement
                   #must run something
                   #as such to avoid an error
                   #an empty string must be
                   #run which will not effect
                   #the rest of the code

            line=line.strip("\n") #This removes the new line character
                                  #from the end of the balance
                                  #The balance will be assigned to the
                                  #varible amount and turn into int(amount)
                                  #later on as such this code is neccessary

            try: #This runs the code below when there
                 #are no exceptions or error thrown

                number, amount=line.split(",") #This splits line on the basis of ","
                                               #and assignes the two lists to
                                               #the variables number and amount

                if int(number)==int(marker): #This checks if the user id obtained
                                             #from the balances.txt file is equal
                                             #to the marker parameter set when
                                             #calling the function

                    amount=value #sets the amount variable
                                 #to the value variable
                    try: #attempt this
                        while len(amount.split(".")[1])!=2: #check if there is a decimal, and if it is two zeroes
                            amount=str(amount)+"0" #until it is two zeroes, add zeroes
                    except: #if there is no decimal
                        amount=str(amount)+".00" #add the end
                baldic[number]=amount #adds the variable number:amount
                                      #to the balance dictionary
                                      #These two variables correspond
                                      #to user id:balance

            except: #The code indented inside
                    #the except statement will run
                    #if an exception or error is
                    #thrown when the code
                    #indented inside the try
                    #statement is run

                "" #The except statement
                   #must run something
                   #as such to avoid an error
                   #an empty string must be
                   #run which will not effect
                   #the rest of the code

        file=open("balances.txt", "w") #opens the balances.txt
                                       #file in write mode

        file.write("") #make the entire file
                       #an empty string

        file.close() #closes the file
                     #so that the file
                     #can save and be
                     #accessed by other
                     #users

        file=open("balances.txt", "a") #opens the balances.txt
                                       #file in append mode

        for numb in baldic: #Iterates through the keys:value
                            #pairs inside the baldic dictionary

            for elem in usernum: #iterate through the key:value pairs
                                 #inside the dictionary usernum which
                                 #contains name:user id

                if int(usernum[elem])==int(numb): #Checks if the value of the user
                                                  #id obtained from the usernum
                                                  #dictionary is equal to the
                                                  #value obtained from the
                                                  #baldic dictionary

                    break #Ends the loop

            file.write(f"{correctcaps(elem, ['all'])}: {numb},{baldic[numb]}\n")#Corects caps is a function which
                                                                                 #capitalises the first character
                                                                                 #in a string

                                                                                 #This writes username and the list ['all']
                                                                                 # and the user id and the balance to the
                                                                                 #file with a colon in between them
                                                                                 #a new line character - \n - also
                                                                                 #added at the end


                                                                                 #This is so that when in the above code the
                                                                                 #line is split on the basis of the colon
                                                                                 #it will not throw an exception or error

                                                                                 #The new line character is added so that
                                                                                 #the text is not all on the same line

                                                                                 #The {} apply to the syntax of a f string
                                                                                 #essentially everything inside the curly
                                                                                 #brackets now becomes a string



        file.close() #closes the file
                     #so that the file
                     #can save and be
                     #accessed by other
                     #users
#############################################################################




############################################################################# Transactions
        
def deposit(user): #a function for the user to interact with and add money to their account
    balance=getbal(usernum[user]) #find the amount of money in their account
    wipe() #clear screen to allow new content
    logo(2) #display logo in corner
    choice=tinput(f'\nHello, {correctcaps(user, ["all"])}. How much would you like to deposit? Type "cancel" to cancel. $').lower() #ask the user to submit deposit amount
    if choice=="cancel": #if the user enters the cancel input
        menu(user) #return to menu
        return #end
    choice=checktype(choice) #convert choice to the highest type possibe (float > int > str)
    if type(choice)==str: #if the input type entered is invalid and not "cancel"
        sprint("String input is not valid! An integer or float input is required. Please try again.") #tell the user that they have entered invalid input
        return deposit(user) #ask again
    if not choice%5 == 0 or not int(choice)>0: #if they have entered a float or integer, but it is not a valid cash combination
        sprint("This amount is invalid! Only combinations of cash notes can be accepted! Please try again.") #tell the user that they have entered invalid input
        return deposit(user) #ask again
    elif choice%5==0: #if the cash amount is a valid amount, continue on
        choice=int(str(choice).replace(".0", "")) #remove the decimal from the end
        getbal(usernum[user], "write", balance+int(choice)) #write the new balance to the user's line in the balances file
        sprint(f"You deposit ${choice}.00 into account {correctcaps(user, ['all'])}. Your new balance is ${balance+choice}.00") #successful deposit output message
        ask(user, "deposit", choice) #function to ask if the user wants to see their receipt for the deposit
        return #end the function
    input("wait why is this popped up? Maybe check the deposit function... ") #message that triggers as a debug marker if for some reason the function doesn't end


def withdraw(user): #function to deposit
    balance=getbal(usernum[user]) #find the amount of money in their account
    wipe() #clear screen to allow new content
    logo(2) #display logo in corner
    choice=tinput(f'\nHello, {correctcaps(user, ["all"])}. How much would you like to withdraw? Type "cancel" to cancel. $').lower() #interacts with user and asks for amount to withdraw
    if choice=="cancel": #if the user enters the cancel input
        menu(user) #return to menu
        return #end
    choice=checktype(choice)#convert choice to the highest type possibe (float > int > str)
    if type(choice)==str: #if the input type entered is invalid and not "cancel"
        sprint("String input is not valid! An integer or float input is required. Please try again.") #tell the user that they have entered invalid input
        return withdraw(user) #ask again
    if not (choice%10==0 and choice > 40) or not choice>0: #if they have entered a float or integer, but it is not a valid cash combination (20s and 50s)
        sprint("This amount is invalid! Only combinations of $20 and $50 cash notes can be withdrawn! Please try again.") #tell user what input is valid
        return withdraw(user) #ask again
    if choice > balance: #checks for if the user is withdrawing too much
        sprint(f"This amount is invalid! You are trying to withdraw ${choice}, but you only have ${balance} in your account!") #tell the user that they do not have enough money
        return withdraw(user) #ask again
    elif choice%5==0: #if the cash amount is a valid amount, continue on 
        choice=int(str(choice).replace(".0", "")) #remove the decimal from the end
        getbal(usernum[user], "write", balance-int(choice)) #write the new balance to the user's line in the balances file
        sprint(f"You withdraw ${choice}.00 from account {correctcaps(user, ['all'])}. Your new balance is ${balance-choice}.00") #successful withdrawl output message
        ask(user, "withdraw", choice) #function to ask if the user wants to see their receipt for the withdrawl


def receipt(user, transact, amount): #function to make a receipt based on the input user, process, and amount
    now = dm.now() #get a variable from current date and time
    transactlog=(f'''
  {logo(0, "small", "y")}
  
  {now.strftime('Date and Time: %D at %H:%M:%S.')}
  Location: {os.environ['COMPUTERNAME']} branch, machine #{r(1,6)} 
  Transaction ID: {r(10000, 99999)}
  User: {correctcaps(user, ['all'])}, PIN: {userdic[user]}
  Transaction: {correctcaps(transact)} of ${amount}.
  New Balance: ${getbal(usernum[user])}
  {now.strftime('Great Bank® Ltd.  %Y')}''') #an f-string that fills in a template to construct a reciept for the user.
    #line 1 adds the small logo to the corner of the receipt
    #line 3 adds the Date and Time
    #line 4 adds the Location, taking the name of the user's computer and a random number between 1 and 6
    #line 5 generates a random number as the Transaction ID
    #line 6 adds the user's credentials to the receipt?
    #line 7 informs the user as to the transaction they have done and how much money was involved
    #line 8 informs the user of their new balance
    #line 9 is a fake registed company name and the year for realism

    a=True #boolean
    i=0 #
    dic={} #
    slots=3
    while a==True: #until a is not true
        i+=1 #count
        if not os.path.exists(f"receipts/{user}/"): #Checks for if a user folder exists
            os.mkdir(f"receipts/{user}/") #makes a directory for the user if none exists
        for count in range(1, slots+1): #repeat three times, for reciept 1, receipt 2, and receipt 3
            try: #attempt to make a new file with count as the receipt number
                receipt=open(f"receipts/{user}/receipt {count}.txt", "x") #test if receipt count exists already, if it does, throws exception
                receipt.write(transactlog) #if it does not, writes the receipt contents into it
                receipt.close() #closes the file
                a=False #makes a not true so that the function goes to end 
                break #exit for loop
            except: #if the file already exists
                for line in open(f"receipts/{user}/receipt {count}.txt"): #opens the file that is known to exist
                    try: #for every line, checks if it has the date and time on it 
                        dic[line.strip("Date and Time: ").split(" ")[2]]=count #if it is the correct line, extracts date and time, exception is thrown otherwise
                        break #end for loop
                    except: #if it is the wrong line
                        pass #do nothing
                count+=1 #increment to next receipt

        if a==True: #will run if all receipt slots are taken
            lis=[] #define an empty list
            for element in dic: #each time extracted corresponds to the receipt number it was extracted from
                lis.append(element) #make a list from all the keys
                lis=sorted(lis) #sort the list (to find the oldest one)
            count=dic[lis[0]] #sets receipt number to that of oldest receipt
            receipt=open(f"receipts/{user}/receipt {count}.txt", "w") #overwrite the receipt
            receipt.write(transactlog) #write to the receipt
            receipt.close() #close file
            a=False #end the while loop
    
    return transactlog #for ask function

def ask(user, transact, amount): #function to ask the user if they want to see the receipt
    transactlog=receipt(user, transact, amount) #get contents thst were written to receipt
    logo(2) # logo in corner
    print_receipt = checkinput("Would you like to print a reciept? Y|N: ") #ask the user if they wish to see the receipt
    if print_receipt in ["y", "yes"]: #if they answer positively
        wipe() #clear screen to make space for receipt
        logo(16) #logo in corner
        print(transactlog) #print the receipt's contents
        t(0.5) #wait a small bit of time
        print("\nPress Ctrl+C when done reading, or wait for 10 seconds to pass.") #tell user what is happening with wait
        t(10, ["interrupt"]) #wait for 10 seconds, or (due to interrupt parameter) until KeyboardInterrupt is thrown
        menu(user)  #return to the menu
        return  #end

    #if negative input
    sprint("Thank you for using the Great Bank ATM") #end message
    menu(user)  #return to the menu
    return  #end

#############################################################################




############################################################################# Class for Miscellaneous functions

def logo(height_in, size="large", rtn="no"): #Defines the logo() function
                                             #to print the logo in the
                                             #corner of the screen -Ved

                                             #It sets the parameters:
                                             #height_in adjusts the
                                             #spacing underneath the logo


                                             #To use the function in combination
 
    testforvalue("screen_height", 50) #set values for screen_width and screen_height if none exist already
    wipe() #runs the wipe function
    try: #attempt to set the screen_width to the columns parameter
        screen_width=columns #try to do it
    except: #if it can't (maybe logo invoked separately?) then 
        screen_width=40 #set screen_width to 40 as a default
    global charbreak #charbreak for the sprint function
    olc=charbreak #preserve charbreak
    charbreak=0 #no pause between letter prints
    global endbreak #for sprint
    ole=endbreak #preserve endbreak
    endbreak=0 #no pause between lines
    for i in range(int(screen_width/60)): #repeat for 1/60th of the screen width
        print("") #add a spacer to top
    gap=int(screen_width/80)*" " #find the gap from the side of the screen
    log=(f'''
    {gap}+================================================+
    {gap}ǁ         GGGGGGGGGGGGG     BBBBBBBBBBBBBBBBB    ǁ
    {gap}ǁ      GGG::::::::::::G     B::::::::::::::::B   ǁ
    {gap}ǁ    GG:::::::::::::::G     B::::::BBBBBB:::::B  ǁ
    {gap}ǁ   G:::::GGGGGGGG::::G     BB:::::B     B:::::B ǁ
    {gap}ǁ  G:::::G       GGGGGG       B::::B     B:::::B ǁ
    {gap}ǁ G:::::G                     B::::B     B:::::B ǁ
    {gap}ǁ G:::::G                     B::::BBBBBB:::::B  ǁ
    {gap}ǁ G:::::G    GGGGGGGGGG       B:::::::::::::BB   ǁ
    {gap}ǁ G:::::G    G::::::::G       B::::BBBBBB:::::B  ǁ
    {gap}ǁ G:::::G    GGGGG::::G       B::::B     B:::::B ǁ
    {gap}ǁ G:::::G        G::::G       B::::B     B:::::B ǁ
    {gap}ǁ  G:::::G       G::::G       B::::B     B:::::B ǁ
    {gap}ǁ   G:::::GGGGGGGG::::G     BB:::::BBBBBB::::::B ǁ
    {gap}ǁ    GG:::::::::::::::G     B:::::::::::::::::B  ǁ
    {gap}ǁ      GGG::::::GGG:::G     B::::::::::::::::B   ǁ
    {gap}ǁ         GGGGGG   GGGGreat BBBBBBBBBBBBBBBBBank ǁ
    {gap}+================================================+
    ''') #logo 1 (in use)

    """
    {gap}+================================================+
    {gap}ǁ         GGGGGGGGGGGGG     BBBBBBBBBBBBBBBBB    ǁ
    {gap}ǁ      GGG::::::::::::G     B::::::::::::::::B   ǁ
    {gap}ǁ    GG:::::::::::::::G     B::::::BBBBBB:::::B  ǁ
    {gap}ǁ   G:::::GGGGGGGG::::G  $  BB:::::B     B:::::B ǁ
    {gap}ǁ  G:::::G       GGGGGG  $$   B::::B     B:::::B ǁ
    {gap}ǁ G:::::G               $  $  B::::B     B:::::B ǁ
    {gap}ǁ G:::::G               $     B::::BBBBBB:::::B  ǁ
    {gap}ǁ G:::::G    GGGGGGGGGG  $$   B:::::::::::::BB   ǁ
    {gap}ǁ G:::::G    G::::::::G    $  B::::BBBBBB:::::B  ǁ
    {gap}ǁ G:::::G    GGGGG::::G $  $  B::::B     B:::::B ǁ
    {gap}ǁ G:::::G        G::::G  $$   B::::B     B:::::B ǁ
    {gap}ǁ  G:::::G       G::::G   $   B::::B     B:::::B ǁ
    {gap}ǁ   G:::::GGGGGGGG::::G     BB:::::BBBBBB::::::B ǁ
    {gap}ǁ    GG:::::::::::::::G     B:::::::::::::::::B  ǁ
    {gap}ǁ      GGG::::::GGG:::G     B::::::::::::::::B   ǁ
    {gap}ǁ         GGGGGG   GGGGreat BBBBBBBBBBBBBBBBBank ǁ
    {gap}+================================================+
    """ #logo 2 (possibly used in future)


    if size=="small": #if asking for small logo
        log=("""+--------+\n  |::::::::|\n  |::Great:|\n  |::Bank::|\n  |::::::::|\n  +--------+""") #small logo (done in this format because unicode can't map to linebreaks?)
    if rtn in ["y", "yes"]: #if returning
        return log
    for line in log.split("/n"): #print the logo line by line?
        print(line)
    for j in range((screen_height-height_in)-20): #loop to space up the logo
        print("") #newlines
    endbreak=ole #reset endbreak
    charbreak=olc #reset charbreak

    
def local(s_w=32, s_h=38): #locsl function, this reads between universal start function and the local functions, starting the process.
    wipe() #clear the screen for more contnet
    global screen_width #
    global screen_height #
    screen_width=s_w #set
    screen_height=s_h #set

    gap1=int((screen_width-128)/2)*" " #spacingfrom the side of the screen for 'Great'
    gap2=int((screen_width-96)/2)*" " #spacing from the side of the screen for 'Bank'
    print(int((screen_height-40)/4)*"\n", end="") #spacer from the top of the screen to center the text
    print(f'''
    {gap1}        GGGGGGGGGGGGG                                                                                      tttt 
    {gap1}     GGG::::::::::::G                                                                                    ttt:::t
    {gap1}   GG:::::::::::::::G                                                                                    t:::::t
    {gap1}  G:::::GGGGGGGG::::G                                                                                    t:::::t
    {gap1} G:::::G       GGGGGG     rrrrr   rrrrrrrrr            eeeeeeeeeeee           aaaaaaaaaaaaa        ttttttt:::::ttttttt
    {gap1}G:::::G                   r::::rrr:::::::::r         ee::::::::::::ee         a::::::::::::a       t:::::::::::::::::t
    {gap1}G:::::G                   r:::::::::::::::::r       e::::::eeeee:::::ee       aaaaaaaaa:::::a      t:::::::::::::::::t
    {gap1}G:::::G    GGGGGGGGGG     rr::::::rrrrr::::::r     e::::::e     e:::::e                a::::a      tttttt:::::::tttttt
    {gap1}G:::::G    G::::::::G      r:::::r     r:::::r     e:::::::eeeee::::::e         aaaaaaa:::::a            t:::::t
    {gap1}G:::::G    GGGGG::::G      r:::::r     rrrrrrr     e:::::::::::::::::e        aa::::::::::::a            t:::::t
    {gap1}G:::::G        G::::G      r:::::r                 e::::::eeeeeeeeeee        a::::aaaa::::::a            t:::::t
    {gap1} G:::::G       G::::G      r:::::r                 e:::::::e                a::::a    a:::::a            t:::::t    tttttt
    {gap1}  G:::::GGGGGGGG::::G      r:::::r                 e::::::::e               a::::a    a:::::a            t::::::tttt:::::t
    {gap1}   GG:::::::::::::::G      r:::::r                  e::::::::eeeeeeee       a:::::aaaa::::::a            tt::::::::::::::t
    {gap1}     GGG::::::GGG:::G      r:::::r                   ee:::::::::::::e        a::::::::::aa:::a             tt:::::::::::tt
    {gap1}        GGGGGG   GGGG      rrrrrrr                     eeeeeeeeeeeeee         aaaaaaaaaa  aaaa               ttttttttttt
    ''')
    print(f'''
    {gap2}BBBBBBBBBBBBBBBBB                                                      kkkkkkkk
    {gap2}B::::::::::::::::B                                                     k::::::k
    {gap2}B::::::BBBBBB:::::B                                                    k::::::k
    {gap2}BB:::::B     B:::::B                                                   k::::::k
    {gap2}  B::::B     B:::::B        aaaaaaaaaaaa        nnnn  nnnnnnnn          k:::::k    kkkkkkk
    {gap2}  B::::B     B:::::B       a::::::::::::a       n:::nn::::::::nn        k:::::k   k:::::k
    {gap2}  B::::BBBBBB:::::B         aaaaaaaa:::::a      n::::::::::::::nn       k:::::k  k:::::k
    {gap2}  B:::::::::::::BB                  a::::a      nn:::::::::::::::n      k:::::k k:::::k
    {gap2}  B::::BBBBBB:::::B          aaaaaaa:::::a        n:::::nnnn:::::n      k::::::k:::::k
    {gap2}  B::::B     B:::::B       aa::::::::::::a        n::::n    n::::n      k:::::::::::k
    {gap2}  B::::B     B:::::B      a::::aaaa::::::a        n::::n    n::::n      k:::::::::::k
    {gap2}  B::::B     B:::::B     a::::a    a:::::a        n::::n    n::::n      k::::::k:::::k
    {gap2}BB:::::BBBBBB::::::B     a::::a    a:::::a        n::::n    n::::n     k::::::k k:::::k
    {gap2}B:::::::::::::::::B      a:::::aaaa::::::a        n::::n    n::::n     k::::::k  k:::::k
    {gap2}B::::::::::::::::B        a::::::::::aa:::a       n::::n    n::::n     k::::::k   k:::::k
    {gap2}BBBBBBBBBBBBBBBBB          aaaaaaaaaa  aaaa       nnnnnn    nnnnnn     kkkkkkkk    kkkkkkk
    ''')
    t(2)
    begin()

#############################################################################






############################################################################# User Credentials
    
def login(name,password):
  logo(1)
  if int(userdic[name])==int(password): #This checks if the login details are correct based on the dictionary made at start of script (and modified in register, maybe)
    sprint(f"{correctcaps(name, ['all'])} successfully logged in.") #Displays the login was successful

    menu(name) #calls menu function, this allows the rest of the code to continue

  else: #This makes it so that if the user
        #has not submitted the correct login
        #then they will not be granted access

    sprint(f"This is not the PIN for user {correctcaps(name, ['all'])}. Please try again.") #displays that the user has
                                       #entered the wrong login details
    access("login")


def register(name,password):
  name=name.strip()
  file = open("users.txt","a") #a+ Opens a file for both appending and reading.
                               # The file pointer is at the end of the file if
                               # the file exists. The file opens in the append mode.
                               # If the file does not exist,
                               # it creates a new file for reading and writing
  global nextmark
  file.write(f'\n{name},{password},{nextmark}') #writes name and password to
                                                #the user credentials file
  global userdic
  userdic[name]=password

  global usernum
  usernum[name]=nextmark

  
  file.close() #closes the file

  file=open("balances.txt", "a") #open the balances text file
  if int(nextmark)==70:
      amount="421.00"
      sprint(" YOU ARE THE 70TH CUSTOMER YOU GET $421 FREE")
  else:
      amount="10.00"
      sprint(f"User {correctcaps(name, ['all'])} is now registered. As a bonus, you have a free $10 in your new account.")
  file.write(f"{correctcaps(name, ['all'])}: {nextmark},{amount}\n") #add an entry to the balances file for the new user, with $420.
  file.close()
  nextmark+=1
  wipe() #clears the screen

  login(name,password) #runs the login function


def begin(something=""): #the beginning of the whole login thing
  if something!="": #this is a check to see if a login/register decision has already been specified. If it has, run that and end.
    access(something)
    return
  logo(1)
  access(checkinput("""Would you like to "login" to, "register", or "delete" a user? """, ["login", "register", "delete", "l", "r", "d", "exit"])) #Prompts user to input either, only asked if not specified

  
def access(option, name=""): #script to ask for username and password
  option=option.lower()
  wipe()
  logo(3)
  if option=="exit":
      sys.exit("exited by initial menu")
  if option=="l":
      option="login"
  elif option=="r":
      option="register"
  elif option=="d":
      option="delete"
      
  if name=="":
    
    print(f"\n{correctcaps(option)}:")
    name = tinput("""Enter your name, or "cancel" to cancel: """).lower() #prompts the user to input their name
  if name=="cancel":
      return begin()

  if option in ["delete", "d"]:
    global usernum
    global userdic
    if not name in userdic:
        sprint("This user does not exist! Please try again.")
        return begin()
    elif name.lower() in ["sameer", "dunne", "ved"]:
        sprint("This user is an essential user, and can not be deleted! Please try again.")
        return begin()
    else:
        PIN = tinput(f'To delete {name}, enter the PIN, or "cancel" to cancel: ')
        if PIN=="cancel":
            return begin()
        if int(PIN)==int(userdic[name]):
            try:
                file = open("users.txt").readlines() #a+ Opens a file for both appending and reading.
                extra = file[:file.index("**\n")+1] #save everything above the first divisor
                file = file[file.index("**\n")+1:] #remove everything above the divisior
                file.remove("********\n") #remove the divisor between main accounts and extra accounts
                for count, elem in enumerate(file[usernum[name]+1:], usernum[name]):
                    elem=elem.split(",")
                    elem=[str(elem[0])]+[elem[1]]+[str(int(elem[2])-1)]
                    elem=",".join(elem)
                    file[count+1] = elem
                print(file)
                file.pop(usernum[name])
                try:
                    ex=[]
                    for count, elem in enumerate(file[3:], 3):
                        ex.append("\n"+str(elem))
                except:
                    pass
                open("users.txt", "w").writelines(extra+file[:3]+["********"]+ex)
            except:
                print("Part A failed")

            try:
                file2 = open("balances.txt").readlines()
                for count, elem in enumerate(file2[usernum[name]+1:], usernum[name]):
                    ex, elem=elem.split(" ")
                    elem=elem.split(",")
                    elem=[str(int(elem[0])-1)]+[elem[1]]
                    elem=",".join(elem)
                    file2[count+1] = f'{ex} {elem}'
                file2.pop(usernum[name])
                usernum=dict(sorted(usernum.items(), key=lambda x: x[1]))
                for count, elem in enumerate(usernum):
                    if count<=usernum[name]:
                        continue
                    usernum[elem]=usernum[elem]-1
                usernum.pop(name)
                userdic.pop(name)
                file2[len(file2)-1]="\n"+str(file2[len(file2)-1].strip("\n"))
                open("balances.txt", "w").writelines(file2)
                global nextmark
                nextmark-=1
                sprint(f"User {name} deleted!")
            except:
                sys.exit(input("Part B failed"))
            return begin()

        else:
            sprint("This is not the PIN!")
            access("delete", name)

  if option in ["login", "l"] : #Checks what the user has input
                                #and runs the next script based on
                                #what they chose
    
    if name in userdic:
      password = checkintype(f"Enter the PIN for user {correctcaps(name, ['all'])}: ", [int]) #get the user to input password
      login(name,password) #runs the login function

    else:
      sprint(f"The user {correctcaps(name, ['all'])} is not registered. Please try again.")
      begin("login")

  elif option in ["register", "r"]: #Checks what the user has input
        #and runs the next script based on
        #what they chose
    if name.isalnum() == False:
        sprint("Sorry. You have entered invalid characters. ")
        sprint("Only letters and numbers are allowed in your username ")
        access("register")
    if name in userdic:
      sprint(f"The user {correctcaps(name, ['all'])} is already registered. Please try again.")
      begin("register")
    password="0"
    while len(str(password))!=4 or password.isdigit() == False:
        wipe()
        logo(2)
        print("Register: ")
        password = str(tinput(f"Enter a new PIN for user {correctcaps(name, ['all'])}: ")) #prompts the user to input
        if password=="cancel":                                                                   #their password
            return begin()
        if password.isdigit() == False:
            sprint("The password must only be a 4 character digit")
            sprint("For example: 1234")
            continue

        if len(password)==4:
            return register(name,password) #runs the register function'

        else:
            sprint("This PIN is the wrong length! The PIN needs to be four digits long and must only be digits.")

#############################################################################




############################################################################# Menu

def menu(user):
  balance=getbal(usernum[user])
  logo(11)
  charbreak=0.01
  
  choice_input=checkinput(f"""Hello, {correctcaps(user, ['all'])}, your current balance is ${balance}.00 

  1: Deposit
  2: Withdraw
  3: Log Out
  4: Exit
  
  What would you like to do, {correctcaps(user, ['all'])}? """, ["1", "2", "3", "4", "deposit", "withdraw", "log out", "exit", "d", "w", "L", "e"])

  charbreak=0.4
  if choice_input in ["1", "deposit", "d"]:
      deposit(user)
  elif choice_input in ["2", "withdraw", "w"]:
      withdraw(user)
  elif choice_input in ["3", "log out", "lo",]:
      sprint(f"Logging out {user}")
      begin()
  else:
      keyboard.press_and_release('F11')
      system(f'mode con: cols={120} lines={30}')
      sys.exit(f"ATM shut down by user {user}.")
  menu(user)

#############################################################################

#ask("ved", "robbery", 21320)

import stat
import shutil
mypath ="C:/noclear"
fname = mypath + "/" + "noclear.txt"


try: #all of this runs if the user is using the command prompt
##########################################################################################################################################################

    os.get_terminal_size() #this functiins throws an exception if the script is not running in terminal
    def sprint (input_string, words_or_letters="letters", newline="yes"): #this redefines the sprint function to be terminal-friendly
        space="\n"
        if newline!="yes":
            space=""
        print(input_string, end=space)
        t(0.045*len(input_string))
    
    def tinput(instring, a="frick!"):
        return input(instring)
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
        wipe()
        logo(4)
        return checkintype(input_string, list_of_types, letter, slow) #run again
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
            wipe()
            logo(4)
            return checkinput(input_string, comparison_list) #run again
    try: #attempt to delete file
      try:
          shutil.rmtree(mypath)
      except:
          os.chmod(mypath, stat.S_IWRITE)
          shutil.rmtree(mypath)
    except:
        pass #if the file does not exist
    
    ##############################################################
    # obtained from https://stackoverflow.com/a/3129494
    import wx #import WxPython to make an app and find the monitor size
    app = wx.App(False) # the wx.App object must be created first.
    col, lin=wx.GetDisplaySize() # returns a tuple
    ##############################################################
    
    from os import system #import system to modify the os atributes
    system(f'mode con: cols={col} lines={lin}') #change the size of the terminal window
    import keyboard #import the keyboard module, allowing the script to send keystrokes
    keyboard.press_and_release('F11') #this fullscreens the terminal window
    
##########################################################################################################################################################
except: #this runs if they are not using the command prompt
    try: #attempt to make a file that triggers the clear() function
      os.makedirs(mypath,0o777) #make a folder for the file
      open(fname,"w").close() #make a marker file
    except: #if the file already exists
        pass
    tinput("This script is recommended to be run on the command line, using the provided batch file, but if you wish to continue, press Enter: ") #Tell user 

wipe()
sprint("loading...")
wipe()
start("The GREAT Bank")
