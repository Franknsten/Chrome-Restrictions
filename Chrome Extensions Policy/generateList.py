#!/usr/bin/env python3
import csv
import pyperclip
allIDs = []
#Get names and ID's of extensions from file
with open('extensionIDs.csv', 'rt') as f:
    reader = csv.reader(f)
    for row in reader:
        if not row[0] == "Name":
            allIDs.append([row[0], row[1]])
        else:
            #update version each time program is run
            version = int(row[2]) + 1
f.close()
#string to hold the list and links
toCopy = '<ul>'

#generate list items with urls to chrome extensions on the list
for currID in allIDs:
    toCopy +='<li><a href="https://chrome.google.com/webstore/detail/' + currID[1] + '" target="_blank">' + currID[0] + "</a></li>"
toCopy += '</ul>'
pyperclip.copy(toCopy)
spam = pyperclip.paste()
print("The list of allowed extensions has been copied to your clipboard")
