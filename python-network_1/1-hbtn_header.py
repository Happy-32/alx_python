import requests
import sys

if len(sys.argv) < 2:
    print("Insufficient number of arguments\nTry python3 script_name.py url")
    sys.exit(1)

url = sys.argv[1]

try:
    request = requests.get(url)

    x_request_id = request.headers.get("x-request-id")

    if x_request_id:
        print(x_request_id)
    
except requests.exceptions.RequestException as e:
    pass
