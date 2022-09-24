import json

people_string = """
{
    "people" : [
        {
            "name" : "John Smith",
            "phone" : "123-456-7890",
            "emails" : ["johnsmith@gmail.com", "johnsmith@workplace.com"],
            "has_licence" : false
        },
        
        {
            "name" : "Jane Doe",
            "phone" : "098-765-4321",
            "emails" : ["janedoe@gmail.com", "janedoe@workplace.com"],
            "has_licence" : true
        }
    ]
}
"""

data = json.loads(people_string)
print(type(data))
print(data)


print(type(data["people"]))
for p in data["people"]:
    print(p["name"])

for p in data["people"]:
    del p["phone"]
new_str = json.dumps(data)
print(new_str)

a_str = json.dumps(data, indent=2, sort_keys=True)
print(a_str)


