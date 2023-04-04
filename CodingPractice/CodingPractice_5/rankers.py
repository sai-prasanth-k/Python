r = int(input())
top3 = r <= 3
top10 = r <= 10
if top3:
    print("One of Top 3")
elif top10 :
    print("Not Top 3 but One of Top 10")