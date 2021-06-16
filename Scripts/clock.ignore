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
charbreak=0.05
endbreak=0.9
userdic={}
user="ved"
userdic["ved"]=1234

def logo(height_in, size="large", rtn="no"): #a function to print the logo in the corner of the screen -Ved
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
        log=("""+-------+
|::::::::|
|::Great:|
|::Bank::|
|::::::::|
+-------+""")
    if rtn in ["y", "yes"]:
        return log
    sprint(log, "l")
    for j in range((screen_height-height_in)-int(screen_width/80)-19): #loop to space up the logo
        print("") #newlines
    endbreak=ole #reset endbreak
    charbreak=olc #reset charbreak

def receipt(user, transact, amount)    
    from datetime import datetime as dm
    import os
    now = dm.now() # current date and time
    transactlog=(f"""{logo(0, "small", "y")}

    {dm.now().strftime('Date and Time: %D at %H:%M:%S.')}
    Location: {os.environ['COMPUTERNAME']} branch, machine #{r(1,6)}
    Transaction ID: {r(20000, 500000)}
    User: {correctcaps(user, ['all'])}, PIN: {userdic[user]}
    Transaction: {correctcaps(transact)} of ${amount}.
    """)

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

transact=transactlist[len(transactlist)-1]
e=0
while True and e==1:
    try:
        transact=transactlist[transactlist.index(transact)+1]
    except:
        transact=transactlist[0]
    now1 = dm.now()
    t(0.3)
    if now1.strftime("%S")!=(dm.now()).strftime("%S"):
        curtime=(dm.now()).strftime(f"Transaction {transact} processed on %D at %H:%M:%S.")
        print(curtime)
