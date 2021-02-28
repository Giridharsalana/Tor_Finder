import requests
import json

def Torrsearch(Query):

    api_url = "https://api.sumanjay.cf/torrent/?query="

    url = api_url + Query

    if Query:
        json_result = requests.get(url)
        if json_result.status_code == 526:
            return 'Error_Connect'
        else:
            return json_result.json()
    else:
        return 'No_Keyword'
