m = int(input())
dis1 = m >= 90
dis2 = m >= 50
dis3 = m < 50
if dis1 :
    print("Discount is 200")
elif dis2 :
    print("Discount is 100")
else :
    print("No Discount")