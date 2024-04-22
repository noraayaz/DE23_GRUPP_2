import requests

url = 'https://axmjqhyyjpat.objectstorage.eu-amsterdam-1.oci.customer-oci.com/n/axmjqhyyjpat/b/schoolbusiness-sharedfiles/o/profiles1.csv'
response = requests.get(url)
if response.status_code == 200:
    with open('profiles1.csv', 'wb') as f:
        f.write(response.content)
