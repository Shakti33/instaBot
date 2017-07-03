import requests

g=requests.get("https://api.instagram.com/v1/users/self/?access_token=%s"%("4870715640.a48e759.874aba351e5147eca8a9d36b9688f494")).json()
print g