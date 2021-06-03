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
    
def register(username):
    newpass=tinput(f"{username} is not a registed user. Please enter a PIN for this new user: ").strip()
    if len(newpass)==4 and newpass.isdigit():
        if newpass in userdic.values():
            while newpass in userdic.values():
                newpass=tinput("This PIN is already taken! Please choose a different PIN: ")
        userdic[username]=newpass
        newuser=open("users.txt", "a")
        newuser.write(f"\n{username},{newpass}")
        sprint(f"User {username} successfully registered with PIN {newpass}.")
        if not os.path.exists(f"{path_to_directory}/Users/{username}"):
            os.makedirs(f"{path_to_directory}/Users/{username}")
        return username
    sprint(f"{newpass}, {len(newpass)==4}, {newpass.isdigit()}")
    sprint("This PIN is the wrong length or contains non-numerals. Needs to be 4 numerals.")
    return register(username)

def menu(user):
  tinput(f"Welcome, {user}. What would you like to do today? ")

userlist = open("users.txt")
userdic = {}
for combo in userlist:
  try:
    name, pin = combo.split(",")
    userdic[name] = pin.strip("\n")
  except:
    ""
  
def login():
    username=tinput("What is your name? ").lower().strip()
    if not username in userdic:
        return register(username)
    if tinput("What is the PIN? ").strip()==userdic[username]:
        sprint(f"User {username} successfully logged in.")
        return username
    sprint("This is not the correct PIN. Please try again.")
    return login()

logged_in=login()
menu(logged_in)
