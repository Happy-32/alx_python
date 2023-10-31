import requests

request = requests.get("https://alu-intranet.hbtn.io/status")
# print(dir(request))
# statusCode = request.status_code
print("Body response: \n        - type: ", type(request.text),"\n        -content: ", request.text)