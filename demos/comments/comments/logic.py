# Use a global variable as the place to store comments.
# We have to do this since Django is calling our views for us;
# we can't get the list of comments in the call stack.
comments = []


class Comment:
    """Class which represents a single comment.

    It has text and author attributes.
    """
    def __init__(self, text, author):
        self.text = text
        self.author = author

    def __repr__(self):
        return 'Comment({!r}, {!r})'.format(self.text, self.author)


def is_comment_valid(comment):
    """Returns if a comment instance is valid.

    This is if both of the fields are not empty.
    """
    return len(comment.text) > 0 and len(comment.author) > 0


def save_comment(new_comment):
    """Save a new comment."""
    comments.append(new_comment)


def get_all_comments():
    """Return all previously saved comments as a list of Comment instances."""
    return comments


def get_all_authors():
    """Return a set of all previously saved authors."""
    all_comments = get_all_comments()
    return set(comment.author for comment in all_comments)


def get_comments_for_author(author=None):
    """Return all previously saved comments from a specifc author as a list of
    Comment instances."""
    return [
        comment
        for comment
        in comments
        if comment.author == author
    ]
