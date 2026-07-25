import pandas as pd
students = pd.DataFrame({
    "name": ["Hasaan", "Ali", "Sara", "Ahmed", "Fatima"],
    "course_id": [1, 2, 1, 3, 5],
    "score": [85, 92, 78, 95, 88]
})

courses = pd.DataFrame({
    "course_id": [1, 2, 3, 4],
    "course_name": ["Python", "Data Science", "ML", "SQL"],
    "instructor": ["Mr. Khan", "Ms. Smith", "Mr. Ali", "Ms. Jones"]
})
merged =pd.merge(students,courses, on="course_id") 
valid_course = pd.merge(students,courses, on="course_id", how="inner")
print("\n List of student with valid courses")
print(valid_course)
missing_course = pd.merge(students,courses, on="course_id", how="left")
print("\n Student missing courses")
print(missing_course)
no_student = pd.merge(students,courses, on="course_id", how="right")
print("\n Course with no student")
print(no_student)
print("---------------------------")
print(merged.pivot_table(values="score", index="course_name", aggfunc="mean"))
print("---------------------------")
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 50:
        return "C"
    else:
        return "F"
merged["grade"] = merged["score"].apply(get_grade)
print(merged)
print("---------------------------")
print(merged.pivot_table(values="grade", index="course_name", aggfunc="count"))