import requests

url = 'https://www.w3schools.com/python/demopage.php'
myobj = {'somekey': 'somevalue'}
x = requests.post(url, json=myobj)
print(x.text)

#requests.post(url, data={key: value}, json={key: value}, args)