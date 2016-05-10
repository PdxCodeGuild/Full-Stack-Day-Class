comments = []


def save_comment(comment_text):
    """Save a new comment.
    """
    comments.append(comment_text)


def get_all_comments():
    """Return all previously saved comments as a list of strings."""
    return comments
