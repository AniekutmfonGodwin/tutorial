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


sentence = input("enter a sentence: ")

print("word" in sentence)

