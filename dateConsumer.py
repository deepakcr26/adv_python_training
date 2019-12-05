from date import Date

today = Date()
iterToday = iter(today)

input()
while True:
    print(next(iterToday))
    input()
