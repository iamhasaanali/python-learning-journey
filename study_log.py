from datetime import datetime
today = datetime.now().strftime("%d %B %Y")
study_log = input("How many hours did you study today? ")
with open("/Users/hasaanali/Documents/My_Learning/study_log.txt", "a") as file:
    file.write(f"{today} — Studied {study_log} hours\n")








with open("/Users/hasaanali/Documents/My_Learning/study_log.txt", "r") as file:
    content = file.read()
    print("Study Log:")
    print(f"{content}")