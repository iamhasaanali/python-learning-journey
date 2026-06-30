class book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
    def read(self, pages_read):
        self.pages = self.pages - pages_read
        print("I have read", pages_read, "pages of", self.title)
        print("remaining pages are", self.pages)

b1 = book("Metamorphosis", 200)
b1.read(50)
b1.read(30)

