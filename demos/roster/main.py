from student import Student
from roster import Roster


def collect_emails(students):
    """
    >>> collect_emails([Student('David', 'david@david.com'), Student('Helen', 'helen@helen.com')])
    ['david@david.com', 'helen@helen.com']
    """
    return [student.email for student in students]


def write_intro_email(roster):
    r"""

    >>> write_intro_email(Roster([Student('David', 'email1'), Student('Helen', 'email2')], 'Inst'))
    'To: email1,email2\n\nInst will be teaching the class.\nThere are 2 students in it.'
    """
    return 'To: {}\n\n{} will be teaching the class.\nThere are {} students in it.'.format(
        ','.join(collect_emails(roster.students)),
        roster.instructor_name,
        len(roster.students),
    )


def main():
    students = [
        Student('Alice', 'alice@alice.com'),
        Student('Bob', 'bob@bob.com'),
        Student('Mel', 'mel@mel.com'),
    ]
    roster = Roster(students, 'David')

    intro_email = write_intro_email(roster)

    print(intro_email)



if __name__ == '__main__':
    main()
