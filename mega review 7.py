try:
    score = int(input("Enter you score: "))
    if score >100 or score <0:
        print("Scores should be between 0 - 100")
    else:
        print("Score accepted", score)
except:
    print("Invalid entry")