import os  # imports os module
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
          #below will run This ]
          #except statement catches
          #all the lines in the .txt
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

            if int(number)==int(marker): #This checks if the user id is equal
                                         #to the marker parameter which is
                                         #defined in the function parameters
                                         #above

                 return int(amount) #When the two variables are
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



############################################################################# Class for Transactions
def deposit(user): #defines the
    balance=getbal(usernum[user])
    wipe()
    logo(2) #logo in corner
    choice=tinput(f'\nHello, {correctcaps(user, ["all"])}. How much would you like to deposit? Type "cancel" to cancel. $').lower() #ask for amount
    if choice=="cancel": #if exit
        menu(user) #return to menu
        return #end
    choice=checktype(choice)
    if type(choice)==str:
        sprint("String input is not valid! An integer or float input is required. Please try again.")
        return deposit(user)
    if not choice%5 == 0 or not int(choice)>0:
        sprint("This amount is invalid! Only combinations of cash notes can be accepted! Please try again.")
        return deposit(user)
    elif choice%5==0:
        getbal(usernum[user], "write", balance+int(choice))
        sprint(f"You deposit ${choice} into account {correctcaps(user, ['all'])}. Your new balance is ${balance+choice}.")
        receipt(user, "deposit", choice)                                                       z#

def withdraw(user): #function to deposit
    balance=getbal(usernum[user])
    wipe()
    logo(2) #logo in corner
    choice=tinput(f'\nHello, {correctcaps(user, ["all"])}. How much would you like to withdraw? Type "cancel" to cancel. $').lower() #ask for amount
    if choice=="cancel": #if exit
        menu(user) #return to menu
        return #end
    choice=checktype(choice)
    if type(choice)==str:
        sprint("String input is not valid! An integer or float input is required. Please try again.")
        return withdraw(user)
    if not choice%5 == 0 or not int(choice)>0:
        sprint("This amount is invalid! Only combinations of cash notes can be withdrawn! Please try again.")
        return withdraw(user)
    if choice>balance: #checks for if withdrawing too much
        sprint(f"This amount is invalid! You are trying to withdraw ${choice}, but you only have ${balance} in your account!")
        return withdraw(user)       
    elif choice%5==0:
        getbal(usernum[user], "write", balance-int(choice))
        sprint(f"You withdraw ${choice} from account {correctcaps(user, ['all'])}. Your new balance is ${balance-choice}.")
        receipt(user, "withdraw", choice)

def receipt(user, transact, amount):
    now = dm.now() # current date and time
    transactlog=(f'''
  {logo(0, "small", "y")}
  {dm.now().strftime('Date and Time: %D at %H:%M:%S.')}
  Location: {os.environ['COMPUTERNAME']} branch, machine #{r(1,6)}
  Transaction ID: {r(20000, 500000)}
  User: {correctcaps(user, ['all'])}, PIN: {userdic[user]}
  Transaction: {correctcaps(transact)} of ${amount}.
  New Balance: {getbal(usernum[user])}
  {dm.now().strftime('Great Bank inc. %Y')}''')

    a=True
    if not os.path.exists(f"/receipts/{user}"):
       os.makedirs(f"/receipts/{user}")
    while a==True:
        dic={}
        if not os.path.exists(f"receipts/{user}/"):
            os.mkdir(f"receipts/{user}/")
        for count in range(1,4):
            try:
                a=False
                receipt=open(f"receipts/{user}/receipt {count}.txt", "x")
                receipt.write(transactlog)
                receipt.close()
                break
            except:
                e=0
                for line in open(f"receipts/{user}/receipt {count}.txt"):
                    try:
                        dic[line.strip("Date and Time: ").split(" ")[2]]=count
                        break
                    except:
                        e+=1
                count+=1
        if a==True:
            lis=[]
            for element in dic:
                lis.append(element)
                lis=sorted(lis)
            count=dic[lis[0]]
            receipt=open(f"receipts/{user}/receipt {count}.txt", "w")
            receipt.write(transactlog)
            receipt.close()
#############################################################################




############################################################################# Class for Aesthetics
def logo(height_in, size="large", rtn="no"): #Defines the logo() function
                                             #to print the logo in the
                                             #corner of the screen -Ved

                                             #It sets the parameters:
                                             #height_in adjusts the
                                             #spacing underneath the logo


                                             #To use the function in combination




    wipe() #runs the wipe function
    try:
        screen_width
    except:
        screen_width=40
    global charbreak #charbreak for the sprint function
    olc=charbreak #preserve charbreak
    charbreak=0 #no pause between letter prints
    global endbreak #for sprint
    ole=endbreak #preserve endbreak
    endbreak=0 #no pause between lines
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

    if size=="small":
        log=("""+--------+\n  |::::::::|\n  |::Great:|\n  |::Bank::|\n  |::::::::|\n  +--------+""") #small logo
    if rtn in ["y", "yes"]:
        return log
    for line in log.split("/n"):
        print(line)
    for j in range((screen_height-height_in)-int(screen_width/80)-19): #loop to space up the logo
        print("") #newlines
    endbreak=ole #reset endbreak
    charbreak=olc #reset charbreak

