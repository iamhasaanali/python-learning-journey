def get_info(name,score):
    grade = "pass" if score >=50 else "fail"
    return name,grade

student, result = get_info("Ali", 35)
print(student, ":", result)