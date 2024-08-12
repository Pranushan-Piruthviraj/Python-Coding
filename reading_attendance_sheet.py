# import csv

# student_attendance = {}

# with open('attendance_sheet.csv', 'r') as csv_file:
# # with open('C:\\Users\\rajpa\\Downloads\\Python\\Python-Coding\\attendance_sheet.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)
#     next(csv_file)
#     for row in csv_reader:
#         name = row[0]
#         status = row[1]
#         student_attendance[name] = status
# print(student_attendance) 

# student_attendance = {}

# with open('attendance_sheet.csv', 'r') as csv_file:
#     next(csv_file)
#     for row in csv_file:
#         name = row.split(',')[0]
#         status = row.split(',')[1].strip()
#         student_attendance[name] = status
# print(student_attendance) 

# student_attendance = {}
# a = open('attendance_sheet.csv', 'r')
# for row in a:
#         name = row.split(',')[0]
#         status = row.split(',')[1].strip()
#         student_attendance[name] = status
# print(student_attendance) 

# student_attendance = {}
# a = open('attendance_sheet.csv', 'r')
# data = a.readlines()
# #print(data)
# #print(data[1:])
# for row in data[1:]:
#         name = row.split(',')[0]
#         status = row.split(',')[1].strip()
#         student_attendance[name] = status
# print(student_attendance) 


#Method three: use read and readlines method to read csv (read: https://docs.python.org/3/library/io.html#io.TextIOBase) 
#Method four: Use pandas module using import panda to read csv

student_attendance = {}
import pandas as pd
df = pd.read_csv('attendance_sheet.csv')
#print(df)
for index, row in df.iterrows():
    name = row['Name of the student']
    #print(name)
    status = row['Attendance']
    #print(status)
    student_attendance[name] = status
print(student_attendance)
