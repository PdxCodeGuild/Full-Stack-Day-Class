class Student:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return 'Student({!r}, {!r})'.format(
            self.name,
            self.email,
        )

    def __eq__(self, other):
        return (
            self.name == other.name and
            self.email == other.email
        )
