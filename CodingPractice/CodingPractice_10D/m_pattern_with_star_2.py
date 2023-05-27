n = int(input())
for i in range(1,n+1):
    firstSpaces = " "*(n-i)
    firstStars = "* "*i
    firstPortion = firstSpaces+firstStars
    
    spaceBtw = " "*(n-i)
    
    secondSpaces = " "*(n-i)
    secondStars = "* "*i
    secondPortion = secondSpaces+secondStars
    
    print(firstPortion+spaceBtw+secondPortion)