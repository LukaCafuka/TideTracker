import requests


# Copernicus Data Space API base URL
base_url = 'https://catalogue.dataspace.copernicus.eu/odata/v1/Products'

# Define your query parameters to search for sea level data
params = {
    '$filter': "startswith(Name,'S6') and ContentDate/Start ge 2023-01-01 and ContentDate/End le 2024-01-01"
}

# Make the request to fetch the sea level data products
response = requests.get(base_url, params=params)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()['value']

    for item in data:
        print(f"Product Name: {item['Name']}")
        # print(f"Download URL: {item['__metadata']['media_src']}\n")
else:
    print(f"Failed to retrieve data: {response.status_code}")