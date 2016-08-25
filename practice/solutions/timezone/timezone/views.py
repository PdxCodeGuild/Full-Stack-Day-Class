"""timezone Views."""
from django.http import HttpResponse
import arrow
from arrow.parser import ParserError

from . import logic


def _parse_lng_lat(lng_lat_str):
    """Parses a 'lat,lng' location string to a lat, lng float pair.

    >>> _parse_lng_lat('12.34,56.78')
    (12.34, 56.78)
    >>> _parse_lng_lat('12.34')
    Traceback (most recent call last):
        ...
    ValueError: not 'lng,lat' str: '12.34'
    """
    lng_lat = tuple(float(coord_str) for coord_str in lng_lat_str.split(','))
    if len(lng_lat) != 2:
        raise ValueError("not 'lng,lat' str: {!r}".format(lng_lat_str))
    return lng_lat


def render_local_server_time(_):
    """View that renders the current time in the server's timezone in ISO format."""
    current_server_time = logic.get_current_server_time()
    return HttpResponse(current_server_time.isoformat())


def render_location_timezone(_, lat_lng_str):
    """View that renders the timezone string at a location."""
    try:
        lat_lng = _parse_lng_lat(lat_lng_str)
    except ValueError:
        return HttpResponse('bad location', status=400)
    timezone_str = logic.get_timezone_for(lat_lng)
    if timezone_str is not None:
        return HttpResponse(timezone_str)
    else:
        return HttpResponse('no timezone', status=404)


def render_location_time(_, lat_lng_str):
    """View that renders the current time in the timezone at a location in ISO format."""
    try:
        lat_lng = _parse_lng_lat(lat_lng_str)
    except ValueError:
        return HttpResponse('bad location', status=400)
    try:
        lat_lng_current_time = logic.get_current_location_time(lat_lng)
    except ValueError:
        return HttpResponse('no timezone', status=400)
    return HttpResponse(lat_lng_current_time.isoformat())


def render_translated_time(_, time_str, lat_lng_str):
    """View that renders a given time in the local timezone at a location in ISO format."""
    try:
        time = arrow.get(time_str)
    except ParserError:
        return HttpResponse('bad timestamp', status='400')
    try:
        lat_lng = _parse_lng_lat(lat_lng_str)
    except ValueError:
        return HttpResponse('bad location', status=400)
    lat_lng_time = logic.translate_time_to_location(time, lat_lng)
    return HttpResponse(lat_lng_time.isoformat())
