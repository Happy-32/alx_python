import requests

request = requests.get("https://alu-intranet.hbtn.io/status")
# print(dir(request))
# statusCode = request.status_code
print("- type: ", type(request.text))
print("- content: ",request.text)