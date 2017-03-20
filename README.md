# Chrome-Restrictions
## Synposis
A common issue in schools is students installing chrome extensions that either clog bandwidth, or are distracting to themselves and other students, and even teachers. A serious issue for out school is the use of VPN extensions, usually just for Netflix unblocking, but this means they can't use our proxy, and then can't browse the internet. Using [this](https://www.jamf.com/jamf-nation/discussions/22910/vpn) JAMF Nation  discussion as a base, I've made a python script to generate a PLIST with the whitelist of Extension IDs. This then gets uploaded to the JSS, and a configuration profile can be pushed out, preventing anything except the whitelisted extensions from being installed. This even has the benefit of preventing them installing extensions with their personal Google account

Once the profile is pushed out, it takes effect almost instantly, removing non-approved extensions
## Is This For Me
- If you are having troubles caused by students installing extensions, be it network or engagement based
- If you manage a fleet of iOS or OSX devices
- If you want greater control over what your students can install

 Then this is for you.

## Requirements
+ Python 3.x must be installed
+ If you want to do part 3 below, [pyperclip](https://github.com/asweigart/pyperclip) must be installed.
+ You must be using [JAMF](https://www.jamf.com/) software, specifically the JSS To manage your machines

## How To Use
- #### Running The Script
  1. Run `generatePLIST.py`, either via command line (`python3 generatePLIST.py`) or through IDLE (`F5`)
  2. When prompted with `Enter Name: `, enter the name of the extension. This is **solely** for your reference, so you can name them however you like
  3. When prompted with `Enter ID: `, you must enter the extenion ID **exactly** as it appears in the URL
  <br />
  For example, this is the URL for the [Hangouts](https://chrome.google.com/webstore/detail/google-hangouts/nckgahadagoaajjgafhacjanaoiihapd) extention: <br />![Google Hangouts](https://github.com/Franknsten/Chrome-Restrictions/blob/master/images/chromeStoreID.png)<br />
  The highlighted part, `nckgahadagoaajjgafhacjanaoiihapd` is the ID, and any extension will have a string like this in the URL
  4. Repeat this for each extension you wish to block
  5. When you are done, just submit two blank entries (for name and ID) to close
  6. This will create a file called `chromeProfile_vX.plist`, with X being the version. At the moment, it increments the version each time it gets run

  **NOTE** - You only need to do this to ADD extensions in. `extentionIDs.csv` stores all of the ones you have entered, and you can use this to see what is and isn't allowed to be installed

- #### Uploading to JSS
  1. Browse to https://your.jss.address:port/OSXConfigurationProfiles.html
  2. Create a new configuration profile<br />
  ![New config profile](https://github.com/Franknsten/Chrome-Restrictions/blob/master/images/newConfigProfile.png)<br />
  3. Give it a meaningful name and description<br />
  ![Name and description](https://github.com/Franknsten/Chrome-Restrictions/blob/master/images/nameDescription.png)<br />
  4. Under Custom Settings, add a Preference Domain of "com.google.Chrome" and upload `chromeProfile_vX.plist`
  5. The Custom Settings page should now appear like this<br/>
  ![Updated Custom Settings](https://github.com/Franknsten/Chrome-Restrictions/blob/master/images/updatedSettings.png)
  6. In the `Scope` tab, add the machines you want to be impacted by this profile
  7. Save

- #### Inform Users
  1. If you want to provide staff/students with a list of the allowed extensions, running `generateList.py` will copy a HTML unordered list to your clipboard, ready to be pasted into a document or a HTML compatible message
  2. The list items will display with the name of the extension you entered, and will link to the URL using the ID
    - `&lt;li>&lt;a href="https://chrome.google.com/webstore/detail/extensionID" >Extension Name &lt;/a>&lt;/li>`
  3. These are pulled from `extentionIDs.csv`, so it is important that you enter the data correctly

## Acknowledgements
