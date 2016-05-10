from django.http import HttpResponse

from . import logic


def convert_check_input(arg):
    """
    """
    int_arg = int(arg)
    if int_arg < 0:
        raise ValueError('argument is negative')
    else:
        return int_arg


def render_plus(request):
    """
    """
    try:
        x = convert_check_input(request.GET['x'])
    except ValueError:
        return HttpResponse('x must be positive int', status=400)
    try:
        y = convert_check_input(request.GET['y'])
    except ValueError:
        return HttpResponse('y must be positive int', status=400)
    return x, y

    total = x + y

    return HttpResponse(str(total))


def render_minus(request):
    """
    """
    try:
        x = convert_check_input(request.GET['x'])
    except ValueError:
        return HttpResponse('x must be positive int', status=400)
    try:
        y = convert_check_input(request.GET['y'])
    except ValueError:
        return HttpResponse('y must be positive int', status=400)
    return x, y

    diff = x - y

    return HttpResponse(str(diff))
