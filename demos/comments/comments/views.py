from django.http import HttpResponse
from django.shortcuts import render

from . import logic


def render_submit_form(request):
    """Renders the page that asks a user for a new comment."""
    return render(request, 'comments/submit_form.html', {})


def render_ack(request):
    """Accepts a POST of a comment and renders a success or failure page if the
    comment was valid."""
    # Remember, the HTML input name attributes need to match up with the keys
    # in the POST dictionary here.
    comment_text = request.POST['comment_text']
    comment_author = request.POST['comment_author']

    new_comment = logic.Comment(comment_text, comment_author)

    # You can return different templates based on what happend.
    # Only return the success template if it was a "good" comment.
    if logic.is_comment_valid(new_comment):
        logic.save_comment(new_comment)

        template_arguments = {
            'comment': new_comment,
        }
        return render(request, 'comments/ack_succ.html', template_arguments)
    else:
        return render(request, 'comments/ack_fail.html', {})


def render_index(request):
    """Renders the listing of previous comments page."""
    # Use .get to prevent KeyError.
    author = request.GET.get('author')

    if author is None:
        comments = logic.get_all_comments()
    else:
        comments = logic.get_comments_for_author(author)

    all_authors = logic.get_all_authors()

    template_arguments = {
        'comments': comments,
        'author': author,
        'all_authors': all_authors,
    }
    return render(request, 'comments/index.html', template_arguments)
