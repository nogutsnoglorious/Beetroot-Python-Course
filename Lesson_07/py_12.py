visitors_list = [("192.168.0.1", 12), ("192.168.0.2", 4), ("192.168.0.3", 1), ("192.168.0.4", 19), ("192.168.0.5", 22), ("192.168.0.7", 10), ("192.168.0.7", 10)]
day = 0
night = 0
for i in visitors_list:
    if -1 < list(i)[1] < 6 or 17 < list(i)[1] < 24:
        night += 1
    if 5 < list(i)[1] < 19:
        day += 1
total_visits = day + night
if day >= night:
    print("The most popular time of visit is day")
else:
    print("The most popular time of visit is night")
print("Total visits quantity is", total_visits)