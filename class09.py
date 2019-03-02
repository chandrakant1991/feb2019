# Class 09 Parse file

# from os import path, makedirs
# #####################################################################################
# 1) Python Absolute Path
# #############################################################################

# Current Absolute Path
# file_path = r"c:\repos\Library"
# current_file_path = path.abspath(__file__)
# print(current_file_path)
# print(path.dirname(current_file_path))
# print(path.basename(current_file_path))
# get current directory
# current_directory = path.dirname(path.abspath(__file__))
# print(current_directory)
# concat file paths
# json_file_path = path.join(
#     current_directory, 'Demo', 'JSON file', 'json file.json'
# )
# print(json_file_path)
# if path.exists(json_file_path):
#    print("Hello JSON")

#
# xml_file_path= path.join(
# current_directory, 'Demo', 'XML File', 'xmlfile.xml'
# )
# print(xml_file_path)
# if path.exists(xml_file_path):
#     print("HEllo XML ")

#
# txt_file_path = path.join(
# current_directory, 'Demo', 'Txt File', 'Txtfile.txt'
# )
# print(txt_file_path)
# if path.exists(txt_file_path):
#     print("Hello TXT")
# csv_file_path= path.join(
# current_directory, 'Demo', 'CSV_File', 'csvfile.csv'
# )
# print(csv_file_path)
# if path.exists(csv_file_path):
#     print("HEllo CSV")
#
# class_09 = path.join(
# current_directory, 'Demo', 'class_09', 'Test_directory'
# )
# print(class_09)
#mkdir(class_09)

# if not path.exists(class_09):
#     makedirs(class_09)
#     print('Create new directory named class_09')
#
#
# file_data= """
# This is my text file and i want to write anything in this file.
# You could not stop me whatever I want to do i will do it.
# That's it.
# """

# file_obj = open(txt_file_path, 'w+')
# file_obj.writelines(file_data)
# file_obj.close()
# with open(txt_file_path, 'r+')as txt_file:
#     txt_file.writable(file_data)
#
# with open(txt_file_path, 'r+') txt_file_read:
#     file_data = txt_file_read.readlines()
#     print(file_data)
# with open(txt_file_path, 'r+')as txt_file_read:
#     for line in txt_file_read:
#         print(line.replace("\n", ' '))


# def generator_parse_file(file_path):
#     with open(file_path, 'r+') as txt_file:
#         for line in text_file:
#             yield line.replace('\n' , '')
#
# for i in generator_parse_file(txt_file_path):
#     print(i)


