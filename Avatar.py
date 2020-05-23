import requests
from bs4 import BeautifulSoup 
import webbrowser
import os
# import LogIn

print(" \t Welcome to Avatar ")
urlSite = 'https://nodejs.org/en/'
techStatus = " Searching for new Tech Updates..."
# System Config
stream = os.popen('Node -v')
output = stream.read()
output = output.strip()
# output = str(output)
# os.system('Node --version')
print(techStatus)
try:
    r = requests.get(urlSite)
except:
       romErr = input("\n Internet Connection is required \n"+" Hit Enter to exit Avatar")
htmlContent = r.content

# Web-Scraping
soup = BeautifulSoup(htmlContent, 'html.parser')
A = soup.find("a", class_="home-downloadbutton")
versionDescription = A.get_text()
version = str(versionDescription)
version = version.lstrip()
currentVersion = "v"+version[0:7]
oldVersion = output
urlDownload = 'https://nodejs.org/dist/'+currentVersion+'/node-'+currentVersion+'-x64.msi'

# Defining Input Strings
errorConnection = " Oops! Internet Connection lost. Reconnect, then try. \n"
noUpdaterequire = " NodeJS "+oldVersion+" is up to date"+'\n'+" Hit Enter to exit Avatar: "
update = " We found new updates for NodeJS "+oldVersion+" Download "+currentVersion+" (yes/no): "
noMatchtoDownload = " \n Seems like NodeJS is not installed in this machine. Install or Download the latest release, NodeJS "+currentVersion+" (yes/no): "

# Checking for Updates
if(currentVersion != oldVersion and len(currentVersion) == len(oldVersion)):
    updateSystem = input(update)
    if(updateSystem == "yes"):
     try:
        downloadFile = webbrowser.open(urlDownload)
     except:
        romErr2 = input(errorConnection)
    oldVersion = currentVersion

elif(currentVersion == oldVersion):
     exitKey = input(noUpdaterequire)

else: 
    downloadSystem = input(noMatchtoDownload)
    if(downloadSystem == "yes"):
     try:
        downloadFile = webbrowser.open(urlDownload)
     except:
        romErr2 = input(errorConnection)
    oldVersion = currentVersion
#Closing Avatar 
print(" Closing Avatar")        


         
