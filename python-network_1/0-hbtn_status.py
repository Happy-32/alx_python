import requests

try:
    request = requests.get("https://alu-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type:", type(request.text))
    print("\t- content:", request.text)
    # print(dir(request))
    # statusCode = request.status_code
    # print("Body response:\n  - type:", type(request.text), "\n  - content:", request.text)
except requests.exceptions.RequestException as e:
    print(e)