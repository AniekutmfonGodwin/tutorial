# # if True:
# #     print("is true")
# #     print("yes")

# """
# if True:
#     print("is true")
#     print("yes")
# """

# # print("anies said \"how are you\" ") # this is to print hello world



# name = "anies"


# def greet():
#     name = "edidiong"
#     print("good morning ",name)


# greet()
# print("name",name)



# # >>> range(1,30)      
# # range(1, 30)
# # >>> list(range(1,30)) 
# # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
# # >>> tuple(range(1,30)) 
# # (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29)
# # >>>

# item_list = [
#     1,
#     2,
#     3,
#     4
# ]

# (1,2,3,4,5)

# # age,name,account_balance
# # the key must always be in quote
# # the value must be a python datatype
# data = {
#         "name":"anies",
#         "age":40,
#         "account_balane":4000.66
#     }

# # set is a like a list but does not contain duplicate values
# {1,2,3,4,5}



# # inbult function for type conversion
# # >>> str
# # <class 'str'>
# # >>> float
# # <class 'float'>
# # >>> tuple
# # <class 'tuple'>
# # >>> set
# # <class 'set'>
# # >>> complex
# # <class 'complex'>
# # >>> int
# # <class 'int'>
# # >>> bool
# # <class 'bool'>
# # >>>


# # type conversion or casting
# # >>> age = "30" 
# # >>> int(age) 
# # 30
# # >>> float(age) 
# # 30.0
# # >>> list(age)  
# # ['3', '0']
# # >>> set(age)  
# # {'3', '0'}
# # >>> tuple(age) 
# # ('3', '0')
# # >>>


# message = """
# hello 
# how are you
# """

# # iterable -> any datatype that can be looped through



# ###################
# ##### STRING ######
# #################

# # accessing a string
# """
# >>> data = "hello how are you?" 
# >>> data
# 'hello how are you?'
# >>> data[0] 
# 'h' 
# >>> data[1] 
# 'e' 
# >>> data[2] 
# 'l' 
# >>> 
# """
# data = "hello how are you?" 

# for x in data:
#     print(x)

# # find the length of a list
# len(data) 

# txt = "The best things in life are free!"
# print("free" in txt)



# if "hate" in sentence:
#     print("bad word in sentence hate")
# if "kill" in sentence:
#     print("bad word in sentence")







# def checker():
#     sentence = input("emter your sentence: ")
#     print("sentence is \n",sentence)


# checker()





# """
# # what you have learn so far
# # the assignment
# # scope -> limitation
# # present your project
# """
# list,tuple,set,str

# items = [
#     (1,2),
#     (3,5),
#     (4,6)
# ]





# for x,y in items:
#     print("x",x," y",y)



    


# >>> print(template.format("john"))  
# Hello john we are glad to have you
# >>> print(template.format("anies")) 
# Hello anies we are glad to have you
# >>> template = "good {} {} we are glad to have you"
# >>> print(template.format("morning","name")) 
# good morning name we are glad to have you
# >>> print(template.format("morning","anies")) 
# good morning anies we are glad to have you
# >>> print(template.format("afternoon","anies")) 
# good afternoon anies we are glad to have you
# >>> template = "good {1} {0} we are glad to have you" 
# >>> print(template.format("afternoon","anies"))       
# good anies afternoon we are glad to have you
# >>> template = "good {1} {1} we are glad to have you"
# >>> print(template.format("afternoon","anies"))       
# good anies anies we are glad to have you
# >>>



# increment and in operation
# >>> a +=1
# >>> a
# 11
# >>> a +=1
# >>> a
# 12
# >>> a -=1 
# >>> "anies" in 'hello anies'
# True
# >>> "anies" not in 'hello anies' 
# False
# >>>


# list method 
# >>> li
# ['apple', 'banana', 'cherry']
# >>> li[0] = "new value" 
# >>> li
# ['new value', 'banana', 'cherry']
# >>> li[1:] = [1,2,3,4] 
# >>> li
# ['new value', 1, 2, 3, 4]
# >>> li.insert(1,"inserted item") 
# >>> li
# ['new value', 'inserted item', 1, 2, 3, 4]
# >>>



# assignment => what data type will you use to store this datas
# a table of users information
# types of cars
# list of usernames with no duplicate


# sentence = input("enter a sentence: ")

# print("word" in sentence)

"""
name => anies
age => 10
class => primary 1
"""




'''
false values are:'',0,[],{},(),False,None
'''

# age
# remove username and use email

