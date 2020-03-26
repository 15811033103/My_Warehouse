import requests

url = 'https://www.baidu.com'
data = None

re = requests.get(url,data)
print(re)