dictionary = {
    "python": "a programming language",
    "function": "a reusable block of code",
    "loop": "repeating a block of code",
    "list": "a collection of items",
    "dictionary": "a collection of key value pairs"
}
word = input("Enter a word: ")
if word in dictionary:
    print("It is", dictionary[word])