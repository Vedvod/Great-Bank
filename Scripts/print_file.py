import os

try:
  user
except:
  user=input("Which user? ")
try:
  number
except:
    number=int(input("What number? "))
while number>3 or number<0:
  number=input("The current value for number, {number} is invalid! Enter a new value.")
os.startfile(os.path.dirname(os.path.realpath(__file__))+f"/receipts/{user}/receipt {number}.txt", "print")
