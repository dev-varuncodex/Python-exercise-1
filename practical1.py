# numbers=[4,2,6,7,3,5,8,10,6,1,9,2]
# square=0
# sqaures=[]
# for value in numbers:                                         # for loop
#     square=value**2
#     sqaures.append(square)
# print("the list of sqaures is : ",sqaures)
#------------------------------------------------
# string="python Loop"
# for s in string:
#     if s=="o":                                                # else in for loop
#         print("if block")
# else:
#     print(s)
#------------------------------------------
# print(range(15))
# print(list(range(15)))
# print(list(range(4,9)))                                       # range in python
# print(list(range(5,25,4)))
#------------------------------------------
# tuple=("python","loop","sequence","condition","range")
# for i in range(len(tuple)):                                   # making .upper using range
#     print(tuple[i].upper())
#------------------------------------------
# a=int(input("Enter the number"))
# b=0
# for i in range(0,a+1):                                        # sum of natural number
#     b=b+i
# print(b)
#--------------------------------------------
# a=int(input("Enter the number : "))
# c=int(input("Enter the number : "))
# b=0                                                           # multiplication table
# for i in range(1,c+1):
#     b=i*a
#     print(i," * ",a," = ",b)
#------------------------------------------------
# a=int(input("Enter the number : "))
# fact=1
# for i in range(1,a+1):                                        # factorial 
#     fact=fact*i
# print("factorial : ",fact)
#------------------------------------------------
# a=int(input("Enter the number : "))
# b=0
# c=1
# d=0
# z=[]
# z.append(b)                                           
# z.append(c)                                                   # aanocii series 3 variations
# for i in range(1,a+1):
#     d=b+c
#     b=c
#     c=d
#     z.append(d)
# print(z)

# a=int(input("Enter the number : "))
# b=0
# c=1
# d=0
# z=[]
# z.append(b)
# z.append(c)
# for i in range(1,a-1):
#     d=b+c
#     b=c
#     c=d
#     z.append(d)
# print(z)


# a=int(input("Enter the number : "))
# b=0
# c=1
# d=0
# z=[]
# z.append(b)
# z.append(c)
# for i in range(1,a+1):
#     d=b+c
#     b=c
#     c=d
#     if d<=a:
#         z.append(d)
# print(z)
#--------------------------------------------------
# name = input("What is your name : ")
# age = int(input("How old are you : "))                          # task 3       
# print("Hello ",name,", you are",age,"years old.")
#-------------------------------------------------
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# if a > b:
#     a += 10                                                     # task 4
# else:
#     a -= 5
# print("Updated first number:", a)
#-------------------------------------------------
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))                            # task 5
# fav = int(input("Enter your favorite number: "))
# print(f"Hello, {name}, You are {age} years old, and your favorite number is {fav}.")
#-------------------------------------------------
# a=int(input("Enter a number : "))
# if a==0:
#     print("It is Zero")
# elif a>0:                                                       # task 8 /2
#     print(a," is Positive")
# else:
#     print(a," is Negative")
#-------------------------------------------------
#sum of numbers from 1 to 10---------------------------------
# (Exercise 1)

# sum = 0
# for i in range(1, 11):                                            # task 9/1
#     sum += i
# print("Sum : ", sum)

#print even numbers from list-------------------------
# (Exercise 2)

# a = [1, 2, 3, 4, 5, 6]
# for i in a:                                                        # task 9 /2
#     if i % 2 == 0:
#         print(i)

#multiplication table of 1 to 5-------------------------
# (Exercise 3)

# n=5
# for i in range(1, n+1):
#         for j in range(1, n+1):                                      # task 9/3
#             a=i*j
#             print(a, end="\t")
#         print()
#--------------------------------------------------------
# fav = ["biriyani","mandhi","porotta with beef curry","duck varieties","masala dosa"]
# for i in fav:                                                                                 # task 15
#     print(f"I love eating {i}.")
#--------------------------------------------------------
# n = [x**2 for x in range(1, 11)]                              # task 16/1
# print(n)

