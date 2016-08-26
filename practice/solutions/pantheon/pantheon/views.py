"""pantheon Views."""
from operator import itemgetter

from django.http import HttpResponse
from django.shortcuts import render

from . import models
from .settings import GOOGLE_MAPS_API_KEY


def _sort_countries(countries):
    """Sort a list of country dicts by country name.

    >>> _sort_countries([
    ...     {'countryCode': 'US', 'countryName': 'United States'},
    ...     {'countryCode': 'IN', 'countryName': 'India'},
    ... ]) == [
    ...     {'countryCode': 'IN', 'countryName': 'India'},
    ...     {'countryCode': 'US', 'countryName': 'United States'},
    ... ]
    True
    """
    return sorted(countries, key=itemgetter('countryName'))


def render_country_list(request):
    """View that renders a list of all known Pantheon person countries in alphabetical order."""
    countries = models.get_countries()

    template_arguments = {
        'countries': _sort_countries(countries),
    }
    return render(request, 'pantheon/countries.html', template_arguments)


def render_industry_list_for_country(request, country_code):
    """View that renders all industries in alphabetical order for Pantheon persons in a given country by country code.
    """
    try:
        country = models.get_country_by_code(country_code)
        industries = models.get_industries_for_country(country_code)
    except KeyError:
        return HttpResponse('no country with code {}'.format(country_code), status=404)

    template_arguments = {
        'country': country,
        'industries': sorted(industries),
    }
    return render(request, 'pantheon/industry.html', template_arguments)


def _sort_people(people):
    """Sort a list of people dicts by name.

    >>> _sort_people([
    ...     {'name': 'Sarah', 'industry': 'ACTIVIST'},
    ...     {'name': 'David', 'industry': 'OUTLAW'},
    ...     {'name': 'Helen', 'industry': 'ACTIVIST'},
    ... ]) == [
    ...     {'name': 'David', 'industry': 'OUTLAW'},
    ...     {'name': 'Helen', 'industry': 'ACTIVIST'},
    ...     {'name': 'Sarah', 'industry': 'ACTIVIST'},
    ... ]
    True
    """
    return sorted(people, key=itemgetter('name'))


def render_person_list_for_country_industry(request, country_code, industry):
    """View that renders a list of Pantheon people in alphabetical order in a given country and industry."""
    try:
        country = models.get_country_by_code(country_code)
    except KeyError:
        return HttpResponse('no country with code {}'.format(country_code), status=404)

    try:
        people = models.get_people_for_industry_for_country(country_code, industry)
    except KeyError:
        return HttpResponse('no people in industry {}'.format(industry), status=404)

    template_arguments = {
        'country': country,
        'industry': industry,
        'people': _sort_people(people),
    }
    return render(request, 'pantheon/people.html', template_arguments)


def _get_gender_background_class(gender):
    """Return the CSS class that should be applied to the body of the person page based on gender.

    >>> _get_gender_background_class('Female')
    'female-background'
    >>> _get_gender_background_class('Male')
    'male-background'
    >>> _get_gender_background_class('Other')
    ''
    """
    first_letter = gender[0].lower()
    if first_letter == 'f':
        return 'female-background'
    elif first_letter == 'm':
        return 'male-background'
    else:
        return ''


def render_person(request, person_id):
    """View that renders info about a single Pantheon person by ID."""
    try:
        person = models.get_person_by_id(person_id)
    except KeyError:
        return HttpResponse('no person with ID {}'.format(person_id), status=404)

    template_arguments = {
        'person': person,
        'gender_class': _get_gender_background_class(person['gender']),
        'google_maps_api_key': GOOGLE_MAPS_API_KEY,
    }
    return render(request, 'pantheon/person.html', template_arguments)
