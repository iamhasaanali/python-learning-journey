from datetime import datetime
from dateutil.relativedelta import relativedelta

today = datetime.now()

books = [
    {"title": "The Alchemist", "author": "Paulo Coelho", "year_published": datetime(1988, 1, 1), "rating": 4.7},
    {"title": "Atomic Habits", "author": "James Clear", "year_published": datetime(2018, 10, 16), "rating": 4.8},
    {"title": "Sapiens", "author": "Yuval Noah Harari", "year_published": datetime(2011, 1, 1), "rating": 4.4},
    {"title": "Rich Dad Poor Dad", "author": "Robert Kiyosaki", "year_published": datetime(1997, 4, 1), "rating": 4.2},
    {"title": "Deep Work", "author": "Cal Newport", "year_published": datetime(2016, 1, 5), "rating": 4.6},
]
for b in books:
    diff = relativedelta(today,b["year_published"])
    b["age"] = diff.years

oldest = max(books, key=lambda x: x["age"])
highest = max(books, key=lambda x: x["rating"])
print(f"{oldest["title"]} is the oldest book in the list")
print(f"{highest["title"]} is highest rated book in the list with ratings of {highest["rating"]}")
books.sort(key=lambda x: x["rating"], reverse=True)
for b in books:
    print(f"{b["title"]} : {b["rating"]}")

older_books = [b for b in books if b["age"] > 10]
for b in older_books:
    print(f"{b["title"]} is {b["age"]} years old book")


