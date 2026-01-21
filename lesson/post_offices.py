import requests

url = "https://api.postalpincode.in/pincode/533101"

headers = {
    "User-Agent": "curl/8.5.0",
    "Accept": "*/*",
    "Connection": "keep-alive"
}

response = requests.get(url, headers=headers, timeout=10)

data = response.json()

# write code to see the type/details in the variable 'data' and print the details.
# find the collections that are present in variable 'data' and get each details of the post offices present in the data.


