# i=10
# if (i>15):
#     print("is grater than 15")                        # if statement
# print("lesser than 15")

# if (i<10):
#     print("is lesser than 10")                        # if else
# else:
#     print("is greater than 10 or equals to 10")

# if (i<10):
#     print("is lersse than 10")
# if(i>10):
#     print("is greater than 10")                       # nested if
# else:
#     print("the number is 10 and is equal")

# if (i<10):
#     print("is lersse than 10")
# elif (i>10):                                          # if elif else
#     print("is greater than 10")
# else:
#     print("the number is 10 and is equal")
#--------------------------------------------------------------------
# a=int(input("Enter the number"))
# if (a==0):
#     print(" the number is even")
# elif (a%2==0):                                        # odd or even
#     print("the number is even")
# else:
#     print("the number is odd")
#--------------------------------------------------------------
# a=int(input("Enter the number : "))
# b=int(input("Enter the number : "))
# c=int(input("Enter the number : "))

# if( a>=b and a>=c):                                   # greatest among three number
#     print(a," is larger")
# elif (b>=a and b>=c):
#     print(b," is greater")
# else:
#     print(c," is greater")
#----------------------------------------------------------
# a=int(input("Enter the number : "))
# if (a<0 or a>100):
#     print("Enter a valid Mark")
# elif(a>=95 and a<=100):
#     print("You have A+ grade With High Distinction")
# elif(a>=90 and a<=100):
#     print("You have A+ grade")
# elif(a>=80 and a<90):
#     print("You have A grade")                 # task 8/1
#     print("You have B grade")
# elif(a>=60 and a<70):
#     print("You have C grade")
# else:
#     print("You have Failed")
#----------------------------------------------------------
# print("1 = Addition, 2 = Subtraction, 3 = Multiplication, 4 = Divition")
# a=int(input("Enter option number to perform : "))
# b=int(input("Enter 1st number : "))
# c=int(input("Enter 2nd number : "))
# if (a==1):
#     x=b+c
#     print("The sum is : ",x)
# elif (a==2):
#     x=b-c
#     print("The subtracted value is : ",x)                     # taking options and doing function according to the option
# elif (a==3):
#     x=b*c
#     print("The multiplied value is : ",x)
# elif(a==4):
#     if(c==0):
#         print("A number cannot be devided by zero")
#     else:
#         x=b/c
#         print("The devided value is : ",x)
# else:
#     print("Enter a valid number")
#-------------------------------------------------------
# vow=str(input("Enter a alphabet: "))
# vow=vow.islower()
# if (vow=="a" or vow=="e" or vow=="i" or vow=="o" or vow=="u"):          # to find the vowels
#     print(vow," is Vowel")
# else:
#     print(vow," is not vowel")

# vow=str(input("Enter a alphabet: "))
# a=vow.lower()
# print(a)                                                                # to find vowel using in function
# vowel=["a","e","i","o","u"]
# if vow in vowel:
#     print(vow," is Vowel")
# else:
#     print(vow," is not vowel")
#-------------------------------------------------
# a=[1,2,3,4,5,6,7,8,9,10]
# for i in a:                                                   # to print even number form given list
#     if i % 2 == 0:
#         print(i)

#-------------------------------------------------
#-------------------------------------------------
#-------------------------------------------------

# n = int(input("Enter a value for N: "))
# sum = 0
# for i in range(1, n + 1):                                     # sum of even numbers upto range given
#     if i % 2 == 0:
#         sum += i
# print("Sum of even numbers between 1 and", n, "is:", sum)
#--------------------------------------------------
# a = input("Enter a string: ")
# a=a.lower()
# b=("a","e","i","o","u")
# vow= 0                                                        # count of vowels in string
# for i in a:
#     if i in b:
#         vow += 1
# print("Number of vowels : ",vow)
#-------------------------------------------------
# a = [10, 0, 1000, 100, 200, 500]
# b = a[0]
# for i in a:                                                    # find max number in list
#     if i > b:
#         b = i
# print("The maximum number in the list is:", b)
#------------------------------------------------
# a = [10, 1000, 100, 200, 500]
# b=1
# for i in a:                                                   # product of all nnumbers in list
#     b *=i
# print(b)
#------------------------------------------------
# a = input("Enter a string: ")
# b=len(a)
# rev = ""                                                      # reversing the string
# for i in range (b):
#     rev = a[i] +rev
# print("Reversed string is:", rev)
#-------------------------------------------------
# a = input("Enter a string: ")
# b=len(a)
# for i in range(0, b, 2):                                          # printing characters in the even  index positions 
#     print("Character at even position ",i," is : ", a[i])
#------------------------------------------------
# a=int(input("Enter the number of elements to add in 1st list : "))
# b=[]
# for i in range (a):
#     c=input("Enter the elemnts for 1st list : ")
#     b.append(c)

# x=int(input("Enter the number of elements to add iin 2nd list : "))       # finding common elements in two lists
# y=[]
# for j in range (x):
#     z=input("Enter the elemnts for 2nd list : ")
#     y.append(z)

# for k in b:
#     for l in y:
#         if k==l:
#             print(k) 
#-------------------------------------------------
# a= int(input("Enter the number : "))
# c=len(str(a))
# sum=0
# b=0
# for i in range (0,c):                                                     # sum of digits using for loop
#     b=a%10
#     sum+=b
#     a=int(a/10)
# print("The sum is : ",sum)
#-------------------------------------------------

# count=1
# while count <=5:                                                          # while loop
#     print(count)          
#     count +=1

# count=1
# while count <=5:                                                          # while loop with else
#     print(count)          
#     count +=1
# else:
#     print("suceessfully completed")
#------------------------------------------------
# a= 10
# while a>=1:                                                               # print numbers from 10 to 1
#     print(a)
#     a -=1
#-----------------------------------------------
# a= int(input("Enter a number : "))
# b=0
# while a>0:                                                                # sum of digits of a number
#     b=b+a%10
#     a=int(a/10)
# print(b)
#------------------------------------------------
# a = input("Enter a string: ")
# b=len(a)-1
# rev = ""                                                      
# while b>=0:
#     rev += a[b]                                                           # string is palindrome or not
#     b-=1
# if a==rev:
#     print(a," is palindrome")
# else:
#     print(a," is not palindrome")
#----------------------------------------------
# a= int(input("Enter the number : "))
# b=0
# if a==0:
#     b=1                                                                   # count of numbers in a digit
# else:
#     while a>0:
#         a=int(a/10)
#         b+=1
# print(b)
#----------------------------------------------
# a=int(input("Enter the number of elements to add in 1st list : "))
# b=[]
# for i in range (a):
#     c=input("Enter the elemnts for 1st list : ")
#     b.append(c)
#--------------------------------------------
# a=""
# while a.lower()!= "quit":                                             # while input not quit print user inputs
#     a=input("Enter the word : ")
#-------------------------------------------
# a= int(input("Enter the number : "))
# b= int(input("Enter the digit to check : "))
# c=0
# while a>0:                                                        # to check how much times a digit repeates in number
#     d=a%10
#     if d==b:
#         c+=1
#     a=int(a/10)
# print(c)
#-----------------------------------------
# a= int(input("Enter the number : "))
# b=0
# c=0
# d=a
# while a>0:
#     b= a%10                                                       # armstrong number checking
#     c += b**3
#     a=int(a/10)
# if c==d:
#     print(c," is a armstrong number")
# else:
#     print(c," is not a armstrong number")
