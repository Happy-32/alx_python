import requests
import sys

if len(sys.argv) < 2:
    print("Insufficient arguments")

url = sys.argv[1]

try:
    request = requests.get(url)
    stat_code = request.status_code
    if stat_code >= 400:
        print("Error Code: ",stat_code)
    if stat_code == 200:
        print("Regular request")
except:
    pass
