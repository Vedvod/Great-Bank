############################################################################
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

        import os    #imports os module
        import sys   #imports sys module
        import time  #imports time module

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

                exec(open("/".join(segment)+"/universal functions.py").read()) #tries to open
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

############################################################################
#All above uses os module to locate
#the project folder using user input
#It then opens universal functions
#using this path

global charbreak #comment
global endbreak  #comment

userlist = open("users.txt")
userdic = {}
usernum = {}
for combo in userlist:
  try:
    name, pin, nextmark = combo.strip("\n").split(",")
    userdic[name] = pin.strip()
    nextmark=int(nextmark)
    usernum[name] = nextmark
    nextmark+=1
  except:
   ""

charbreak=0.025 #set charbreak for slow
endbreak=0.065 #set endbreak for slow

def getbal(marker, mode="read", value=0):
    balances=open("balances.txt")
    if mode in ["r", "read"]:
        for line in balances:
            try:
                line=line.split(": ")[1]
            except:
                ""
            line=line.strip("\n")
            number, amount=line.split(",")
            number=int(number)
            if int(number)==int(marker):
                 return int(amount)
        
    elif mode in ["w", "write"]:
        baldic={}
        for line in balances:
            try:
                line=line.split(": ")[1]
            except:
                ""
            line=line.strip("\n")
            try:
                number, amount=line.split(",")
                if int(number)==int(marker):
                    amount=value
                baldic[number]=amount
            except:
                ""
        file=open("balances.txt", "w")
        file.write("") #clears file
        file.close()
        file=open("balances.txt", "a")
        for numb in baldic:
            for elem in usernum:
                if int(usernum[elem])==int(numb):
                    break
            file.write(f"{correctcaps(elem, ['all'])}: {numb},{baldic[numb]}\n")
        file.close()

def deposit(user): #function to deposit
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
        receipt(user, "deposit", choice)

def logo(height_in, size="large", rtn="no"): #a function to print the logo in the corner of the screen -Ved
    wipe()
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
    ''') #the logo
    if size=="small":
        log=("""+--------+\n  |::::::::|\n  |::Great:|\n  |::Bank::|\n  |::::::::|\n  +--------+""") #small logo
    if rtn in ["y", "yes"]:
        return log
    sprint(log, "l")
    for j in range((screen_height-height_in)-int(screen_width/80)-19): #loop to space up the logo
        print("") #newlines
    endbreak=ole #reset endbreak
    charbreak=olc #reset charbreak

def local():
    wipe()
    global screen_width
    global screen_height
    try:
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
    {gap3}Absurd Tachyometric Matrix Machine                                                                                              
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
    t(1)
    begin()


################

def reading_sleep():
    #sleep for 5 is fucntion i use frequently within my code for the theory section
    #So i have decided to shorted the process and make it a function
    t(5)

def normal_sleep():
    #sleep for 0.5 is fucntion i use frequently within my code
    #So i have decided to shorted the process and make it a function
    t(0.5)

def wipe():
    t(1)
    try:
        open("C:/noclear/noclear.txt")
        clear()
    except:
        if os.name != 'posix':
            # Else Operating System is Windows (os.name = nt)
            _ = os.system('cls')
        # Check if Operating System is Mac and Linux or Windows
        else:
            _ = os.system('clear')


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
      
  if name=="":
    
    print(f"\n{correctcaps(option)}:")
    name = tinput("""Enter your name, or "cancel" to cancel: """).lower() #prompts the user to input their name
  if name=="cancel":
      begin()
      return

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
        password = checkintype(f"Enter a new PIN for user {correctcaps(name, ['all'])}: ", [int]) #prompts the user to input
        if len(str(password))==4:                                #their password
            break
        sprint("This PIN is the wrong length! The PIN needs to be four digits long.")
        wipe()
        logo(2)

    register(name,password) #runs the register function

################

def receipt(user, transact, amount):
    from datetime import datetime as dm
    import os
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
    while a==True:
        dic={}
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

def menu(user):
  balance=getbal(usernum[user])
  logo(10)
  sprint(f"Hello, {correctcaps(user, ['all'])}, your current balance is ${balance}.\n")
  sprint("""
  1: Deposit
  2: Withdraw
  3: Check Transactions
  4: Exit
  """, "l")
        
  charbreak=0.01
  choice_input=checkinput(f"What would you like to do, {correctcaps(user, ['all'])}? ", ["1", "2", "3", "4", "deposit", "withdraw", "check transactions", "exit", "d", "w", "check", "e", "ct", "c"])
  if choice_input in ["1", "deposit", "d"]:
      deposit(user)
  elif choice_input in ["2", "withdraw", "w"]:
      choice_input="Withdraw"
  elif choice_input in ["3", "check transactions", "check", "ct", "ct", "c"]:
      choice_input="Check Transactions"
  else:
      sys.exit("ok bye!")
  print(f"Choice: {choice_input}")
  menu(user)

wipe()
start("The GREAT Bank")

logo(1)
