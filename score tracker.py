name = input("What is your name? ").title()
score = input("Whta is your score? ")
with open("/Users/hasaanali/Documents/score.txt", "a")as file:
    file.write(name + "\n")
    file.write(score + "\n")



with open("/Users/hasaanali/Documents/score.txt", "r")as file:
    content = file.read()
    print("---Your score ---")
    print(content)