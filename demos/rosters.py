class Student:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return 'Student({!r}, {!r})'.format(self.name, self.email)


class ClassRoster:
    def __init__(self, instructor, students):
        self.instructor = instructor
        self.students = students

    def __repr__(self):
        return 'ClassRoster({!r}, {!r})'.format(
            self.instructor, self.students)


def calc_num_students(cgclass):
    return len(cgclass.students)


def find_all_studen_emails(cgclass):
    return [student.email for student in cgclass.students]


def draft_email(cgclass):
    to_line = 'To: ' + ', '.join(find_all_studen_emails(cgclass)) + '\n'
    body = 'There are {} people in the class.\n\nSincerely, {}'.format(
        calc_num_students(cgclass),
        cgclass.instructor)
    return to_line + body


def main():
    you = Student('Helen', 'helen@helen.com')
    day_class = ClassRoster('David', [you])
    print(draft_email(day_class))

main()
