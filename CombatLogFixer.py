import sys
import os
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

#file path gained by dragging combatlog on .py
try:
    oldFileName = sys.argv[1]
except:
    oldFileName = filedialog.askopenfilename(title="Please select WoWCombatLog.txt")

print("CombatLog is getting fixed")
print("Please wait ...")
#new file path is in the same directory but with a different name
newFileName = os.path.dirname(os.path.abspath(oldFileName)) + "\\WoWCombatLog_fixed.txt"
def guidShouldBeChanged(listLines,index):

    #the string in the line List doesnt exist
    if len(listLines) <= index:
        return False
    #the string inside the list is too short
    if len(listLines[index]) <= 3:
        return False
    #number is not a GUID
    if "x" != listLines[index][1]:
        return False
    #sourceGUID is an npc
    if "F" == listLines[index][2]:
        return False
    #sourceGUID is already zero
    if "0" == listLines[index][3]:
        return False
    return True

with open(oldFileName) as old, open(newFileName, 'w') as new:
    for line in old:
        line = line.split(",", 12)
        if guidShouldBeChanged(line,1):
             line[1] = "0x0000" + line[1][6:]
        if guidShouldBeChanged(line,5):
             line[5] = "0x0000" + line[5][6:]
        if guidShouldBeChanged(line,9):
             line[9] = "0x0000" + line[9][6:]
        if guidShouldBeChanged(line,12):
             line[12] = "0x0000" + line[12][6:]
        new.write(",".join(str(s) for s in line))