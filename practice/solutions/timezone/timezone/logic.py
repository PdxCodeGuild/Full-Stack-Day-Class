"""timezone Logic."""
import arrow
from tzwhere.tzwhere import tzwhere


print('Loading tzwhere... ', end='')
TZ_FINDER = tzwhere()
print('done.')


def get_current_server_time():
    """Return the current time in the server's timezone."""
    return arrow.now()


def get_timezone_for(lat_lng):
    """Find the timezone at a location.

    >>> get_timezone_for((35.29, -89.66))
    'America/Chicago'
    """
    lat, lng = lat_lng
    return TZ_FINDER.tzNameAt(lat, lng)


def translate_time_to_location(time, lat_lng):
    """Return a given time in the timezone at a location.

    >>> translate_time_to_location(
    ...     arrow.get('2016-08-25T10:40:15-07:00'),
    ...     (35.29, -89.66)
    ... )
    <Arrow [2016-08-25T12:40:15-05:00]>
    """
    lat_lng_tz = get_timezone_for(lat_lng)
    if lat_lng_tz is not None:
        return time.to(lat_lng_tz)
    else:
        raise ValueError('no timezone at {},{}'.format(*lat_lng))


def get_current_location_time(lat_lng):
    """Return the current time in the timezone at a location."""
    server_time = get_current_server_time()
    return translate_time_to_location(server_time, lat_lng)
