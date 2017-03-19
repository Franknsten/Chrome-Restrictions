# Chrome-Restrictions
Generate plist with all extensions blacklisted and only allowed ones whitelisted

Requires Python

This is used in a JAMF environment, but I guess it can be applied to any environment using plists to restrict student abilities

USEAGE
Part 1 - Script
Run the generatePLIST.py script
At the prompt 'Enter Name: ', enter the name of the extension. This is only so its easy for you to search through the allowed extension csv and remove/change things, so it doesn't need to be the exact Chrome Store™ name
At the prompt 'Enter ID: ', enter the EXACT id from the Chrome Store™ (Random string in URL. For example, the Hangouts Extension URL is https://chrome.google.com/webstore/detail/google-hangouts/nckgahadagoaajjgafhacjanaoiihapd so the ID is nckgahadagoaajjgafhacjanaoiihapd

This is what is used in the Whitelist, so you need to make sure this is correct

Part 2 - JAMF
Create New Configuration Profile
Call it something like 'Chrome Restrict Extensions', just so you know what it does
Under 'Custom Settings' Add:
Preference Domain: com.google.Chrome

Then upload the output plist of this script. It'll add something like 
{ExtensionInstallBlacklist=[*], ExtensionInstallWhitelist=[listOfIDs]} 

Add the relevant groups to the schope of the profile, then push out. When you add new plist, just push out to all devices whe nprompted

Part 3 - Distribute List (Optional)
If you want to communicate this to students/staff, run the generateList.py script. This requires pypercut (https://github.com/asweigart/pyperclip)

This will copy the entire unordered list to your clipboard, so just paste into a message that supports HTML, or just a webpage
Each item in the list will be the name of the extension you provided, which acts as a link to the Chrome Store with the ID you provided
