person = {
    "name" : "Hasaan Ali",
    "age" : 27,
    "city" : "Sydney"
}
if "name" in person:
    print("name exists", person["name"])

if "salary" in person:
    print("salary exists", person["salary"])
else:
    print("salary does not exist")
