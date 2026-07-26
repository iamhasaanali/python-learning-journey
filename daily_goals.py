from datetime import datetime
today = datetime.now().strftime("%d %B %Y")
goal = input("what is your goal for today? ")
with open("/Users/hasaanali/Documents/My_Learning/daily_goals.txt", "a") as file:
    file.write(f"{today} My goal for today: {goal}\n")

with open("/Users/hasaanali/Documents/My_Learning/daily_goals.txt", "r") as file:
    content = file.read()
    print("Goals:")
    print(f"{content}")