# a = 'Python Programming is fun!'
# vow = [char for char in a if char.lower() in 'aeiou']         # task 16/2
# print(vow)

# a = [x for x in range(1, 21) if x % 2 != 0]                   # task 16/3
# print(a)
#--------------------------------------------------------
# # Extract the first and last character of a string:
# a = "Programming"                                               # task 17/1
# print(a[0],a[-1])

# # Reverse a string:
# a = "Programming"                                               # task 17/2
# rev = a[::-1]
# print(rev)

# # Count occurrences of a specific character:
# a = "Programming"                                               # task 17/3
# print(a.count("m"))

# # Replace spaces with underscores:
# a = "Python is fun to learn"                                    # task 17/4
# print(a.replace(" ", "_"))

# # Check if a string is a palindrome:
# a = "madam"                                                     # task 17/5
# print(a == a[::-1])
#--------------------------------------------------------
# a = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
# print("first day : ",a[0])
# print("second day : ",a[-1])                                                             # task 19/1
# print("slicing : ",a[1:4])
# print("indexing of wednesday : ",a.index("Wednesday"))

# students = ["varun", "aneez", "varun", "sandra", "noufiya","aneez"]
# a = set(students)
# print("Unique students : ", a)

# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# b = set1 | set2                                                                          # task 19/2 
# print("Union : ", b)
# c = set1 & set2
# print("Intersection : ", c)
# d = set1 - set2
# print("Difference (set1 - set2) : ", d)

# e = set1 <= b
# print("Is set1 a subset of b : ", e)
#--------------------------------------------------------
# a=""
# b=0
# while a != -1 :                                       # sum of numbers entered until -1 is entered
#     a=int(input("Enter a number : "))
#     if (a != -1):
#         b=b+a   
# print(b)
#--------------------------------------------------------
# n=5
# for i in range(0,n):
#     for j in range(0,n):
#         print("* ",end=" ")
#     print()

# n=5
# b=1
# for i in range(0,n):
#     for j in range(0,n):
#         print(b,end=" ")
#         b=b+1
#     print()

# n=5
# for i in range(0,n):
#     for j in range (i+1):
#         print("* ",end=" ")
#     print()

# n=5
# for i in range(0,n):
#     for k in range (0,n-i):
#         print("",end=" ")
#     for j in range (0,i+1):
#         print("* ",end="")
#     print()
#---------------------------------------------------
# num=[1,2,3,4,5]
# a=[x**2 for x in num]
# print(a)

# list= [char for char in [1,2,3]]                          # list comprehension
# print(list)

# matrix=[[j for j in range(3)] for i in range(3)]
# print(matrix)
#---------------------------------------------------------
# list1=["varun","aneez","sandra","noufiya","varuna"]
# list2=[1,2,3,4,5]                                         # zip function
# a=zip(list1,list2)
# print(dict(a))
#---------------------------------------------------------
# n = 5 
# for i in range(1, n + 1):
#     for j in range(1, i + 1):               # Right Half Pyramid
#         print("*", end=" ")
#     print()

# n = 5
# for i in range(1, n + 1):
#     for j in range(n - i):
#         print(" ", end=" ")                 # Left Half Pyramid
#     for k in range(i):
#         print("*", end=" ")
#     print()

# n=5
# for i in range(0,n):
#     for k in range (0,n-i):                   # Full Pyramid
#         print("",end=" ")
#     for j in range (0,i+1):
#         print("* ",end="")
#     print()

# n = 5
# for i in range(1, n + 1):
#     for j in range(n-i + 1):                    # inverted right half pyramid
#         print("*", end=" ")
#     print()

# n = 5
# for i in range(n):
#     for j in range(i):
#         print(" ", end=" ")                     # inverted left half pyramid
#     for k in range(n-i):
#         print("*", end=" ")
#     print()

