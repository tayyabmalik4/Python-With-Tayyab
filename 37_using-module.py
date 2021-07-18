# import random

# random_number = random.randint(0, 5)
# print(random_number)
# rand = random.random()*10
# print(rand)

# lst = ["tayyab","zahid","junaid","zulafqar","shahzab"]
# choice = random.choice(lst)
# print(choice)

import calendar

y = int(input("enter the year: "))
m = int(input("enter the month: "))
cal = calendar.month(y,m)
print(cal)