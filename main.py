import requests

body = {"name": "morpheus",
        "job": "yut"}
get_info = requests.put("https://reqres.in/api/users/2", body)
response = get_info.status_code
print(get_info.json())
print(response)
