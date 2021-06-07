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
