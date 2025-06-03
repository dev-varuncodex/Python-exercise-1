# # print("Varun")
# a=10
# b=20

# # a,b=b,a
# # print(a)                                    1st day exercise
# # print(b)

# a = a + b
# b = a - b
# a = a - b

# print(a)
# print(b)
#----------------------------------------------------------------
# x="varun"
# y=5                             #Type of
# print(type(x))
# print(type(y))
#-------------------------------------------------------------
# name= "Varun Madhu"              #Length of string
# print(len(name))        
# ------------------------------------------------------------
# name="Varun"
# print(name[2])                #string indexing.position start from 0 to end.. and to count from back use -1 to end
# print(name[-3])               # use : for limit
# print(name[-2])     
# print(name[0:3])              # use 3rd digit to jump
# print(name[0:5:2])            # ::-1 for printing it reverse
# print(name[::-1])     
#---------------------------------------------------------------
# first= "Varun"
# second= "Madhu"
# a= 6                              #string addition
# print(first+ " "+second)
# print(first+ " "+second+" "+str(6))
#-------------------------------------------------------------
# name= "Varun Madhu"
# print(name.upper())                               # .upper
# print(name.lower())                               # .lower    
# x=name.count("a")                                 # .count
# print(x)                                          # .find
# print(name.find("M"))                             # .replace
# y=name.replace("Varun Madhu","Good Name")
# print(y)
#-------------------------------------------------------------
# print(5>3)
# print(5<3)                    #boolean print true or false
# print(5==3)
#----------------------------------------------------------
# name=["varun","varuna","madhu","jayasree"]        # list in python -----
# name.append("sandra")                             # .append()
# name.insert(1,1)                                  # .insert()
# vehicle=["car","bike","scooter"]                  # .extend()
# name.extend(vehicle)                              # change value
# name[1]="yeye"
# print(name)
#----------------------------------------------------------
# vehicle=["car","bike","scooter","helicopter","van","boat","hahah"]
# vehicle.pop()
# print(vehicle)                                    # .pop()
# vehicle.pop(1)                                    # del[]
# print(vehicle)                                    # .remove       
# del vehicle[0]                                    # .reverse()
# print(vehicle)
# vehicle.remove("van")
# print(vehicle)
# vehicle.reverse()
# print(vehicle)
#-------------------------------------------------------
# a=[1,2,3,4,5,6,]
# a=a*2                                 # list operators----------
# print(a)                              # repetation
# b=["a","b","c","d","e"]               # concatenation
# c=a+b                                 # length
# print(c)                              # iteration
# length=len(a)                         # membership
# print(length)
# for i in a:
#     print(i)
# print(4 in a)
# print(100 in a)
#------------------------------------------------
# a=[1,2,3,4,5,6,]
# print(max(a))                         # max()
# print(min(a))                         # min()
#-------------------------------------------------
# a=[1,2,3,4,5,6]
# b=[3,4,5,6,7,8,9]                        # intersection
# c=set(a).intersection(b)                 # using intersection method
# d=set(a)&set(b)                          # using and(&) operator
# print(c,d)
#------------------------------------------------
# a=(1,2,3,4,5,6,7,1,2,3,4,5,6,7,1,2,3,4,5,6,7)
# print(a)
# b=("mouse",[1,2,3,4],(1,2,3))            # touple
# print(b)                                 # count
# x=a.count(1)                             # indexing
# print(x)                                 # -ve indexxing
# y=a.index(2)                             # index
# print(y)                                 # repetation
# print(a[5])
# print(a[-7])
# b=b*3
# print(b)
# for i in b:                              # iteration
#     print(i)                             # in function // prints only true or false
# print("mouse" in b)
# print("cat" in b)
# print(b)
#------------------------------------------------
# name={"varun","Madhu","jayasree","varuna"}
# print(name)
# word=set(["cat","dog","buffallo"])              # set
# print(word)
# print(type(word))
# for i in name:                                  # .add
#     print(i)                                    # .update       
# name.add("sandra")                              # .discard
# print(name)                                     # .remove
# word.update(["duck","cow"])
# print(word)
# word.remove("cat")
# word.discard("duck")
# print(word)
#--------------------------------------------------
# names={"varun","Madhu","jayasree","varuna","sandra","noufiya"}
# names1={"varun","Madhu","jayasree","varuna","sandra","noufiya"}
# name1={"varun","Madhu","jayasree","varuna"}
# name2=set(["varun","sandra","noufiya"]) 
# print(name1|name2)                                     # union in sets
# print(name1&name2)                                     # intersection in sets
# print(names>name1)                                     # >,<,>=,<=,== comparison operators
# print(names>=names1)                                     
# print(names==names1)    
# print(name1==name2)
#---------------------------------------------------
# city={"kalamassery":"Ernakulam","thottapilly":"alappuzha"}       #dictionary
# print(city)
# city["thampanoor"]="Trivandrum"
# city["kanyakumari"]="Trivandrum"                # adding new elements
# city["kalamassery"]="kochi"                     # updation
# print("updated :",city)
# print(city["kalamassery"])                      # accessing elements from dictionary
# del city["kanyakumari"]
# print(city)
# for i in city:                                  # iteration
#     print(city[i])
#     print(i)
#-----------------------------------------------------
# a=int(input("Enter the number"))
# b=int(input("Enter the number"))              # input taking from user
# c=a+b
# print("{} and {}".format(a,b))
# print(a,"+",b,"=",c)                          # use commas to seperate
