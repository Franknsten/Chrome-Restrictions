# Chrome-Restrictions
Generate plist with all extensions blacklisted and only allowed ones whitelisted

Requires Python

This is used in a JAMF environment, but I guess it can be applied to any environment using plists to restrict student abilities

USEAGE

Create New Configuration Profile
Call it something like 'Chrome Restrict Extensions', just so you know what it does
Under 'Custom Settings' Add:
Preference Domain: com.google.Chrome

Then upload the output plist of this script. It'll add something like 
{ExtensionInstallBlacklist=[*], ExtensionInstallWhitelist=[listOfIDs]} 