def local():
    wipe()
    global screen_width
    global screen_height
    try:
        screen_height-=2
        screen_width
    except:
        screen_width=40
    gap1=int((screen_width-122)/2)*" "
    gap2=int((screen_width-90)/2)*" "
    gap3=int((screen_width-34)/2)*" "
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
    print(int((screen_height-40)/2)*"\n", end="")
    t(2)
    begin()

if not ('idlelib.run' in sys.modules or "PYCHARM_HOSTED" in os.environ):
    endbreak=0
    charbreak=0
    def sprint (input_string, words_or_letters="letters", newline="yes"):
        space="\n"
        if newline!="yes":
            space=""
        print(input_string, end=space)
        t(0.065*len(input_string))
#############################################################################






############################################################################# Class for User Credentials
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
    access("login", name)

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
  file.write(f"{correctcaps(name, ['all'])}: {nextmark},{10}\n") #add an entry to the balances file for the new user, with $10.
  file.close()
  nextmark+=1
  sprint(f"User {correctcaps(name, ['all'])} is now registered. As a bonus, you have a free $10 in your new account.")
  wipe() #clears the screen

  login(name,password) #runs the login function

def begin(something=""): #the beginning of the whole login thing
  if something!="": #this is a check to see if a login/register decision has already been specified. If it has, run that and end.
    access(something)
    return
  logo(1)
  access(checkinput("""Would you like to "login", "register", or "delete"? """, ["login", "register", "delete", "l", "r", "d"])) #Prompts user to input either, only asked if not specified
  
def access(option, name=""): #script to ask for username and password yes
  option=option.lower()
  wipe()
  logo(3)
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
      begin()
      return



  if option in ["delete", "d"]:
    global usernum
    if not name in usernum:
        sprint("This user does not exist! Please try again.")
        begin()
    else:
        if int(tinput(f"To delete {name}, enter the PIN. "))==int(userdic[name]):
            file = open("users.txt").readlines() #a+ Opens a file for both appending and reading.
            extra=file[:file.index("**\n")+1]
            file = file[file.index("**\n")+1:]
            file.remove("********\n")
            file.pop(usernum[name])
            fil=open("users.txt", "w")
            fil.writelines(extra+file[:3]+["********\n"]+file[3:])
            fil.close()

            file2 = open("balances.txt").readlines()
            file2.pop(usernum[name])
            fil=open("balances.txt", "w")
            fil.writelines(file2)
            fil.close()
            sprint(f"User {name} deleted!")
            begin()
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
      
    if name in userdic:
      sprint(f"The user {correctcaps(name, ['all'])} is already registered. Please try again.")
      begin("register")
    password="0"
    while len(str(password))!=4:
        password = str(tinput(f"Enter a new PIN for user {correctcaps(name, ['all'])}: ")) #prompts the user to input
                                                                                                  #their password
        if password.isdigit() == False:
            sprint("The password must only be a 4 character digit")
            sprint("For example: 1234")
            continue

        if len(password)==4:
            break
        else:
            sprint("This PIN is the wrong length! The PIN needs to be four digits long and must only be digits.")

        wipe()
        logo(2)

    register(name,password) #runs the register function
#############################################################################







############################################################################# Class for Menu
def menu(user):
  balance=getbal(usernum[user])
  logo(11)
  sprint(f"Hello, {correctcaps(user, ['all'])}, your current balance is ${balance}.\n")
  sprint("""
  1: Deposit
  2: Withdraw
  3: Check Transactions
  4: Log Out
  5: Exit
  """, "l")
        
  charbreak=0.01
  choice_input=checkinput(f"What would you like to do, {correctcaps(user, ['all'])}? ", ["1", "2", "3", "4", "deposit", "withdraw", "check transactions", "exit", "d", "w", "check", "e", "ct", "c"])
  if choice_input in ["1", "deposit", "d"]:
      deposit(user)
  elif choice_input in ["2", "withdraw", "w"]:
      withdraw(user)
  elif choice_input in ["3", "check transactions", "check", "ct", "ct", "c"]:
      choice_input="Check Transactions"
  elif choice_input in ["4", "log out", "lo",]:
      sprint(f"Logging out {user}")
      begin()
  else:
      sys.exit(f"ATM shut down by user {user}.")
  menu(user)
#############################################################################


wipe()
sprint("loading...")
start("The GREAT Bank")

