import requests
import datetime

now = datetime.datetime.now().date()
TODAY = now.strftime('%Y%m%d') # C언어가 떠오르는 기법이다.
# today = datetime(year=2021, month=3, day=6)
# today.strftime('%Y%m%d')
CHANGE_DAY = 0 #yyyymmdd

USERNAME = "naru"
TOKEN = "black5598"
GRAPH_ID = "graph1"

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


value_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

value_quantity = "20"
value_config = {
    "date": TODAY,
    "quantity": input("KM : "),
}

# response = requests.post(url=value_endpoint, json=value_config, headers=HEADERS)
# print(response.text)


put_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{CHANGE_DAY}"

put_config = {
    "quantity": "15"
}

# response = requests.put(url=put_endpoint, json=put_config, headers=HEADERS)
# print(response.text)


delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{CHANGE_DAY}"

# response = requests.delete(url=delete_endpoint, headers=HEADERS)
# print(response.text)

