def get_grades(score):
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
def get_status(score):
    if score >=50:
        return "PASS"
    else:
        return "FAIL"
def print_score(name,score):
    grade = get_grades(score)
    status = get_status(score)
    print("Student:", name)
    print("Score: ", score)
    print("Grade: ", grade)
    print("Status: ",status)
    print("---")
print_score("Sara", 72)

