import requests
import json


r = requests.get("https://candidate.hubteam.com/candidateTest/v3/problem/dataset?userKey=d91f73ac23623f7fbd86cd04ebf3")
print(r.status_code) # prints 200 if successfully ran
print(r.ok) # same function as above

jsonData = r.json()
# dumping json data into a file:
with open("partners_file.json", "w") as f:
    json.dump(jsonData, f, indent=2)
# reading data from file:
with open("partners_file.json", "r") as fr:
    partner_data = json.load(fr)


# creating needed structures from json data:
availability_dates = {}
partner_by_country = {}
for partner in partner_data["partners"]:
    partner_full_name = partner["firstName"] + " " + partner["lastName"]
    availability_dates[partner_full_name] = partner["availableDates"]
    country = partner["country"]
    available_dates = partner["availableDates"]
    partner_data = [country, *available_dates]
    partner_by_country[partner_full_name] = partner_data

# function that converts string into date:
def date_finder(d):
    year = int(d[:4])
    month = int(d[5:7])
    day = int(d[8:])
    full_date = [year, month, day]
    return full_date

# function that returns available dates for each person:
def availability(dict):
    available_people = {}
    for people, date in dict.items():
        for date1 in date:
            d1 = date_finder(date1)
            for date2 in date[1:]:
                d2 = date_finder(date2)

                if (d1[0] == d2[0]) and (d1[1] == d2[1]):
                    if (d1[2] + 1 == d2[2]) or (d1[2] - 1 == d2[2]):
                        dates = [d1, d2]
                        available_people[people] = dates
                else: continue
    return available_people


# available date count by country (TBC):
for p, c in partner_by_country.items():
    dates = {}
    US_availability = {}
    IE_availability = {}
    SP_availability = {}
    MEX_availability = {}
    CAN_availability = {}
    SIN_availability = {}
    JAP_availability = {}
    UK_availability = {}
    FRA_availability = {}

    if c[0]=="United States":
        # extracting the the dates from values
        dates[p] = c[1:]
        US_availability = availability(dates)
        UScount = []
        counter = 0
        for i in US_availability.values():
            for j in i:
                if j not in UScount:
                    UScount.append(j)
            counter += 1
        print(j, counter)
        #counter should add 1 for each date and add the date to the list if it's not already added
    elif c[0]=="Ireland":
        dates[p] = c[1:]
        IE_availability = availability(dates)
    elif c[0]=="Spain":
        dates[p] = c[1:]
        SP_availability = availability(dates)
    elif c[0]=="Mexico":
        dates[p] = c[1:]
        MEX_availability = availability(dates)
    elif c[0]=="Canada":
        dates[p] = c[1:]
        CAN_availability = availability(dates)
    elif c[0]=="Singapore":
        dates[p] = c[1:]
        SIN_availability = availability(dates)
    elif c[0]=="Japan":
        dates[p] = c[1:]
        JAP_availability = availability(dates)
    elif c[0]=="United Kingdom":
        dates[p] = c[1:]
        UK_availability = availability(dates)
    elif c[0] == "France":
        dates[p] = c[1:]
        FRA_availability = availability(dates)
    else: continue

with open("partners_availability.json", "w") as new_file:
    json.dump(availability_dates, new_file, indent=2)

#payload = #TODO
# API_ENDPOINT = "https://candidate.hubteam.com/candidateTest/v3/problem/result?userKey=d91f73ac23623f7fbd86cd04ebf3"
# API_KEY = "d91f73ac23623f7fbd86cd04ebf3"
# p = requests.post(url=API_ENDPOINT, data=API_KEY) #json=payload

