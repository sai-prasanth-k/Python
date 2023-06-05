n =int(input())
for i in range(n):
    if i == 0 :
        stars = "* "*(i+1)
        print(stars)
    else :
        s = i + 1
        stars = "* "*(i+s)
        print(stars)