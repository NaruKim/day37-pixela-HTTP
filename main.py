import requests
import datetime

now = datetime.datetime.now().date()


USERNAME = "naru"
TOKEN = "black5598"
GRAPHID = "graph1"

HEADERS = {
    "X-USER-TOKEN": TOKEN
}

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
# https://pixe.la/@naru


graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "graph1",
    "unit": "Km",
    "type": "float",
    "color": "kuro",
}


# response = requests.post(url=graph_endpoint, json=graph_config, headers=HEADERS)
# print(response.text)

# value_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"
#
# value_config = {
#     "date": ,
#     "quantity":,
# }

