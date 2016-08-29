"""comments Models."""


class Comment:
    """Value type that represents a posted comment.

    It has some text and an author.
    """

    def __init__(self, text, author):
        self.text = text
        self.author = author

    def __eq__(self, other):
        return self.text == other.text and self.author == other.author

    def __repr__(self):
        return 'Comment({}, {})'.format(self.text, self.author)


_COMMENTS = []


def get_all_comments():
    """Return all comments in submitted order."""
    return _COMMENTS


def get_comments_for_author(author):
    """Return all comments written by an author in submitted order."""
    return _filter_comments_for_author(_COMMENTS, author)


# Have this private function that is doctestable, but doesn't have access to the DB data.
def _filter_comments_for_author(comments, author):
    """Filter a list of comments to just those of a given author.

    >>> _filter_comments_for_author([Comment('1', 'Bob'), Comment('2', 'Alice')], 'Alice')
    [Comment('2', 'Alice')]
    """
    return [comment for comment in comments if comment.author == author]


def add_new_comment(text, author):
    """Validate and add a new comment to the comment DB then return it.

    If an invalid comment is submitted, a ValueError is raised.

    >>> add_new_comment('Great!', 'David')
    Comment('Great!', 'David')
    >>> add_new_comment('', '')
    Traceback (most recent call last)
        ...
    ValueError: comment is invalid
    """
    if is_comment_valid(text, author):
        new_comment = Comment(text, author)
        _COMMENTS.append(new_comment)
        return new_comment
    else:
        raise ValueError('comment is invalid')


def is_comment_valid(text, author):
    """Return if a comment is valid.

    Valid comments have non-empty text and author.

    >>> is_comment_valid('Great!', 'David')
    True
    >>> is_comment_valid('', 'David')
    False
    >>> is_comment_valid('Great!', '')
    False
    """
    return len(text) > 0 and len(author) > 0
