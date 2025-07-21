import urllib.parse
import urllib
import os
from clash_stat_functions import getClan, getPlayerDat, json_to_excel
from pathlib import Path

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




baseID = "#QLCJYJLVJ"



def main():
    baseIDParse = urllib.parse.quote(baseID)

    # print(response['clan']['name'])
    clanTag,clanName = getPlayerDat(baseIDParse)
    clanNameParse = urllib.parse.quote(clanName)
    # print(clanNameParse)
    getClan(clanNameParse, clanTag)
    json_to_excel(r'CoC_Json\\CoC_Dat.json', r'CoC_Json\\CoC_Dat.xlsx', sheet_name="PlayerData")
    json_to_excel(r'CoC_Json\\CoC_Clan_Dat.json', r'CoC_Json\\CoC_Clan_Dat.xlsx', sheet_name="ClanData")


if __name__ == "__main__":
    main()