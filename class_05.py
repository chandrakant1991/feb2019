# Assignment
# 1) Write list comprehension to create 15 random numbers
# 2) Write list comprehension to create Prime Numbers till user defined number
# 3) Write Dictionary comprehension with 5 key value pair
# 4) Convert all pattern assignments in User Defined Function


# List Comprehension
# odd = list()
# for i in range(1, 10, 2):
#     odd.append(i)
# print(odd)
# print('###################################################')
# # Dictionary Coprehension
# sq = {}
# number = [2, 4, 9, 6, 3, 5]
# for num in number:
#     sq[num] = num*num
# print(sq)
# print('##################################################')
# sq = {num: num*num for num in number}
# print(sq)
# print('##################################################')
# labels = ['Name', 'Age', 'Contact no']
# user1 = ['Parth', 20, 1234567890]
# user2 = ['shrikant', 15, 22222222222]
# user3 = ['Chandrakant', 12, 9637646900]
#
# op = list()
# for user in [user1, user2, user3]:
#     _user = dict()
#     for index in range(0, 3):
#       _user[labels[index]] = user[index]
#     op.append(_user)
# print(op)
#
#
# ouptput = [
#     {
#      labels: user[index] for index, labels in enumerate(labels)
#     }
#     for user in [user1, user2, user3]
# ]
# print(ouptput)

# User Defined Function
# def greetings():
#     """
#      This is Greeting Function
#     :return:
#     """
#     print("Hello word")
# greetings()
#
#
#
# def arg_greeting(name):
#     """
#       This is greeting function with argument
#     :param name:user name
#     :return:
#     """
#     print(F'hello{name}')
# arg_greeting(name= 'chandrakant')
# arg_greeting
# def arg_return_greetings(name):
#     """
#
#     :param name:
#     :return:
#     """
#     message = F'hello {name}'
#     return message
#
# _name = input('Enter The name:=> ')
# resp = arg_return_greetings(_name)
# print(resp)
# #
# def wild_card_args_funtion(*args):
#     """
#
#     :param args:
#     :return:
#     """
#     print(args[0], [1])

# def wild_card_kwargs_function(**kwargs):
#     """
#
#     :param kwargs:
#     :return:
#     """
#     for key, values in kwargs.items():
#         print(key, ":", values)
# user_1={"name":"Chandrakant","Age": 26, "contact no": 9637646900}
# wild_card_kwargs_function(**user_1)
# i = 0
# #list= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for i in range(1, 11):
#  print(i*10)
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for i in range(0, 10):
#     print(list1[i]*10, end=" ")

# list1 = [10, 11, 12, 13, 14, 15, 16, 17, 18]
# for i in range(len(list1)):
#     print(list1[i]*10)
# multi = 1
# number = input("Enter The Range ==> ")
# for i in range(len(number)):
#     for j in range(1, 10):
#         multi = i*j
#         j+=1
#         print(multi)
# number = int(input("Enter The Range ==> "))
# print("The Prime number in given range are: ")
# for num in range(2, number+1):
#     if num > 1:
#       for j in range(2, num):
#         if (num % j) == 0:
#           break
#       else:
#        print(num,end=" ")
# Output:-
# Enter The Range ==> 20
# The Prime number in given range are:
# 2 3 5 7 11 13 17 19

# list = []
# for i in range(0, 15):
#     if i % 2 == 0:
#         i-= 1
#     else:
#         i+=3
#     list.append(i)
# print(list)
# Output
# [-1, 4, 1, 6, 3, 8, 5, 10, 7, 12, 9, 14, 11, 16, 13]





# labels = ['EName', 'Designation', 'Emp. code', 'Address', 'Mobile no']
# user1 = ['Parth', 'VP', 20, "Vadgaonsheri", 1234567890]
# user2 = ['shrikant', 'CEO',  15, 'Vishrantwadi', 22222222222]
# user3 = ['Chandrakant', 'SystemAdmin', 12, 'SainikNagar,Yerwada', 9637646900]
# op = list()
# for user in [user1, user2, user3]:
#     _user = dict()
#     for index in range(0, 5):
#       _user[labels[index]] = user[index]
#     op.append(_user)
# print(op)

# Output:-
# [{'EName': 'Parth', 'Designation': 'VP', 'Emp. code': 20, 'Address': 'Vadgaonsheri', 'Mobile no': 1234567890},
# {'EName': 'shrikant', 'Designation': 'CEO', 'Emp. code': 15, 'Address': 'Vishrantwadi', 'Mobile no': 22222222222},
# {'EName': 'Chandrakant', 'Designation': 'SystemAdmin', 'Emp. code': 12, 'Address': 'SainikNagar,Yerwada', 'Mobile no': 9637646900}]

# def numeric():
#     for i in range(1, 6,):
#         for j in range(1, i+1):
#          print(j, end=" ")
#         print("")
# numeric()

# Output:-
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# def numeric():
#     for i in range(1, 6,):
#         for j in range(1, 6):
#          print(j, end=" ")
#         print("")
# numeric()
# Output:-
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# def numeric():
#     for i in range(1, 6,):
#         for j in range(1, 6):
#          print(i, end=" ")
#         print("")
# numeric()

# Output:-
# 1 1 1 1 1
# 2 2 2 2 2
# 3 3 3 3 3
# 4 4 4 4 4
# 5 5 5 5 5

# def numeric():
#     for i in range(1, 6,):
#         for j in range(1, 6):
#          print('*', end=" ")
#         print("")
# numeric()

# Output:-
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

# def numeric():
#     for i in range(1, 6,):
#         for j in range(1, i+1):
#          print('1', end=" ")
#         print("")
# numeric()
# Output:-
# 1
# 1 1
# 1 1 1
# 1 1 1 1
# 1 1 1 1 1
# def numeric():
#     for i in range(1, 6):
#         for j in range(1, i+1):
#          print(j%2, end=" ")
#         print("")
#         i-=1

# numeric()
# Output:-
# 1
# 1 0
# 1 0 1
# 1 0 1 0
# 1 0 1 0 1


# 3) def star():
#  for i in range(0, 5):
#
#      for j in range(1, 6):
#          print(i%2, end=" ")
#      print("")
# star()

#Output:-
# 0 0 0 0 0
# 1 1 1 1 1
# 0 0 0 0 0
# 1 1 1 1 1
# 0 0 0 0 0

def star():2
number = 5
for i in range(0, 6):
    #print("")
    #number = number - 1
    for j in range(0, number):
     print(1, end=" ")
    print("")
    number = number - 1
star()

# Output:-
# 1 1 1 1 1
# 1 1 1 1
# 1 1 1
# 1 1 
# 1
