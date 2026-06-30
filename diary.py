entry = input("What is on your mind today? ")
with open("/Users/hasaanali/Documents/diary.txt","a") as file:
    file.write(entry + "\n")
