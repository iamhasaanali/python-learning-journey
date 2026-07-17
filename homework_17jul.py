from datetime import datetime
from dateutil.relativedelta import relativedelta

today = datetime.now()

movies = [
    {"title": "Inception", "release_date": datetime(2010, 7, 16), "genre": "Sci-Fi"},
    {"title": "The Dark Knight", "release_date": datetime(2008, 7, 18), "genre": "Action"},
    {"title": "Interstellar", "release_date": datetime(2014, 11, 7), "genre": "Sci-Fi"},
    {"title": "Avengers Endgame", "release_date": datetime(2019, 4, 26), "genre": "Action"},
    {"title": "Oppenheimer", "release_date": datetime(2023, 7, 21), "genre": "Drama"},
]
for movie in movies:
    name = movie["title"]
    date = movie["release_date"]
    difference = today - date
    days = difference.days
    print(f"{name} was released {days} ago!")
print("---------------------------------------------------")
for movie in movies:
    diff =  relativedelta(today,movie["release_date"])
    movie["age_year"] = diff.years
    print(f"{movie["title"]} is {diff.years} years old movie!")
print("---------------------------------------------------")
oldest = max(movies, key=lambda x:x["age_year"])
newest = min(movies, key=lambda x:x["age_year"])

print(f"Oldest movie: {oldest['title']} ({oldest['age_year']} years old)")
print(f"Newest movie: {newest['title']} ({newest['age_year']} years old)")
print("---------------------------------------------------")
def is_classic(movie):
    if movie["age_year"] > 10:
        return True
    else:
        return False
print("Classic movies:")
for movie in movies:
    if is_classic(movie):
        print(f"{movie['title']} is a classic!")
    