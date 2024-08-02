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

student_attendance = {}
a = open('attendance_sheet.csv', 'r')
print(a)
next(a)
for row in a:
        name = row.split(',')[0]
        status = row.split(',')[1].strip()
        student_attendance[name] = status
print(student_attendance) 