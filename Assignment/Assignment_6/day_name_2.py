d = input()
n = int(input())
if d == "Monday" :
    day = 1
elif d == "Tuesday" :
    day = 2
elif d == "Wednesday" :
    day = 3
elif d == "Thursday" :
    day = 4 
elif d == "Friday" :
    day = 5
elif d == "Saturday" :
    day = 6 
elif d == "Sunday" :
    day = 7

target_day = day+n-1
target_day = target_day%7 

if target_day == 1 :
    print("Monday")
elif target_day == 2 :
    print("Tuesday")
elif target_day == 3 :
    print("Wednesday")
elif target_day == 4 :
    print("Thursday")
elif target_day == 5 :
    print("Friday")
elif target_day == 6 :
    print("Saturday")
elif target_day == 7 :
    print("Sunday")