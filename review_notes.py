#Mega Review Challenge 11 of 12

Notes = input("My Notes: ")
with open("/Users/hasaanali/Documents/My_Learning/review_notes.txt", "a") as file:
    file.write(Notes + "\n")








with open("/Users/hasaanali/Documents/review_notes.txt", "r") as file:
    content = file.read()
    print("Review Notes:")
    print(f"{content}")