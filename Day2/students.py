import json
students=[
     {"ID":"1","Name":"Abdu","Course":"CSE"},
     {"ID":"2","Name":"Jacob","Course":"IT"},
     {"ID":"3","Name":"Ali","Course":"AD"},
     {"ID":"4","Name":"Sonu","Course":"CSE"},
     {"ID":"5","Name":"Boby","Course":"CIVIL"}
    ]
with open("students.json","w") as f:
    json.dump(students,f,indent=4)
with open ("students.json","r") as f:
    data=json.load(f)
for student in data:
    print(f"ID:{student['ID']}, Name:{student['Name']}, Course:{student['Course']}")