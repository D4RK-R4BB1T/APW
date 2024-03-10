# Anti-Pedo Toolkit


![](https://i.imgur.com/YIYQulg.png)

Hopefully my final redo of this repo 3rd edition mistake: So, In the blacklist.txt I saved the wrong copy during my work I was using it to skip over duplicate links I've already scanned thus leading to me uploading around 5,000 Domains (Whoops) I've deleted the repo due to Commit History.

This tool kit aims to bring you some simplisitc ways to info gathering whist looking like an Utter skid. Who gives a shit how you go about taking down pedophiles or what not?

What does this contain? Some quickly generated scripts I was too lazy to do my damnself as I prefer GoLang to Python3. It's faster and generally better IMO. This focuses heavily on the tech illiterate side of darkest corners of the internet. Most pedophiles run MyBB which this aims for mostly.

I also left some powerhsell scripts and most should be pretty fucking simple. Some work best on Windows (PowerShell) meanwhile the Python3 is ready to use with an updated Kali VM (Which as I said, you're gonna look like a skid so just fucking embrace it).

## What can you expect: 

### html.py: 
Simple HTML to UID &  Display Name. Seperated by : e.g. 1:Pavel

### Sorter.ps1: 
As it sounds, Sorts & Removes Duplicates from .txt files

### Parser.ps1:

 Parses your CSV file by user Column then keyword. e.g. Col: Country, Keyword: RU (Dumps all results in Column "Country" and matching the keyword: RU, which is Russia Highly Effective for Exporting data to for Bulk IP Lookups/Parsing the CSV you got from a bulk lookup)

### Save.py 

Asks user to specify how many pages they wish to download from the /memberlist.php  this one may run into Legal Issues so I advise caution and proper protection.

### DS.py
Better known as "Domain Sorter" this fixes the issue with directories/docs/args/queries made in the URL by simply removing all that nonsense. e.g. example dot com/member.php?action=profile&amp;uid=1 well, this removes the /member.php?action=profile and leaves you with example dot com this makes using the Sorter.ps1 way easier.

### Cleanup.py 
Simply put it this way, it can process an entire directory and it's not fully functional  It'll remove strings (which, In my case is domains). This script is best used with lynx browser and another script I'll add below. Essentially, Like Maltego you can use Lynx a lightweight CLI based browser can utilized as a quick way to do an "External Link Transform" this allows you to quickly map out new domains and disgard of garbage e.g. wordpress.org and all those framework websites that are not involved in criminal activity.

The script also will allow you to dump links by files. This allows you to speed up the automation for finding 3rd party services or links that contain CSAM (Most is behind a paywall, so this makes it easier for law enforcement but can be easier to bulk report to the file sharing service/Image Hosting Provider e.g. Imgur)

It requres different files (which I'll add but most notably is blacklist.txt)

Options 4 & 5 May not work. THIS IS A DIRECTORY 

**THIS IS A DIRECTORY BASED SCRIPT, ENSURE YOU SEGERATE YOUR FILES BEFORE USING**

### lynx.ps1 
A Simple script made specifically for Debian Based Linux Machines, this assumes you have Lynx Browser installed it will ask to specify a .txt file to which you shall give and it'll export a text file now to which you can copy the output to a CLI and let lynx do it's business. It numbers the txt files by name. It's recommend you execute this from a new folder or you'll enjoy the cleanup of the cloned repo.

### Resources.txt
My Favorite links and tools for hunting

# Closing, Warning & Advice:
For legal reasons: I do not offer support, these scripts are offered as is. I, the creator do not want to know nor have any involvement to any degree in your usage of these scripts. I do not care, I don't wanna know . Use them at you own risk

I will recommend a strong VPN (e.g. Mulvad, paid with XMR or Cash).
For the best OPSEC: I Recommend a new laptop, with a 64 GB MicroSD Card (And Adapter), Encrypt your Laptop with full disk encryption & then your MicroSD card with full disk encryption.

Download Virtual Box, Ensure you tell your browser to "Ask where to download things to" then save your Bootable Disks and VM Files on your Encrypted MicroSD card. They're easy to swallow in a pinch. This tip is credited to /u/funshine of Dread and Hacktown. No writting to your main disk please.

Parser & Sorter: 1 of these fuckers will not open in CLI, So use Windows Powershell ISE. The Parser claims it allows JSON & TXT Input, It don't. It does export to JSON, TXT and CSV just doesn't import.

The rest of the tools may be weird, but I'm sure the dumbest of skids can figure out how shit works. Powershell = Windows, Python = Linux. 

Common Errors:
Execution Policy Error - Use google, Enable all
Missing (Instert random module here) pip install (whatever is missing here without the () )
PS CMD Insta closing: As I said, use the ISE.

Any other issues figure it out.

#Happy Hunting Follow us on Twitter
[D4RKR4BB1T47](http://twitter.com/D4RKR4BB1T47 "D4RKR4BB1T47")
[Creep Bin ](http://twitter.com/creep_bin "Creep Bin ")


# Evil Rabbit Security Inc: Thumping Pedophiles in the head Since 2013
[![](https://i.imgur.com/8G5bPmw.png)](https://i.imgur.com/8G5bPmw.png)
