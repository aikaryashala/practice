# post_offices.py file
```py
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

```
Use curl command to download this file.

```bash
curl https://raw.githubusercontent.com/aikaryashala/practice/refs/heads/main/lesson/post_offices.py -o post_offices.py
```