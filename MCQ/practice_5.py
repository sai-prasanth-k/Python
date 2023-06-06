# for i in range (2,5):
#     for j in range(1,3):
#         print("Programmer")
#     print("Happy Coding!")

# name1 = "Happy"
# name2 = "Coding"
# total = 1
# for a in name1:
#     for b in name2:
#         if a == b:
#             total = total + 1
# print(total)

# number = int(input())
# for i in range(0,number):
#     result = ""
#     res = number - i 
#     for j in range(res):
#         result = result + str(res)
#     print(result)

# for i in range(3,4):
#     print("Outer loop: "+str(i))
#     for j in range(0,i):
#         print(" Inner loop: "+str(j))


# text = input()
# count = 0
# for i in range(0,len(text)):
#     for j in range(0,len(text)):
#         if i == j :
#             count = count + 1
# print(count)


# name = ""
# for i in range(3,5):
#     for j in range(3,5):
#         name = name + str(j)
#     print(name)


# for i in range(1,3):
#     print("Outer loop: "+str(i))
#     for j in range(0,2):
#         print("Inner loop: "+str(j))
#     print("End")

# text1 = "b"
# text2 = "B"
# for i in range(2,len(text1)):
#     print("Hello")
#     for j in range(0,len(text2)):
#         print("CCBPians")
# print("Done!")

# for i in range(0,1):
#     for j in range(1,3):
#         print(i)

# k = 0
# while k < 3 :
#     l = 3
#     while l < 3 :
#         print(k)
#         l = l + 1
#     k = k + 1


# for i in range(3,4):
#     for j in range(1,2):
#         print("CCBPians")

# for i in range(1,10):
#     for j in range(0,0):
#         print("Take Care")


# number = int(input())
# for i in range(1,2):
#     k = number - 1
#     while(k >= 0):
#         spaces = " "* k
#         stars = "* "*(i-1)+"*"
#         k = k -1 
#     print(spaces + stars)


# result1  = 1
# result2 = 1 
# for i in range(5,8):
#     j = 2
#     while(j < 6):
#         if i < j:
#             result2 = result2 + 1
#         else :
#             result1 = result1 + 1
#         j = j + 1
# print(result2)
# print(result1)


# i = 0
# count = 1

# while ( i < 3 ):
#     j = 2 
#     while(j < 3):
#         if (i ** j)< 6:
#             count = count + 1
#         j = j + 1
#     i = i +1
# print(count)

# for i in range(0):
#     result = 1
#     for j in range (5,8):
#         result = result + j
#         if result < 0:
#             print(result)

# for i in range(3,4):
#     for j in range(3,4):
#         if (i == j):
#             print("Square of"+str(i)+" is"+str(i*i))


# for i in range(0,0):
#     print("Happy")
#     for j in range:
#         print("Coding")

# i = 3 
# while ( i < 6):
#     for j in range(5,6):
#         if j % i == 0:
#             print(str(j)+" "+str(i))
#     i = i + 1

pattern = ""
for i in range(1,3):
    pattern = ""
    for j in range(1,i+1):
        if(j == 1):
            pattern = pattern + str(j)
        else:
            pattern = pattern + str(j)+" "
    print(pattern)