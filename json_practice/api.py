import json
from urllib.request import urlopen

with urlopen("website-url") as response:
    source = response.read()

print(source) #this will print all the contents of the website

data = json.loads(source)
print(json.dumps(data, indent=2))


print(len(data["list"]["resources"])) # showing how many resources are there

usd_rates = dict()

for item in data['list']['resources']:
    name = item['resource']['fields']['name']
    price = item['resource']['fields']['price']
    usd_rates[name] = price

print(50 * float(usd_rates['USD/INR']))