############################################################################
try: #if function defined, run it
    exec(findpath()) #try run function
except: #otherwise, run
    def findpath(): #define function to find path
        #import modules
        import os
        import sys
        import time

        #set variables
        segment=[]
        count=0
        dic={}
        y=0
        #get file path
        filepath=__file__ + "check universal functions"

        #translate windows to macOS/linux if applicable, by changing character 92 (\) to /
            #then, split on the /
        modfilepath=(filepath.replace(chr(92),"/")).split("/")
        
        for step in modfilepath: #increment directory to locate which one universal functions is in
            if count==0: #ignore first, which is a "" or a "D:"
                count=1 #stop ignoring
                segment.append("")
                continue
            segment.append(step) #adds step to path
            try: #attempt to find and run universal functions in given directory
                exec(open("/".join(segment)+"/universal functions.py").read()) #try to open universal functions
                global path_to_directory #sets global path file to the user-chosen path
                path_to_directory="/".join(segment)
                break #end loop since universal functions located
            except: #if can not open universal functions file
                continue
        try: #test if previous loop actually found the file
            open(path_to_directory+"/universal functions.py", "r").read() #open it
            return open(path_to_directory+"/universal functions.py", "r").read() #return the opened file, since function is executed
        except: #if can not find file
            sys.exit("It seems that the universal functions file cannot run!") #error message, ends script
    exec(findpath()) #if not fail, executes universal function
############################################################################
#All above uses os module to locate the project folder using user input
    #It then opens universal functions using this path

import os
import sys
import time
global charbreak
global endbreak
charbreak=0.025 #set charbreak for slow
endbreak=0.065 #set endbreak for slow

def correctcaps(string, all=""): #a function to correct the capitalisation of a given string, typically multi-sentence.
    final="" #define final as a string
    dotsplit=string.lower().replace(".", "*.").replace("?", "^?").replace("!", "@!").replace(" ", "`` ").split(".") #add markers for punctuation, then split on dots
    quesplit=[]
    if all=="y":
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

def logo(height_in): #a function to print the logo in the corner of the screen -Ved
    global charbreak #charbreak for the sprint function
    olc=charbreak #preserve charbreak
    charbreak=0 #no pause between letter prints
    global endbreak #for sprint
    ole=endbreak #preserve endbreak
    endbreak=0 #no pause between lines
    gap=int(screen_width/80)*" " #find the gap from the side of the screen
    sprint(f'''
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
    ''', "l") #the logo
    for j in range((screen_height-height_in)-int(screen_width/80)): #loop to space up the logo
        print("") #newlines
    endbreak=ole #reset endbreak
    charbreak=olc #reset charbreak

def calibsize(): #function to get user to calibrate their screen size for later usage
    if checkinput("Do you want to quick calibrate the screen size? ") in ["y", "yes"]: #negative response
        screen_height=37 #default height
        screen_width=32*4 #default width
        for i in range(32*4+1):
            print("0", end="")
        input("\nAdjust the screen width until all the zeros are on one line.")
        clear()
        print("0")
        for i in range(36, 0, -1): #script to callibrate screensize
            print("") #countdown on screen
        input("Adjust the screen height until the zero is fully on the screen.")
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
    clear() #clear
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
screen_width, screen_height=calibsize()

def local():
    clear()
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
    t(0.5)
    
start("The GREAT Bank")

##
def login():
    userlist = open("users.txt")
    userdic = {}
    for combo in userlist:
      try:
        name, pin, balance = combo.split(",")
        userdic[name] = pin.strip("\n")
      except:
        ""
    username=tinput("\nWhat is your name? ").lower().strip()
    if not username in userdic:
        sprint(f"Registration required for new user {correctcaps(username, 'y'}...")
        local()
        return register(username, userdic)
    if tinput("What is the PIN? ").strip()==userdic[username]:
        sprint(f"User {correctcaps(username, 'y')} successfully logged in.")
        return username, balance
    sprint("This is not the correct PIN. Please try again.")
    local()
    return login()

def register(username, userdic):
    newpass=tinput(f"""{correctcaps(username, 'y')} is not a registed user. Please enter a PIN for this new user, or "cancel" to cancel: """).strip()
    if newpass.lower()=="cancel":
        local()
        return login()
    if len(newpass)==4 and newpass.isdigit():
        if newpass in userdic.values():
            while newpass in userdic.values():
                newpass=tinput("This PIN is already taken! Please choose a different PIN: ")
        userdic[username]=newpass
        newuser=open("users.txt", "a")
        newuser.write(f"\n{correctcaps(username, 'y')},{newpass}")
        sprint(f"User {correctcaps(username, 'y')} successfully registered with PIN {newpass}.")
        if not os.path.exists(f"{path_to_directory}/Users/{username}"):
            os.makedirs(f"{path_to_directory}/Users/{username}")
        return username
    if len(newpass)!=4:
        sprint("This PIN is the wrong length. The PIN needs to be 4 digits long.")
    if not newpass.isdigit():
         sprint("This PIN contains non-numerals. The PIN needs to be only numerals.")
    local()
    return register(username, userdic)

def menu(user, balance):
    clear()
    logo(31)
    sprint(f"Hello, {correctcaps(user, 'y')}. Your current balance is ${balance}\n")
    sprint('''
    1: Deposit
    2: Withdraw
    3: Check Transactions
    4: Exit
    ''', "l")
      
    charbreak=0.01
    choice_input=checkinput(f"What would you like to do, {correctcaps(user)}? ", ["1", "2", "3", "4", "deposit", "withdraw", "check transactions", "exit", "d", "w", "check", "e", "ct", "c"])
    if choice_input in ["1", "deposit", "d"]:
        choice_input="Deposit"
    elif choice_input in ["2", "withdraw", "w"]:
        choice_input="Withdraw"
    elif choice_input in ["3", "check transactions", "check", "ct", "ct", "c"]:
        choice_input="Check Transactions"
    else:
        sys.exit(f"{correctcaps(user)} logged out, shutting down...")
    print(f"Run: {choice_input}")
    
logged_in, balance=login()
menu(logged_in, balance)
