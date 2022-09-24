import requests

r = requests.get("https://xkcd.com/353/")
# print(dir(r)) --> attributes and object that we can access in this header
# print(r.text) --> gives the content of the response in unicode, html of the page

# downloading an image from a website:

i = requests.get("https://imgs.xkcd.com/comics/python.png")
with open("comic.png", "wb") as f: # wb - write byte mode
    f.write(i.content)

# 200s - success, 300s - redirect, 400s - client errors, 500s - server errors (site crashes etc)
print(r.status_code)
print(i.status_code)
# easier to check with booleans, returns true for anything lesser than 400:
print(r.ok)
print(i.ok)

print(r.headers)
print(i.headers)


payload = {"page": 2, "count": 25}
example = requests.get("https://httpbin.org/get", params=payload)
# print(example.text)
print(example.url)

"""
payload2 = {"username": "idilpo", "password": "idilpo"}
example2 = requests.post("https://httpbin.org/get", data=payload2)
print(example2.text)
ex2_dict = example2.json()
print(ex2_dict)
"""


