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
        z=[]
        zel=1
        dic={}
        y=0
        zel=0
        hay=[]
        #get file path
        b=__file__ + "check universal functions"

        #translate windows to macOS/linux if applicable, by changing character 92 (\) to /
            #then, split on the /
        a=(b.replace(chr(92),"/")).split("/")

        for w in a:
            if y==0: #ignore first, which is a "" or D:
                y=1
                z.append("")
                continue
            z.append(w) #adds step to path
            zel+=1
            hay.append(str(zel))
            dic[str(zel)]="/".join(z) #stores path in dictionary
            
        global pat #
        for a in dic: #for each step in path, print incrementally
            pat=dic[a] #works if user input is dictionary key
            try:
                exec(open(pat+"/universal functions.py").read()) #opens universal functions
                break
            except: #if can not open universal functions file
                continue
        try:
            exec(open(pat+"/universal functions.py", "r").read())
        except: #if universal functions is not work
            sys.exit("Check universal functions.py perhaps...")
        global path #sets global path file to the user-chosen path
        path=pat
        print(path+" located.") #confirmation message
        return open(path+"/universal functions.py", "r").read()
    exec(findpath())
############################################################################
#All above uses os module to locate the project folder using user input
    #It then opens universal functions using this path
