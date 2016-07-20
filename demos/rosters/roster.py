"""Module containing Roster class."""
# If you use any classes just in doctests, you have to import them also.
from student import Student


class Roster:
    """All of the information about a single PDX Code Guild class.

    Contains a list of students and an instructor name.
    """

    def __init__(self, students, instructor_name):
        self.students = students
        self.instructor_name = instructor_name

    def __repr__(self):
        """Return repr.

        >>> repr(Roster([Student('David', 'david@david.com')], 'Helen'))
        "Roster([Student('David', 'david@david.com')], 'Helen')"
        """
        return 'Roster({!r}, {!r})'.format(
            self.students,
            self.instructor_name,
        )

    def __eq__(self, other):
        """Check for equality.

        >>> (
        ...     Roster([Student('David', 'david@david.com')], 'Helen') ==
        ...     Roster([Student('David', 'david@david.com')], 'Helen')
        ... )
        True
        >>> (
        ...     Roster([Student('David', 'david@david.com')], 'Helen') ==
        ...     Roster([Student('Helen', 'helen@helen.com')], 'David')
        ... )
        False
        """
        return (
            self.students == other.students and
            self.instructor_name == other.instructor_name
        )
