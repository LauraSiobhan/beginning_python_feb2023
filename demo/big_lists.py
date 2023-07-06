from datetime import datetime

big_list = range(10000000)

earlier = datetime.now()
result = 10000001 in big_list
later = datetime.now()
delta = later - earlier
print('"in" test ran in {} seconds and {} microseconds'.format(delta.seconds, delta.microseconds))

earlier = datetime.now()
for num in big_list:
    if num == 10000001:
        result = True
later = datetime.now()
delta = later - earlier
print('"for" test ran in {} seconds and {} microseconds'.format(delta.seconds, delta.microseconds))
