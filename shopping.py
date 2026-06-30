shopping=[]
for i in range(4):
    item= input("enetr item to the shopping list: ")
    shopping.append(item)
for i in range(len(shopping)):
    print(i + 1, shopping[i])

