"""periodic Views."""
from django.http import HttpResponse
from django.shortcuts import render

from .models import ELEMENTS
from .models import SYMBOL_TO_ELEMENT


def render_index(request):
    """Render the index of all elements."""
    template_arguments = {
        'elements': ELEMENTS,
    }
    return render(request, 'periodic/index.html', template_arguments)


def render_element(request, symbol):
    """Lookup an element by symbol and render its info page."""
    try:
        element = SYMBOL_TO_ELEMENT[symbol]
    except KeyError:
        return HttpResponse('no element with symbol', status=404)
    template_arguments = {
        'element': element,
    }
    return render(request, 'periodic/element.html', template_arguments)
