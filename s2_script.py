##NOTA UDS NECESITA INSTALAR pip install requests

import requests
import json

ip = input("Enter IP to Lookup: ")
url = f"https://ipapi.co/{ip.strip()}/json"

contents = requests.get(url)
print("----- RAW Output -----")
print(contents)
print("\n----- FORMATTED Output -----")
print(json.dumps(contents.json(), indent=4))
