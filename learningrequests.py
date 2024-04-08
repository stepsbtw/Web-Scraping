import requests

link = "https://www.google.com"

response = requests.get(link)
# requesting GET

print(response)

'''
if response.status_code == "200":
    print("ok")
else:
    print("error")
'''

if response:
    print("ok!")
else:
    raise Exception(f"error code: {response.status_code}")

print(response.content) # !!!!