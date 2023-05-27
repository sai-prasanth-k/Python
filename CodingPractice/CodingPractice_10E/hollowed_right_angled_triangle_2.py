n = int(input())
for i in range(n+1):
    if i == 0 :
        print("_"*(n+1))
    else :
        forwardDash = "/"
        dash = "|"
        spaces = " "*(n-i)
        print(dash+spaces+forwardDash)