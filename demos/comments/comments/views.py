from django.http import HttpResponse
from django.shortcuts import render

from . import logic


def render_form(request):
    """Renders the page that asks a user for a new comment.
    """
    return render(request, 'comments/form.html', {})


def render_ack(request):
    """Accepts a POST of a comment and renders the ack."""
    comment_text = request.POST['comment_text']

    logic.save_comment(comment_text)

    context = {
        'comment_text': comment_text,
    }
    return render(request, 'comments/ack.html', context)


def render_index(request):
    """Renders the listing of previous comments page.
    """
    comments = logic.get_all_comments()

    context = {
        'comments': comments,
    }
    return render(request, 'comments/index.html', context)
