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


def collect_emails(students):
    """Collects student emails from a list of students.

    >>> collect_emails([
    ...     Student('David', 'david@david.com'),
    ...     Student('Helen', 'helen@helen.com'),
    ... ])
    ['david@david.com', 'helen@helen.com']
    """
    return [student.email for student in students]


def write_intro_email(roster):
    # Remember, if a doctest has backslashes in it, raw-escape the whole docstring with `r`.
    r"""Given a class roster, return the intro email.

    The intro email

    >>> print(write_intro_email(Roster(
    ...     [Student('David', 'david@david.com'), Student('Helen', 'helen@helen.com')],
    ...     'Meg',
    ... )))  # Call print() so that the output doesn't need quotes. Doctest just compares output.
    ... # Use `<BLANKLINE>` to represent a blank line in the output.
    To: david@david.com,helen@helen.com
    <BLANKLINE>
    Meg will be teaching the class.
    There are 2 students in it.
    """
    return (
        'To: {}\n\n' +
        '{} will be teaching the class.\n' +
        'There are {} students in it.'
    ).format(
        ','.join(collect_emails(roster.students)),
        roster.instructor_name,
        len(roster.students),
    )
