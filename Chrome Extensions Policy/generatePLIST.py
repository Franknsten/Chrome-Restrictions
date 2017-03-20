#!/usr/bin/env python3
import csv
import os
##########
#Author: Isaac Wallis
#Date: March 20 2017
#Function: Create plist with whitelist of chrome extension IDs to allow
##########

#variables

#first half of the mobileconfig file
first = ''
#last half of the mobileconfig file
last = ''
#inputs from user
askingName = ''
askingID = ''
#next line to read
nextLine = ''
#list of all IDs
allIDs = []
#config version
version = ''
#Get cwd
realPath = os.path.realpath(__file__)
dirPath = os.path.dirname(realPath)

#read in list of OLD IDs from file "oldIDs.csv"
with open(dirPath + '/extensionIDs.csv', 'rt') as f:
    reader = csv.reader(f)
    for row in reader:
        if not row[0] == "Name":
            allIDs.append([row[0], row[1]])
        else:
            #update version each time program is run
            version = int(row[2]) + 1
f.close()

#get list of NEW IDs from user
askingName = input("Enter Name: ")
askingID = input("Enter ID: ")
while askingID:
    allIDs.append([askingName,askingID])
    askingName = input("Enter Name: ")
    askingID = input("Enter ID: ")


#set strings either side of the store IDs
first = '''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>ExtensionInstallWhitelist</key><array>'''
last = '''
</array><key>ExtensionInstallBlacklist</key>
<array>
            	<string>*</string>
        	</array>                          
	</dict>
</plist>
                                '''

#write to file
f = open(dirPath + "/ChromeProfile_v" + str(version) + ".txt", "w")
f.write(first)
for currID in allIDs:
    if not currID[1] == 'ID':
        f.write('''    <string>''')
        f.write(currID[1])
        f.write('''</string>''')                               
f.write(last)
f.close()

#rename txt to plist
configFileName = "ChromeProfile_v" + str(version) + ".txt"
newConfigFileName = "ChromeProfile_v" + str(version) + ".plist"
for filename in os.listdir(dirPath):
    if filename.startswith(configFileName):
        os.rename(dirPath + "/" + filename, dirPath + "/" + newConfigFileName)


#write IDs to file 
with open(dirPath + '/extensionIDs.csv', "wt") as file:
    writer = csv.writer(file, quoting=csv.QUOTE_ALL)
    writer.writerow(["Name","ID", version])
    for currID in allIDs:
        writer.writerow([currID[0], currID[1]])
                  


