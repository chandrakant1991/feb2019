#
# 1) Program to accept the strings which contains all vowels
# 2) Palindrome numbers in a list
# 3) Number to words like 121 converts one two one or one hundred twenty one





# list1 = [121, 100, 201, 252, 656, 589, 248, 494, 10]
# # list2 = list1
#
# for i in list1:
#     n = i
#     rev = 0
#     while i>0:
#         dig =i%10
#         rev= rev*10+dig
#         i=i//10
#     if(n==rev):
#         print(rev)
#




# string1 = 'This is my india.'
# string1 = string1.split()
# print(string1)
# import string
# alpha = string.ascii_lowercase
# num = int(input())
# def srange(N):
#     return list(range(N))+list(range(N-2,-1,-1))
# for i in srange(num):
#     print('-'.join([alpha[num-j-1] for j in srange(i+1)]).center(4*(num-1)+1,'-'))
#
#

# import string
# alpha = string.ascii_lowercase
# n = int(input())
# L = []
# for i in range(n):
#     s = "-".join(alpha[i:n])
#     L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
# print('\n'.join(L[:0:-1]+L))
# def print_rangoli(n):
#     import string
#     alpha = string.ascii_lowercase
#     l=[]
#     for i in range(n):
#         s = '-'.join(alpha[i:n])
#         l.append((s[::-1]+s[1:]).center(4*n-3,'-'))
#     b=reversed(l[1:])
#     print("\n".join(b), "\n".join(l), sep = "\n")
#

# list = ['a', 'b', 'c']
# for i in range(0,5):
    # for j in range(0,9):
    #  print('-'.join(list))
# def print_rangoli(size):
#     width  = size*4-3
#     string = ''
#
#     for i in range(1,size+1):
#         for j in range(0,i):
#             string += chr(96+size-j)
#             if len(string) < width :
#                 string += '-'
#         for k in range(i-1,0,-1):
#             string += chr(97+size-k)
#             if len(string) < width :
#                 string += '-'
#         print(string.center(width,'-'))
#         string = ''
#
#     for i in range(size-1,0,-1):
#         string = ''
#         for j in range(0,i):
#             string += chr(96+size-j)
#             if len(string) < width :
#                 string += '-'
#         for k in range(i-1,0,-1):
#             string += chr(97+size-k)
#             if len(string) < width :
#                 string += '-'
#         print(string.center(width,'-'))
# if __name__ == '__main__':
#     n = int(input())is
#     print_rangoli(n)
# Rangoli pattern
# number = 3
# rows = list()
# for i in range(1, number+1):
#     sequence = list()
#     space = list()
#     for s in range(0, (number-i)*2):
#         space.append("")
#     chars = list()
#     for j in range(0, i):
#         chars.append(chr(96+number-j))
#     sequence=space + chars + chars[::-1][1:] + space
#     rows.append(sequence)
#     print("-".join(sequence),end="")
#     print("")
# for i in rows[::-1][1:]:
#     print('-'.join(i))
#
# N = int(input("Enter The No.==>"))
# if (N%2==1):
#  print('weird')
# else:
#     print("Not weird")
# string = input("Enter The First name and last name:= ")
# string1=string.split()
# for i in string1:
#     print(i.capitalize())







