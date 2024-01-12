import requests

pixela_endpoint = "https://pixe.la/v1/users"
name = "swati666"
token = "pixelajkjkjkk12345"


pixela_params = {
    "token": "pixelajkjkjkk12345",
    "username": "swati666",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# my_pixela_account = requests.post(url=pixela_endpoint, json=pixela_params)
# print(my_pixela_account.text)
# link- account = "https://pixe.la/@swati666"

secure_token = {
    "X-USER-TOKEN": token
}

graph_params = {
    "id": "swati",
    "name": "Study Hours",
    "unit": "hours",
    "type": "float",
    "color": "ajisai"
}

# graph_pixela = requests.post(url=f"https://pixe.la/v1/users/{name}/graphs", headers=secure_token, json=graph_params)
# print(graph_pixela.text)
# link_for_graph = https://pixe.la/v1/users/swati666/graphs/swati.html

graph_id = "swati"

add_pixel_params = {
   "date": "20240112",
   "quantity": "7.30",
}

add_pixel = requests.post(url=f"https://pixe.la/v1/users/{name}/graphs/{graph_id}",
                          json=add_pixel_params,
                          headers=secure_token)
print(add_pixel.text)