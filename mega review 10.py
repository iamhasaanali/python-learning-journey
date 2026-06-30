name = input("What is you name? ")
score = int(input("Enter your score: "))
def grades(Score):
    if score >=90:
        return "A"
    elif score >=80:
        return "B"
    elif score >=70:
        return "C"
    elif score >=60:
        return "D"
    else:
        return "F"

print(name, "got", grades(score))