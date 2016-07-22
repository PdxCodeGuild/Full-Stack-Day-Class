"""Program that prints out PDX Code Guild class rosters."""

from student import Student
from roster import Roster
from roster import write_intro_email


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
