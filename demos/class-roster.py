class_name_to_students = {}

student_name = None
while student_name != 'done':
    print('Student name or done? ')
    student_name = input()
    if student_name != 'done':
        print('What class is ' + student_name + ' in? ')
        class_name = input()
        if not class_name in class_name_to_students:
            class_name_to_students = {student_name}
        else:
            class_name_to_students[class_name] |= {student_name}

print()
print('Class Rosters')
for class_name in class_name_to_students:
    students_in_class = class_name_to_students[class_name]
    print(class_name + ': ' + ', '.join(students_in_class))
