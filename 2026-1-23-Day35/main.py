import requests

url = "https://www.ymori.com/books/python2nen/test2.html"

response = requests.get(url)

response.encoding = response.apparent_encoding

print(response.text)
