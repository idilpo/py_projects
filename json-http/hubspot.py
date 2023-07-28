import requests
import json

r = requests.get("")
print(r.status_code)
print(r.ok)

jsonData = r.json()
print(jsonData)

jsonStringData = json.dumps(jsonData)

with open("issAsttrosDumps.json", "w") as f:
    print("Writing the data to file...")
    print()
    f.write(jsonStringData)

jsonOutputFile = open("issAsttrosDumps.json", "w")
json.dump(jsonData, jsonOutputFile, indent=2) # dump(file_to_write, file_to_write_to)
jsonOutputFile.close()



API_ENDPOINT = "http://pastebin.com/api/api_post.php"
API_KEY = "d91f73ac23623f7fbd86cd04ebf3"

source_code = '''
print("Hello, world!")
a = 1
b = 2
print(a + b)
'''

# data to be sent to api
data = {'api_dev_key': API_KEY,
        'api_option': 'paste',
        'api_paste_code': source_code,
        'api_paste_format': 'python'}

# sending post request and saving response as response object
p1 = requests.post(url=API_ENDPOINT, data=data)
# in reponse to this, the server processes the data sent to it and sends the pastebin URL
# of your source_code which can be simply accessed by r.text
# extracting response text:
pastebin_url = p1.text
print("The pastebin URL is:%s" % pastebin_url)



payload = {"username": "idilpo", "password": "idilpo"}
p = requests.post("https://httpbin.org/get", data=payload)
print(p.text)
p_dict = p.json()
print(p_dict)

print(p.status_code)
print(p.ok)

print(p1.status_code)
print(p1.ok)




for person in availability_dates.items():
    available_two_dates_in_row[person] =

for date1 in availability_dates.values():
    for date2 availability_dates.values():
        if date1[6] == date2[6]:
            if (date1[8:] + 1 == date2[8:]) or (date1[8:] - 1 == date2[8:]):
                two_dates_in_row.append(date1)
        elif (date1[6] + 1 == date2[6]) or (date1[6] - 1 == date2[6]):

        else:
            continue