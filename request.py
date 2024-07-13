import requests
import sys

def test_data_post():
    url = 'http://localhost:5000/convert_data'
    csv_data = """Name,Age,City
    John,28,New York
    Alice,25,San Francisco
    Bob,30,Los Angeles"""

    try:
        response = requests.post(url, data=csv_data.encode('utf-8'))
        if response.status_code == 200:
            print(response.json())
        else:
            print(f"Request failed with status code {response.status_code}")
            print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Request error: {str(e)}")

def test_file_post():
    url = 'http://localhost:5000/convert'
    files = {'file': open('pepper.csv', 'rb')}

    response = requests.post(url, files=files)

    print(response.json())

if __name__ == "__main__":
    if sys.argv[1] == 1:
        test_file_post()
    else:
        test_data_post()