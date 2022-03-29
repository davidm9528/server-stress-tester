'''define a function prompt user to enter a number run an already existing python script the number of times the user enters open file instances in new command line windows'''
import os
print("How many clients would you like to run?")
amount = input("%")

def openfiles(numtimes):
    for X in range(numtimes):
        os.system("start /B start cmd.exe @cmd /k python client.py")
    print(amount + " clients opened...")

openfiles(numtimes=int(amount))