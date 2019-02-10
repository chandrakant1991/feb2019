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
def greetings():
    """
     This is Greeting Function
    :return:
    """
    print("Hello word")
greetings()





