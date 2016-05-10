from django.http import HttpResponse
from django.shortcuts import render

from . import logic


def render_ack(request):
    """Accepts a POST of a comment and renders the ack."""
    comment_text = request.GET['comment_text']

    logic.save_comment(comment_text)

    return HttpResponse('')


def render_index(request):
    """Renders the listing of previous comments page.
    """
    comments = logic.get_all_comments()

    context = {
        'comments': comments,
    }
    return render(request, 'comments/ajax_index.html', context)
