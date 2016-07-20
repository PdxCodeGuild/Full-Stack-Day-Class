"""Program that prints out PDX Code Guild class rosters."""

from student import Student
from roster import Roster


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


def main():
    """Main function.

    Sets up some example students, then prints the intro email.
    """
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
