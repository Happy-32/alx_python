import requests
import sys


# if len(sys.argv) < 2:
#     print("No result")
letter = sys.argv[1]

def search(letter):   
    url = "http://0.0.0.0:5000/search_user"

    data = {"q": letter}
    request = requests.post(url, data=data)
    try:
        json = request.json()
        if json:
            print("[{}] {}".format(json.get('id'), json.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")


    # try:
    #     request = requests.post(url, data=data)

    #     if request.status_code == 200:
    #         try:
    #             info = request.json()
    #             if info:
    #                 user_id = info.get('id')
    #                 user_name = info.get('name')
    #                 print("[{}] {}".format(user_id, user_name))
    #             else:
    #                 print("No result")
    #         except ValueError:
    #             print("Not a valid JSON")
    #     else:
    #         print("No result")

    # except requests.exceptions.RequestException as e:
    #     print("Request could not be made")

search(letter)