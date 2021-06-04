import time
import sys
import os
import random
from os import system, name
from time import sleep

granted = False
def grant():
  global granted
  granted = True

def menu():
  pass

def reading_sleep():
    #sleep for 5 is fucntion i use frequently within my code for the theory section
    #So i have decided to shorted the process and make it a function
    sleep(5)

def normal_sleep():
    #sleep for 0.5 is fucntion i use frequently within my code
    #So i have decided to shorted the process and make it a function
    sleep(0.5)

def clear():
    # define our clear function
    # for windows
    if name == 'nt':
        _ = os.system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')

def login(name,password):
  valid = False
  file = open("User_Credentials.txt","a+") #a+ Opens a file for both appending and reading.
                                           # The file pointer is at the end of the file if
                                           # the file exists. The file opens in the append mode.
                                           # If the file does not exist,
                                           # it creates a new file for reading and writing

  for i in file:          #this for loop takes the user input for password and name and checks
                          #if it is correct or not

    n,p = i.split(",")    #n is the variable for name
                          #p in the variable for password
                          #i.split spits the lines read from
                          #the user credentials file on the basis
                          #of the , and put them in lists

    p = p.strip()         #The strip() method returns a copy of
                          # the string by removing both the leading and
                          # the trailing characters (based on the string
                          # argument passed). The strip() method removes
                          # characters from both left and right based on the
                          # argument (a string specifying the set of characters t
                          # o be removed).

    if (n == name and p == password ): #This checks if n and name and
                                       # p and password have the same value

      valid = True #this changes valid to true
                   #which is neccessary for the
                   #next if statement which gives
                   #confirmation to the user if they
                   #have entered the correct longin
                   #and were successful or whether they were wrong

      break #break leaves the looop

  file.close() #closes the file

  if(valid):
    print("Login successful") #Displays the login was successful

    clear() #clears screen for improved
            #readability

    grant() #The grant function changes
            #changes the granted value
            #to true so that the user can
            #now access the menu

  else: #This makes it so that if the user
        #has not submitted the correct login
        #then they will not be granted access

    print("Wrong usernme or password") #displays that the user has
                                       #entered the wrong login details

def register(name,password):
  file = open("User_Credentials.txt","a+") #a+ Opens a file for both appending and reading.
                                           # The file pointer is at the end of the file if
                                           # the file exists. The file opens in the append mode.
                                           # If the file does not exist,
                                           # it creates a new file for reading and writing

  file.write("\n"+name+","+password) #writes name and password to
                                     #the user credentials file

  file.close() #closes the file

  clear() #clears the screen

  login(name,password) #runs the login function

  clear() #clears the screen

  grant() #runs the grant function

def begin():
  global option #makes option a global
                #variablw which can be
                #accesssed in any part
                #of the code

  print("Welcome to the Great Bank") #Displays welcome to Great Bank

  option = input("Login or Register (Login,Reg): ") #Prompts user to input either
                                                    #Login or Reg

  if option != "Login" and option != "Reg": #this makes sure the user
                                            #can only input Login or Reg

    clear() #Clears the screen

    begin() #makes the begin function start
            #again until the desired input
            #is reached

def acess():
  global name
  if (option == "Login"):
    name = input("Enter your name: ")
    password = input("Enter your password: ")
    login(name,password)
  else:
    print("Please enter you name and password to register")
    name = input("Enter your name: ")
    password = input("Enter a password: ")
    register(name,password)
    
begin()
acess()

if(granted):
  print("Welcome to the Great Bank")
  print("Username: ", name)
