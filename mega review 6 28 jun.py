person = {
    "name" : "Hasaan",
    "job" : "IT",
    "salary" : 100000
}
for key in person:
    print(key, ":", person[key])
if "bonus" in person:
    print("bonus exists", person["bonus"])
else:
    print("bonus does not exist")