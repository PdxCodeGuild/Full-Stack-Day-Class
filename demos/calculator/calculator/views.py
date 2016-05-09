from django.http import HttpResponse


def render_plus(request):
    lhs = int(request.GET['x'])
    rhs = int(request.GET['y'])
    total = lhs + rhs
    return HttpResponse(str(total))


def render_minus(request):
    lhs = int(request.GET['x'])
    rhs = int(request.GET['y'])
    diff = lhs - rhs
    if diff <= 0:
        return HttpResponse(status=400)
    return HttpResponse(str(diff))
