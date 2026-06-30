class counter:
    total_count = 0

    def __init__(self, name):
        self.name = name
        counter.total_count += 1

c1 = counter("First")
c2 = counter("Second")
c3 = counter("Third")
c4 = counter("FFFF")

print(counter.total_count)