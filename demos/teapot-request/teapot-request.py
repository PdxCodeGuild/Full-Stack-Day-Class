import requests

teapot = requests.get('http://www.google.com')
print(teapot.text)
