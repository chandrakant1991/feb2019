# Assignment
# 1) Write list comprehension to create 15 random numbers
# 2) Write list comprehension to create Prime Numbers till user defined number
# 3) Write Dictionary comprehension with 5 key value pair
# 4) Convert all pattern assignments in User Defined Function


# # List Comprehension
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
def arg_return_greetings(name):
    """

    :param name:
    :return:
    """
    message = F'hello {name}'
    return message

_name = input('Enter The name:=> ')
resp = arg_return_greetings(_name)
print(resp)
#
def wild_card_args_funtion(*args):
    """

    :param args:
    :return:
    """
    print(args[0], [1])

def wild_card_kwargs_function(**kwargs):
    """

    :param kwargs:
    :return:
    """
    for key, values in kwargs.items():
        print(key,":", values)
user_1={"name":"Chandrakant","Age": 26, "contact no": 9637646900}
