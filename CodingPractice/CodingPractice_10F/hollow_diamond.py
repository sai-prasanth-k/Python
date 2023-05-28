n = int(input())
spaceCount = n -1 
space = " "*spaceCount
firstrow = space+"*"
print(firstrow)

hollowCount = -1 
for i in range(2,n+1):
    spaceCount = n - i
    space = " "*spaceCount
    
    hollowCount = hollowCount+2
    hollowSpace = " "*hollowCount
    row = space +"*"+hollowSpace+"*"
    print(row)
    
for i in range(1,n-1):
    spaceCount = i
    space = " "*spaceCount
    
    hollowCount = hollowCount-2
    hollowSpace = " "*hollowCount
    
    row = space+"*"+hollowSpace+"*"
    print(row)
    
spaceCount = n -1
space = " "*spaceCount
last_row = space+"*"
print(last_row)



# Understanding the problem:

# Here we need to print the diamond pattern of 2N - 1 rows using the asterisk character (*).

# let us consider N = 5 so need to print 5 (i.e., 2*(5)-1) rows using the asterisk character (*).

#     *
#    * *
#   *   *
#  *     *
# *       *
#  *     *
#   *   *
#    * *
#     *
# Code:

# Let us break the pattern in to two parts 

# single star
# Upper part
# lower part
# Single star:

# As we observe the pattern there is a single star (*) at the first row and the last row which contains n-1  white spaces followed by one star(*) 

# left_spaces_count = n - 1  
# left_spaces = " " * left_spaces_count
# row_output = left_spaces + "*"
# print(row_output)
# Upper part:

# To print the upper half triangle, we need to know the number of left spaces to give and the number of stars to print in each line.

# You can notice from observing the pattern that we need to give n-1 spaces in the first line and print one star. In the subsequent lines, we need to reduce the number of spaces and increase the number of stars. This would print the upper half of the triangle. Here we need to White spaces (" ") between the stars. For the upper part , the hollow spaces should be increased by 2 initially let us assume 

# hollow_spaces_count = -1
# for row in range(2, n + 1): # Upper Part
#     left_spaces_count = n - row
#     left_spaces = " " * left_spaces_count
#     hollow_spaces_count = hollow_spaces_count + 2
#     hollow_spaces = " " * hollow_spaces_count
#     row_output = left_spaces + "*" + hollow_spaces + "*"
#     print(row_output)
# For 1st iteration:

# row =2

# left_sapce count = 5 - 2 => left_space_count = 3

# left_spaces = " " *3 

# hollow_spaces_count = hollow_spaces_count + 2 => -1 + 2 => 1

# hollow_spaces = " " * hollow_spaces_count => " " * 1

# row_output = left_spaces + "*" + hollow_spaces + "*"

# So, it print the pattern with 3 left spaces followed by one star(*) follwed by 1 hollow space follow by one star (*) 

# For 2nd iteration:

# row =3

# left_sapce count = 5 - 3 => left_space_count = 2

# left_spaces = " " *2

# hollow_spaces_count = hollow_spaces_count + 2 => 1 + 2 => 3

# hollow_spaces = " " * hollow_spaces_count => " " * 3

# row_output = left_spaces + "*" + hollow_spaces + "*"

# So, it print the pattern with 2 left spaces followed by one star(*) follwed by 3 hollow space follow by one star (*)  

# For 3rd iteration:

# row =4

# left_sapce count = 5 - 4 => left_space_count = 1

# left_spaces = " " *1 

# hollow_spaces_count = hollow_spaces_count + 2 => 3 + 2 => 5

# hollow_spaces = " " * hollow_spaces_count => " " * 5

# row_output = left_spaces + "*" + hollow_spaces + "*"

# So, it print the pattern with 1 left spaces followed by one star(*) follwed by 5 hollow space follow by one star (*) 

# Lower Part:

# Similarly, To print the lower half we need to repeat the same in a reverse way i.e., the spaces before the stars should increase and spaces between the stars are decreased by 2 . 

# for row in range(1, n - 1): # Lower Part
#     left_spaces_count = row
#     left_spaces = " " * left_spaces_count

#     hollow_spaces_count = hollow_spaces_count - 2
#     hollow_spaces = " " * hollow_spaces_count
#     row_output = left_spaces + "*" + hollow_spaces + "*"
#     print(row_output)
# For 1st iteration:

# row =1

# left_sapce count = 1 => left_space_count = 1

# left_spaces = " " *1 

# hollow_spaces_count = hollow_spaces_count - 2 => 5 -2 => 3

# hollow_spaces = " " * hollow_spaces_count => " " * 3

# row_output = left_spaces + "*" + hollow_spaces + "*"

# So, it print the pattern with 1 left spaces followed by one star(*) follwed by 3 hollow space follow by one star (*) 

# Similarly for the remaining iterations