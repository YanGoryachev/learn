from requests import post

a = post("http://127.0.0.1:8000/user/1", json={"id":1, "username":"yan"})
print(a.json())