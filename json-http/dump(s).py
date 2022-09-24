from json import dump
from json import dumps
from requests import get

responseObj = get("http://api.open-notify.org/astros.json")
print(responseObj)

jsonData = responseObj.json()
print(jsonData)

jsonStringData = dumps(jsonData)

with open("issAsttrosDumps.json", "w") as f:
    print("Writing the data to file...")
    print()
    f.write(jsonStringData)

jsonOutputFile = open("issAsttrosDumps.json", "w")
dump(jsonData, jsonOutputFile, indent=2) # dump(file_to_write, file_to_write_to)
jsonOutputFile.close()