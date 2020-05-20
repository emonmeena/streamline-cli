import requests
from bs4 import BeautifulSoup 
import webbrowser

url = 'https://nodejs.org/en/'

URL = {

}
r = requests.get(url)

htmlContent = r.content

soup = BeautifulSoup(htmlContent, 'html.parser')

A = soup.find("a", class_="home-downloadbutton")
versionDescription = A.get_text()

version = str(versionDescription)
version = version.lstrip()
currentVersion = version[0:7]
oldVersion = "12.16.2"
if(currentVersion != oldVersion):
    updateSystem = input("We found new update for Node.js  "+oldVersion+" LTS. Do you want to Update Node.js to "+currentVersion+" version yes (yes/no): ")
    if(updateSystem == "yes"):
        # print(updateSystem)
        webbrowser.open('https://nodejs.org/dist/v12.16.3/node-v12.16.3-x64.msi')
        oldVersion = currentVersion
print(oldVersion)