# list of users password
# database = [
#     {
#         "username":"anies",
#         "password":"123"
#     },
#     {
#         "username":"edi",
#         "password":"113"
#     },
# ]


# user_username = input("enter your username: ")
# user_password = input("enter your password: ")





# if {"username":user_username,"password":user_password} in database:
#     print("logged in successful")
# else:
#     print("incorrect password")


# 3 ways to create a list 
# >>> list((1,2,3)) 
# [1, 2, 3]
# >>> list("asdd")  
# ['a', 's', 'd', 'd']
# >>> [x for x in 'anies'] 
# ['a', 'n', 'i', 'e', 's']
# >>> list("anies") 
# ['a', 'n', 'i', 'e', 's']
# >>>



# how to add an item to a list value

# >>> li = [1,2,3,4] 
# >>> li +=[55] 
# >>> li
# [1, 2, 3, 4, 55]
# >>> li.append("3344") 
# >>> li
# [1, 2, 3, 4, 55, '3344']
# >>> li.insert(2,1000)    
# >>> li
# [1, 2, 1000, 3, 4, 55, '3344']
# >>> li.extend(["mango", "pineapple", "papaya"]) 
# >>> li
# [1, 2, 1000, 3, 4, 55, '3344', 'mango', 'pineapple', 'papaya']
# >>> li.extend(("kiwi", "orange")) 
# >>> li
# [1, 2, 1000, 3, 4, 55, '3344', 'mango', 'pineapple', 'papaya', 'kiwi', 'orange']
# >>> [*li,"400",9900] 
# [1, 2, 1000, 3, 4, 55, '3344', 'mango', 'pineapple', 'papaya', 'kiwi', 'orange', '400', 9900]
# >>>



# removing an item from a list
# >>> li = [1,2,3,4]
# >>> li.remove(1) 
# >>> li
# [2, 3, 4]
# >>> li.remove(4) 
# >>> li
# [2, 3]
# >>> li.remove(4)
# Traceback (most recent call last):       
#   File "<stdin>", line 1, in <module>    
# ValueError: list.remove(x): x not in list
# >>>


# create a list
# add new item to the list
# add a new list to the existing list
# insert an item into the list
# remove an item in a list using its value
# remove an item in a list using its index
# remove the last item from a list



# looping through a list
# >>> for a in li:
# ...     if a%2 == 0:
# ...             print("{} is an even number".format(a))
# ... 
# 2 is an even number
# 4 is an even number
# 6 is an even number
# 8 is an even number
# 10 is an even number
# >>>



# while (condition)):
#     print("hello")


# spam_words = [
#     "fuck you",
#     "kill"
# ]


# sentence = input("enter your message ")

# def my_sorting_func(item):
#     return item["year"]

# cars = [
#   {'car': 'Ford', 'year': 2005},
#   {'car': 'Mitsubishi', 'year': 2000},
#   {'car': 'BMW', 'year': 2019},
#   {'car': 'VW', 'year': 2011}
# ]
# cars.sort(key=my_sorting_func)
# print(cars)


#############################
##### TUPLE ################
#  tuple is immutable

# cars = ("toyota","camery")




# cars[0] = ["camery"]








# if "toyota" in cars[0]:
#     print("give access")

# unpacking
# >>> (a,b,c,*rest) = (22,44,66,445)
# >>> rest
# [445]
# >>> (a,b,c,*rest_of_item) = (22,44,66,445,444,555,666,777) 
# >>> a
# 22
# >>> b
# 44
# >>> c
# 66
# >>> rest_of_item
# [445, 444, 555, 666, 777]
# >>>



# >>> rest
# [445, 444, 555, 666, 777]
# >>> rest * 2
# [445, 444, 555, 666, 777, 445, 444, 555, 666, 777]
# >>> rest = tuple(rest)
# >>> rest
# (445, 444, 555, 666, 777)
# >>> rest.count(444) 
# 1
# >>> rest +=rest
# >>> rest
# (445, 444, 555, 666, 777, 445, 444, 555, 666, 777)
# >>> rest.count(444) 
# 2
# >>> rest.index(444) 
# 1
# >>>



# add item to a set
# >>> li.add(990)  
# >>> li
# {777, 555, 666, 444, 445, 990}
# >>> li.add(66) 
# >>> 


names = set()


for _ in range(3):
    name = input("enter your name: ")
    if name:
        names.add(name)
    else:
        print("empty value is not allow")

print('names',names)



"""
# algorithm for loop
create a set
create a loop to loop 10 times
get input from user for every loop
check if input from user is not empty
if input is not empty add to the set
if input is empty print a warning message
after the loop print the set
"""










