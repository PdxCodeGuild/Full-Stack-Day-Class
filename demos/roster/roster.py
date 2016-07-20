class Roster:
    def __init__(self, students, instructor_name):
        self.students = students
        self.instructor_name = instructor_name

    def __repr__(self):
        return 'Roster({!r}, {!r})'.format(
            self.students,
            self.instructor_name,
        )

    def __eq__(self, other):
        return (
            self.students == other.students and
            self.instructor_name == other.instructor_name
        )
