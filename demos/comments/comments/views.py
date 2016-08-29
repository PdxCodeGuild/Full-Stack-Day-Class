"""comments Views."""
from django.http import HttpResponse
from django.shortcuts import render

from . import models


def render_index(request):
    """Render listing of all comments or comments by a specific author."""
    # Use .get to prevent KeyError.
    author = request.GET.get('author')

    if author is None:
        comments = models.get_all_comments()
    else:
        comments = models.get_comments_for_author(author)

    template_arguments = {
        'comments': comments,
        'no_comments': len(comments) < 1,
        'author': author,
    }
    return render(request, 'comments/index.html', template_arguments)


def render_comment_form(request):
    """Render new comment form."""
    return render(request, 'comments/comment_form.html')


def render_comment_ack(request):
    """Render comment submission acknowledgement."""
    try:
        text = request.POST['text']
        author = request.POST['author']
    except KeyError:
        return HttpResponse('missing comment fields', status=400)
    try:
        comment = models.add_new_comment(text, author)
    except ValueError:
        return render(request, 'comments/comment_ack_fail.html')
    template_arguments = {
        'comment': comment,
    }
    return render(request, 'comments/comment_ack_succ.html', template_arguments)
