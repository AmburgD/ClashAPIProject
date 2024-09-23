import urllib.parse
import requests
from dotenv import load_dotenv
import os
import urllib
import pandas as pd
import json


load_dotenv()

KEY = os.getenv("API_KEY")

# print(KEY)

# Get the directory where the Python file is located
current_dir = os.path.dirname(os.path.abspath(__file__))

# Define the folder name you want to create
folder_name = 'CoC_Json'

# Combine the directory path with the folder name
folder_path = os.path.join(current_dir, folder_name)

# Create the folder if it doesn't already exist
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
    print(f"Folder '{folder_name}' created successfully!")
else:
    print(f"Folder '{folder_name}' already exists.")


headers = {
    "Accept" : "applicatipon/json",
    "authorization" : "Bearer " + KEY
}

baseID = "#QLCJYJLVJ"
baseIDParse = urllib.parse.quote(baseID)

def getPlayerDat(baseIDParse):
    # print (URL)
    playerData = requests.get("https://api.clashofclans.com/v1/players/"+baseIDParse, headers=headers)
    # print(playerData.json())

    playerResponse = playerData.json()

    # Open the file in write mode ('w')
    with open('CoC_Json\CoC_Dat.json', 'w') as f:
        # Convert the response dictionary to a JSON-formatted string and write it to the file
        json.dump(playerResponse, f, indent=4)  # `indent=4` is optional; it just makes the JSON file readable
    clanTag = playerResponse['clan']['tag']
    clanName = playerResponse['clan']['name']
    return  clanTag, clanName

# print(response['clan']['name'])
clanTag,clanName = getPlayerDat(baseIDParse)

clanNameParse = urllib.parse.quote(clanName)
print(clanNameParse)

def getClan(clanNameParse):
    clanData = requests.get("https://api.clashofclans.com/v1/clans?name=" + clanNameParse, headers=headers)

    clanResponse = clanData.json()

    for clan in clanResponse['items']:
        # print(clan['tag'])
        if(clan['tag'] == clanTag):
            # Open the file in write mode ('w')
            with open('CoC_Json\CoC_Clan_Dat.json', 'w') as f:
                # Convert the response dictionary to a JSON-formatted string and write it to the file
                json.dump(clan, f, indent=4)  # `indent=4` is optional; it just makes the JSON file readable

getClan(clanNameParse=clanNameParse)