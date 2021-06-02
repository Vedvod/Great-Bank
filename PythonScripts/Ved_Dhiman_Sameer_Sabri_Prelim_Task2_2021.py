############################################################################
try: #if started value assigned, don't run
    exec(findpath())
except: #otherwise, run
    def findpath():
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
        
        for step in modfilepath:
            if count==0: #ignore first, which is a "" or a "D:"
                count=1
                segment.append("")
                continue
            segment.append(step) #adds step to path
            try:
                exec(open("/".join(segment)+"/universal functions.py").read()) #opens universal functions
                global path_to_directory #sets global path file to the user-chosen path
                path_to_directory="/".join(segment)
                break
            except: #if can not open universal functions file
                continue
        try:
            open(path_to_directory+"/universal functions.py", "r").read()
            return open(path_to_directory+"/universal functions.py", "r").read()
        except:
            sys.exit("It seems that the universal functions file cannot run!")
    exec(findpath())
############################################################################
#All above uses os module to locate the project folder using user input
    #It then opens universal functions using this path
import os
import sys
import time
global charbreak
global endbreak
charbreak=0.035
endbreak=0.065

def correctcaps(string): #a function to correct the capitalisation of a given string, typically multi-sentence.
    final=""
    e=0
    sentences=string.lower().replace(".", "*.").replace("?", "^?").split(".")
    sent=[]
    for f in sentences:
        f=f.strip().split("?")[:len(f)]
        sent+=f
    sentences=sent
    for sentence in sentences:
        if sentence=="":
            continue
        sentence=sentence.strip()
        finsentence=sentence[0].upper()
        for letter in sentence[1:]:
            if e==1:
                letter=letter.upper()
                e=0
            if letter=="~":
                e=1
                continue
            finsentence+=letter
        final+=finsentence
        if finsentence.endswith("^"):
            final=final.rstrip("^")
            final+="? "
        elif finsentence.endswith("*"):
            final=final.rstrip("*")
            final+=". "
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
    ''', "l")
    for j in range((screen_height-height_in)-int(screen_width/80)): #loop to space up the logo
        print("") #newlines
    endbreak=ole #reset endbreak
    charbreak=olc #reset charbreak

def calibsize(): #function to get user to calibrate their screen size for later usage
    global screen_width #global screensize
    global screen_height #global screensize
    if checkinput("Do you want to calibrate the screen size? ") not in ["y", "yes"]: 
        screen_height=46 #default height
        screen_width=37*4 #default width
        return
    for i in range(91, 0, -1): #script to callibrate screensize
        print(i) #countdown on screen
    global charbreak #
    charbreak=0.001
    global endbreak
    endbreak=0.03
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
global screen_height
calibsize()

def local():
    clear()
start("The GREAT Bank")

gap1=int((screen_width-122)/2)*" "
gap2=int((screen_width-90)/2)*" "
gap3=int((screen_width-34)/2)*" "
print(f"""                                                                                                                                                                                                                                                              
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
""")
print(f"""
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
""")
print(int((screen_height-40)/2)*"\n", end="")
t(2)

##
def login():
    username=tinput("What is your name? ").lower().strip()
    if not username in userdic:
        return register(username)
    if tinput("What is the PIN? ").strip()==userdic[username]:
        sprint(f"User {correctcaps(username)} successfully logged in.")
        return username
    sprint("This is not the correct PIN. Please try again.")
    return login()

def register(username):
    newpass=tinput(f"{correctcaps(username)} is not a registed user. Please enter a PIN for this new user: ").strip()
    if len(newpass)==4 and newpass.isdigit():
        if newpass in userdic.values():
            while newpass in userdic.values():
                newpass=tinput("This PIN is already taken! Please choose a different PIN: ")
        userdic[username]=newpass
        newuser=open("users.txt", "a")
        newuser.write(f"\n{username},{newpass}")
        sprint(f"User {correctcaps(username)} successfully registered with PIN {newpass}.")
        if not os.path.exists(f"{path_to_directory}/Users/{username}"):
            os.makedirs(f"{path_to_directory}/Users/{username}")
        return username
    sprint(f"{newpass}, {len(newpass)==4}, {newpass.isdigit()}")
    sprint("This PIN is the wrong length or contains non-numerals. Needs to be 4 numerals.")
    return register(username)

userlist = open("users.txt")
userdic = {}
for combo in userlist:
  try:
    name, pin = combo.split(",")
    userdic[name] = pin.strip("\n")
  except:
    ""

logged_in=login()

def menu(user):
    testforvalue("balance", 1000)
    clear()
    logo(31)
    sprint(f"Hello, {correctcaps(user)}. Your current balance is ${balance}\n")
    sprint("""
    1: Deposit
    2: Withdraw
    3: Check Transactions
    4: Exit
    """, "l")
      
    charbreak=0.01
    choice_input=checkinput(f"What would you like to do, {correctcaps(user)}? ", ["1", "2", "3", "4", "deposit", "withdraw", "check transactions", "exit", "d", "w", "check", "e", "ct", "c"])
    if choice_input in ["1", "deposit", "d"]:
        choice_input="Deposit"
    elif choice_input in ["2", "withdraw", "w"]:
        choice_input="Withdraw"
    elif choice_input in ["3", "check transactions", "check", "ct", "ct", "c"]:
        choice_input="Check Transactions"
    else:
        sys.exit("ok bye!")
    print(f"Choice: {choice_input}")

menu(logged_in)
##

