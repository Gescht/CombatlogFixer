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
def guidShouldBeChanged(element):

    #the string inside the list is too short
    if len(element) <= 17:
        return False
    #number is not a GUID
    if "x" != element[1]:
        return False
    #sourceGUID is an npc
    if "F" == element[2]:
        return False
    #sourceGUID is already zero
    if "0" == element[3]:
        return False
    return True
with open(oldFileName, encoding="utf-8", errors='ignore') as old, open(newFileName, 'w', encoding="utf-8") as new:
    for line in old:
        line = line.split(",")
        for index, element in enumerate(line):
            if guidShouldBeChanged(element):
                line[index] = "0x0000" + line[index][6:]
        new.write(",".join(str(s) for s in line))