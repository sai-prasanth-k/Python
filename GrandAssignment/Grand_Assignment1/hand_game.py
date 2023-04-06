s1 = input()
s2= input()
rock = "Rock"
paper = "Paper"
scissor = "Scissors"
if s1 == rock and s2 == rock or s1 == paper and s2 == paper or s1 == scissor and s2 == scissor:
    print("Tie")
elif s1 == rock and s2 == scissor or s1 == paper and s2 == rock or s1 == scissor and s2 == paper :
    print("Abhinav Wins")
else :
    print("Anjali Wins")