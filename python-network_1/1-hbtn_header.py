import requests
import sys

if len(sys.argv) < 2:
    print("Usage: python script.py <URL>")
    sys.exit(1)

url = sys.argv[1]

try:
    response = requests.get(url)

    x_request_id = response.headers.get("x-request-id")

    if x_request_id:
        print(x_request_id)
    
except requests.exceptions.RequestException as e:
    print(f"Error making the request: {e}")
