import requests
import sys

if len(sys.argv) < 3:
    print("Not enough arguments")
    sys.exit(1)

url = sys.argv[1]
email = sys.argv[2]

try:
    request = requests.post(url, {'email': email})
    # print("Email: ",request,email)

    if request.status_code == 200:
        print("success")
    else:
        print('Failed')
    
    print("{}".format(email))
    # pass
except requests.exceptions.RequestException as e:
    # print(e)
    pass