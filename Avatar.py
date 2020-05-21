import requests
from bs4 import BeautifulSoup 
import webbrowser
import os
# import LogIn

print(" \t Welcome to Avatar ")
url = 'https://nodejs.org/en/'

stream = os.popen('Node -v')
output = stream.read()
output = output.strip()
# output = str(output)
# os.system('Node --version')
print(" Searching for any Tech Updates...")
try:
    r = requests.get(url)
except:
       romErr = input("\n Internet Connection is required \n"+" Hit Enter to exit Avatar")
htmlContent = r.content

soup = BeautifulSoup(htmlContent, 'html.parser')
A = soup.find("a", class_="home-downloadbutton")
versionDescription = A.get_text()
version = str(versionDescription)
version = version.lstrip()
currentVersion = "v"+version[0:7]
oldVersion = output

if(currentVersion != oldVersion and len(currentVersion) == len(oldVersion)):
    updateSystem = input(" We found new updates for NodeJS "+oldVersion+" Download "+currentVersion+" (yes/no): ")
    if(updateSystem == "yes"):
     try:
        downloadFile = webbrowser.open('https://nodejs.org/dist/v12.16.3/node-v12.16.3-x64.msi')
     except:
        romErr2 = input(" Oops! Internet Connection lost. Reconnect, than try again later \n")
    oldVersion = currentVersion

elif(currentVersion == oldVersion):
     exitKey = input(" NodeJS "+oldVersion+" is up to date"+'\n'+" Hit Enter to exit Avatar: ")

else: 
    downloadSystem = input(" \n Seems like You don't have NodeJS installed on your machine. Download latest release, NodeJS "+currentVersion+" (yes/no): ")
    if(downloadSystem == "yes"):
     try:
        downloadFile = webbrowser.open('https://nodejs.org/dist/v12.16.3/node-v12.16.3-x64.msi')
     except:
        romErr2 = input(" Oops! Internet Connection lost. Reconnect, then try. \n")
    oldVersion = currentVersion
print(" Closing Avatar")        



