while True:
    try:
        score = int(input("Enter your test score: "))
        if score > 100 or score < 0:
            print("Score should be between o to 100 ")
        else:
            print("Score accepted:", score)
            break
    except:
        print("Please enter a valid number")
