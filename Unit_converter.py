# Program for unit converter
def start():
    print("Welcome to Unit Converter Promgram")
    print("1. Convert mm to cm ")
    print('2. Convert cm to M')
    print('3. Convert mm to M')
    print('Select one of above')
   # no = int(input('Enter The Positive Number one of above ==:'))
start()
no = int(input('Enter The Positive Number one of above ==:'))
if no == 1:


 def convert_mm_cm():
    num = int(input('Enter The Positive Number To convert ==:'))
    num1= num/10
    print('The Value after Coversion is:-',num1,'cm')

 convert_mm_cm()
elif no == 2:
 def convert_cm_m():
    num = int(input('Enter The Positive Number To convert ==:'))
    num1= num/100
    print('The Value after Coversion is:-',num1,'M')

 convert_cm_m()
elif no == 3:
 def convert_mm_m():
    num = int(input('Enter The Positive Number To convert ==:'))
    num1= num/1000
    print('The Value after Coversion is:-')
    print(num1,'M')
 convert_mm_m()
else:
    print('Invalid Choice? Please Enter The number in between 1 and 3')
    print('Do you want to continue Again:')
    start()
