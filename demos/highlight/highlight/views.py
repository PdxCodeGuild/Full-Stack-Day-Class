"""highlight Views"""
from django.http import JsonResponse
from django.shortcuts import render

from . import logic


def render_index(request):
    """Render the main source form page."""
    return render(request, 'highlight/index.html')


def _convert_colored_source_to_json_obj(colored_source):
    """Convert a ColoredSource instance into a JSON-encodable object."""
    # This is the object that will appear in the JS.
    return {
        'language': colored_source.language_name,
        'source_html': colored_source.source_html,
    }


def return_color(request):
    """JSON endpoint which takes in some source code from POST and returns a
    JSON of the guessed language and HTML colored source.
    """
    source_str = request.POST['source-str']
    colored_source = logic.color_source(source_str)
    colored_source_json_obj = _convert_colored_source_to_json_obj(
        colored_source)
    return JsonResponse(colored_source_json_obj)
