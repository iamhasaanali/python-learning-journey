hobbies=["cricket", "football", "running"]
for hobby in hobbies:
    print("i enjoy", hobby)
input1=input("what hobbies do you want to add? ")
input2=input("what hobbies do you want to remove? ")
hobbies.append(input1)
hobbies.remove(input2)
for hobby in hobbies:
    print("i enjoy", hobby)
print("i have", len(hobbies), "hobbies")

