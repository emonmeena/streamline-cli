import requests
from bs4 import BeautifulSoup 
import webbrowser
import os

url = 'https://nodejs.org/en/'
stream = os.popen('Node -v')
output = stream.read()
# os.system('Node --version')
print("Searching for Updates...")
r = requests.get(url)
htmlContent = r.content

soup = BeautifulSoup(htmlContent, 'html.parser')
A = soup.find("a", class_="home-downloadbutton")
versionDescription = A.get_text()
version = str(versionDescription)
version = version.lstrip()
currentVersion = version[0:7]
oldVersion = "12.16.3"

if(currentVersion != oldVersion):
    updateSystem = input("We found new update for NodeJS "+oldVersion+". Download v"+currentVersion+" yes (yes/no): ")
    if(updateSystem == "yes"):
        webbrowser.open('https://nodejs.org/dist/v12.16.3/node-v12.16.3-x64.msi')
        oldVersion = currentVersion
else : exitKey = input("No Updates available for NodeJS "+output+'\n'+"Hit Enter to exit Avatar: ")

print("Closing Avatar")        



