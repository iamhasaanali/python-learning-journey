words = ["python", "is", "great", "python", "is", "fun", "python"]

word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Word Count:", word_count)