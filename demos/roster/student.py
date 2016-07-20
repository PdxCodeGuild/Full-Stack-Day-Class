"""Module containing Student class."""


class Student:
    """A student in any PDX Code Guild Class.

    Contains both a name and email.
    """

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        """Return repr.

        >>> repr(Student('David', 'david@david.com'))
        "Student('David', 'david@david.com')"
        """
        return 'Student({!r}, {!r})'.format(
            self.name,
            self.email,
        )

    def __eq__(self, other):
        """Check for equality.

        >>> Student('David', 'david@david.com') == Student('David', 'david@david.com')
        True
        >>> Student('David', 'david@david.com') == Student('Helen', 'helen@helen.com')
        False
        """
        return (
            self.name == other.name and
            self.email == other.email
        )
