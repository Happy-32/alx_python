import requests, sys

# print(sys.argv[1])
request = requests.get(sys.argv[1])
# print(dir(request))
print(request.headers["x-request-id"])

