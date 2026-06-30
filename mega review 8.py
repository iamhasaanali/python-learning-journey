with open("/Users/hasaanali/Documents/megareview.txt", "w") as file:
    file.write("My name is Hasaan Al" + "\n")
    file.write("i am here for claude mega review" + "\n")


with open("/Users/hasaanali/Documents/megareview.txt", "r") as file:
    read = file.read()
    print(read)
