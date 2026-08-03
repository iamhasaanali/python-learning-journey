from datetime import datetime
today = datetime.now().strftime("%d %B %Y")
journla = input("Enter your journal entry: ")
with open("Users/hasaanali/Documents/My_Learning/mega_review_journal03aug.txt", "a") as file:
    file.write(f"{today} : {journla}\n")

with open("Users/hasaanali/Documents/My_Learning/mega_review_journal03aug.txt", "r") as file:
    content = file.read()
    print(content)