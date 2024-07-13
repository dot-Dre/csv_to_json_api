import requests

url = 'http://localhost:5000/convert'
files = {'file': open('pepper.csv', 'rb')}

response = requests.post(url, files=files)

print(response.json())