# n=5
# for i in range(0,n):
#     for k in range (i):                   # Rhombus Pattern
#         print(" ",end=" ")
#     for j in range (n):
#         print("* ",end="")
#     print()

# n=int(input("Enter the number : "))
# for i in range(n):
#     for j in range(n):
#         if i==0 or i==n-1 or j==0 or j==n-1:          # hollow square
#             print("* ", end=" ")
#         else:
#             print(" ",end="  ")
#     print()

# n=int(input("Enter the number : "))
# for i in range(0,n):
#     for k in range (0,n-i):
#         print("",end=" ")
#     for j in range (0,i+1):
#         if(i==n-1):                                   # Hollow Full Pyramid
#             print("* ",end="")
#         elif(j==0 or j==i):
#             print("* ",end="")
#         else:
#             print(" ",end=" ")
#     print()

# n=int(input("Enter the number : "))
# for i in range(n):
#     for j in range(2*n-1):
#         if j == i or j == (2*n-2-i):                  # printing letter V with range user defined
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# n = 5
# for i in range(n):
#     for k in range(i):
#         print(" ", end="")                            # inverted full pyramid
#     for j in range(n-i):
#         print("*", end=" ")
#     print()

# n=5
# for i in range(0,n):
#     for k in range (0,n-1-i):
#         print(" ",end="")
#     for j in range (0,i+1):
#         print("* ",end="")                            # diamond pattern
#     print()
# for i in range(n):
#     for k in range(i):
#         print(" ", end="")
#     for j in range(n-1-i):
#         print(" *", end="")
#     print()

# n = 5
# for i in range(n):
#     for k in range(i):
#         print(" ", end="")
#     for j in range(n-i):                              # hourglass pattern
#         print("*", end=" ")
#     print()
# for i in range(1,n):
#     for k in range (0,n-1-i):
#         print("",end=" ")
#     for j in range (0,i+1):
#         print("* ",end="")
#     print()

# n = 5
# for i in range(n):
#     for k in range(i):
#         print(" ", end="")
#     for j in range(n-i):                          # hollow inverted full pyramid
#         if (j==0 or j==n-1-i or i==0):
#             print("* ",end="")
#         else:
#             print(" ",end=" ")
#     print()

# n=5
# for i in range(0,n):
#     for k in range (0,n-1-i):
#         print(" ",end="")
#     for j in range (0,i+1):
#         if (j==0 or j==i):
#             print("* ",end="")
#         else:
#             print(" ",end=" ")                # hollow diamond
#     print()
# for i in range(n):
#     for k in range(i):
#         print(" ", end="")
#     for j in range(n-1-i):
#         if (j==0 or j==n-1-(i+1)):
#             print(" *",end="")
#         else:
#             print(" ",end=" ")
#     print()

# n = int(input("Enter a number : "))
# a = 1
# for i in range(1, n + 1):
#     for j in range(1, i + 1):                 # Floyds triangle
#         print(a, end=' ')
#         a += 1
#     print()

# n = 5
# a = 1
# for i in range(n):
#     for k in range(n - i - 1):                # pascals triangle
#         print(' ', end='')
#     for j in range(i + 1):
#         print(a, end=' ')
#         a = a * (i - j) // (j + 1)
#     print()
#--------------------------------------------------------
n = int(input("Enter the number : "))
if n <= 0:
    print("Enter a number greayer than zero")
for i in range (n):
    for l in range(i):
        print(" ", end=" ") 
    a = [0, 1]                                                # pattern with fibanocii
    for j in range(2, n):
        a.append(a[j-1] + a[j-2])
    for k in range(n-1, -1, -1):
        print(a[k], end=' ')

    first = 0
    second = 1
    for i in range(n):
        a.append(first)
        print(first,end=" ")
        c = first + second
        first = second
        second = c
    print()
    n -= 1
