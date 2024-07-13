# CSV to JSON Converter

This Flask application provides endpoints to convert CSV data into JSON format. It supports both file upload and direct data input via HTTP POST requests.

## Features

- **/convert_file Endpoint**: Upload a CSV file to convert it into JSON format.

curl example:
```bash
curl -X POST -F "file=@/path/to/your/file.csv" https://csv2json-ercr.onrender.com/convert_file
```

- **/convert_data Endpoint**: Send CSV data as a string in the request body to convert it into JSON format.

Python Example:
```python
url = 'https://csv2json-ercr.onrender.com/convert_data'
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
```

## Requirements

- Python 3.x
- Flask
- pandas


