import time
timestamp=time.strftime('%H:%M:%S')
print(timestamp)
# if timestamp('%H',range(0-12)):
#     print("GoodMorning")
# else:
#     print("Good afternoon")
timestamp=int(time.strftime('%H'))
# print(timestamp)

if timestamp in range(20,24):
        print("please sleep sir, Goodnight")
elif timestamp in range(4,8):
    print("Good morning sir, please goto college")
elif timestamp in range(13,15):
    print("Good afternoon sir, please take lunch on time")
elif timestamp in range(13,14):
    print("Sir please go to python class")