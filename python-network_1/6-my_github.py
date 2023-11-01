import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("No Result")

    username = sys.argv[1]
    password = sys.argv[2]


# print("{}:{}".format(username, password))

def getCredentials():
    url = "https://api.github.com/users/{}".format(username)

    headers = {
        "Authorization": "Bearer {}".format(password)
    }
    try:
        request = requests.get(url, headers=headers)
        # print(dir(request))
        if request.status_code == 200:
            # print("success")
            data = request.json()
            print(data['id'])
        else:
            print("failure")
    except requests.exceptions.RequestException as e:
        print("Request could not be made")

getCredentials()