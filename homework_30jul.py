from datetime import datetime
from dateutil.relativedelta import relativedelta
import pandas as pd

class Movie:
    def __init__ (self,title,genre,release_date,rating):
        self.title = title
        self.genre = genre
        self.release_date = release_date
        self.rating = rating
    def age_years(self):
        today = datetime.now()
        diff = relativedelta(today,self.release_date)
        return diff.years
    def is_classic(self):
        if self.age_years() > 10:
            return True
        else:
            return False
    def discounted_ticket(self):
        if self.is_classic():
            return f"$8"
        else:
            return f"$15"

m1 = Movie("Inception", "Sci-Fi", datetime(2010, 7, 16), 8.8)
m2 = Movie("Oppenheimer", "Drama", datetime(2023, 7, 21), 8.3)
m3 = Movie("The Dark Knight", "Action", datetime(2008, 7, 18), 9.0)
m4 = Movie("Dune Part 2", "Sci-Fi", datetime(2024, 3, 1), 8.5)

movies = [m1,m2,m3,m4]
data = []
for m in movies:
    data.append({
        "title": m.title,
        "genre": m.genre,
        "release_date": m. release_date,
        "rating": m.rating,
        "classic": m.is_classic(),
        "discount": m.discounted_ticket()
    })

df = pd.DataFrame(data)
print(df)
print("--------------------------")
print(df[df["classic"]])
print("--------------------------")
print(df.sort_values("rating", ascending=False))
