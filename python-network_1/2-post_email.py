import requests
import sys

data = {'email': sys.argv[2]}
request = requests.post(sys.argv[1], data=data)
# print(request.text)
