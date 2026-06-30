number = {
    "Hasaan" : 90,
    "Ali" : 75,
    "Sara" : 45,
    "james" : 50
}
for key in number:
    if number[key] >50:
        print(key, ":", "Passed")
    else:
        print(key, ":", "Failed")
