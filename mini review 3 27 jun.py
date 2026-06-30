class Counter:
    total = 0

    def __init__(self):
        Counter.total += 1

c1 = Counter()
c2 = Counter()
c3 = Counter()

print(Counter.total)