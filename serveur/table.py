users = {'0': {"name": "Mouloud", "conso": 5},
         '1': {"name": "Hamza", "conso": 3},
         '2': {"name": "Ulysse", "conso": 8}, 
         '3': {"name": "Elie", "conso": 7}, 
         '4': {"name": "Jean-Loup", "conso": 15}}

def addConso(id, value):
    users[id]["conso"] += value

def getConso(id):
    return users[id]["conso"]

def getMean():
    s = 0
    count = 0
    for _, value in users.items():
        s += value["conso"]
        count += 1
    return s / count

def getRank():
    sortedUsers = sorted(list(users.values()), key=lambda x:x["conso"])
    return [(x["name"], x["conso"]) for x in sortedUsers]