import requests
import json

token = "secret_unYvXwSFFYT5sFFaA8OOrB4TMm4ZpHdKnrIV0sNSiMi"

database_id = "22758adf0a3347d392d50886b5809ef8"
view_id = "bdbb3bb057fd4955874b24c3e0433104"


headers = {
    "Authorization": "Bearer " + token,
    "Notion-Version": "2021-05-13"
    }

def read_database(database_id, headers):
    read_url = f"https://api.notion.com/v1/databases/{database_id}/query"
    
    res = requests.request("POST", read_url, headers=headers)
    print(res.status_code)
    # print(res.text)
    data = res.json()

    with open("./db.json", 'w', encoding='utf8') as json_file:
        json.dump(data, json_file, ensure_ascii=False)

read_database(database_id, headers)
