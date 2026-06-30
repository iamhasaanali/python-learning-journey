person = {
    "hasaan" : "0413264859",
    "ali": "0429765478",
    "sara" : "0410987453"
}
print("---", "All Contscts", "---")
for key in person:
    print(key.title(), ":", person[key])

contact = input("Search Contact: ").lower()
if contact in person:
    print("Found!", contact.title(), "number is", person[contact])
else:
    print("Contact not found")