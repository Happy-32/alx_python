import requests

request = requests.get("https://alu-intranet.hbtn.io/status")
# print(dir(request))
# statusCode = request.status_code
# print("Body response:\n  - type:", type(request.text), "\n  - content:", request.text)
body_response = request.text[:2] + " " + request.text[2:]

print("Body response:\n  - type: {}\n  - content: {}".format(type(body_response), body_response))