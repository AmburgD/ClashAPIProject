import json
import requests
from dotenv import load_dotenv
import os

import polars as pl
import pandas as pd
from pathlib import Path

load_dotenv()

KEY = os.getenv("API_KEY")
headers = {
    "Accept" : "applicatipon/json",
    "authorization" : "Bearer " + KEY
    }

def getPlayerDat(baseIDParse):
    
    playerData = requests.get("https://api.clashofclans.com/v1/players/"+baseIDParse, headers=headers)
    # print(playerData.json())

    playerResponse = playerData.json()

    # Open the file in write mode ('w')
    with open(r'CoC_Json\\CoC_Dat.json', 'w') as f:
        # Convert the response dictionary to a JSON-formatted string and write it to the file
        json.dump(playerResponse, f, indent=4)  # `indent=4` is optional; it just makes the JSON file readable
    clanTag = playerResponse['clan']['tag']
    clanName = playerResponse['clan']['name']
    return  clanTag, clanName

def getClan(clanNameParse, clanTag):
    clanData = requests.get("https://api.clashofclans.com/v1/clans?name=" + clanNameParse, headers=headers)

    clanResponse = clanData.json()

    for clan in clanResponse['items']:
        # print(clan['tag'])
        if(clan['tag'] == clanTag):
            # Open the file in write mode ('w')
            with open(r'CoC_Json\\CoC_Clan_Dat.json', 'w') as f:
                # Convert the response dictionary to a JSON-formatted string and write it to the file
                json.dump(clan, f, indent=4)  # `indent=4` is optional; it just makes the JSON file readable

def json_to_excel(json_path: str, excel_path: str, sheet_name: str = "Sheet1"):
    path = Path(json_path)

    # Attempt to read NDJSON
    try:
        df = pl.read_ndjson(path)
    except:
        # Fall back to standard JSON
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, dict):
            data = [data]
        df = pl.DataFrame(data)

    # Convert Polars DF to pandas and save as Excel
    df.to_pandas().to_excel(excel_path, index=False, sheet_name=sheet_name)