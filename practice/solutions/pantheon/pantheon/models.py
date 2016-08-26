"""pantheon Models."""
import csv
from operator import itemgetter


# Start with a lot of functions that read and munge the data into useful data structures.

def _load_pantheon_data():
    """Load and return Pantheon data file as a list of person dictionaries."""
    print('Loading data...', end='')
    with open('pantheon/pantheon.tsv', encoding='utf-8') as tsv_file:
        reader = csv.DictReader(tsv_file, delimiter='\t')
        persons = list(reader)
    print('done')
    return persons


def group_by(iterable, key):
    """Place each item in an iterable into a bucket based on calling the key
    function on the item."""
    group_to_items = {}
    for item in iterable:
        group = key(item)
        if group not in group_to_items:
            group_to_items[group] = []
        group_to_items[group].append(item)
    return group_to_items


def _group_persons_by_country_code(people):
    """Group a list of people dicts by country code.

    >>> _group_persons_by_country_code([
    ...     {'name': 'David', 'countryCode': 'US'},
    ...     {'name': 'Helen', 'countryCode': 'GB'},
    ...     {'name': 'Sarah', 'countryCode': 'US'},
    ... ]) == {
    ...     'US': [{'name': 'David', 'countryCode': 'US'}, {'name': 'Sarah', 'countryCode': 'US'}],
    ...     'GB': [{'name': 'Helen', 'countryCode': 'GB'}],
    ... }
    True
    """
    return group_by(people, itemgetter('countryCode'))


def _group_persons_by_industry(people):
    """Group a list of people dicts by industry.

    >>> _group_persons_by_industry([
    ...     {'name': 'David', 'industry': 'OUTLAW'},
    ...     {'name': 'Helen', 'industry': 'ACTIVIST'},
    ...     {'name': 'Sarah', 'industry': 'ACTIVIST'},
    ... ]) == {
    ...     'ACTIVIST': [{'name': 'Helen', 'industry': 'ACTIVIST'}, {'name': 'Sarah', 'industry': 'ACTIVIST'}],
    ...     'OUTLAW': [{'name': 'David', 'industry': 'OUTLAW'}],
    ... }
    True
    """
    return group_by(people, itemgetter('industry'))


def _group_persons_by_country_code_then_industry(people):
    """Group a list of people dicts into two nested dicts, first by country code, then by industry.

    >>> _group_persons_by_country_code_then_industry([
    ...     {'name': 'David', 'countryCode': 'US', 'industry': 'OUTLAW'},
    ...     {'name': 'Helen', 'countryCode': 'GB', 'industry': 'ACTIVIST'},
    ...     {'name': 'Sarah', 'countryCode': 'US', 'industry': 'ACTIVIST'},
    ... ]) == {
    ...     'US': {
    ...         'ACTIVIST': [{'name': 'Sarah', 'countryCode': 'US', 'industry': 'ACTIVIST'}],
    ...         'OUTLAW': [{'name': 'David', 'countryCode': 'US', 'industry': 'OUTLAW'}],
    ...     },
    ...     'GB': {
    ...         'ACTIVIST': [{'name': 'Helen', 'countryCode': 'GB', 'industry': 'ACTIVIST'}],
    ...     }
    ... }
    True
    """
    country_code_to_people = _group_persons_by_country_code(people)
    country_code_to_industry_to_people = {
        country_code: _group_persons_by_industry(country_persons)
        for country_code, country_persons
        in country_code_to_people.items()
    }
    return country_code_to_industry_to_people


def _make_id_to_person(people):
    """Make a mapping from ID to person dict.

    >>> _make_id_to_person([
    ...     {'en_curid': '123', 'name': 'David'}
    ... ]) == {
    ...     '123': {'en_curid': '123', 'name': 'David'}
    ... }
    True
    """
    return {
        person['en_curid']: person
        for person
        in people
    }


def _make_country_code_to_country(people):
    """

    >>> _make_country_code_to_country([
    ...     {'countryCode': 'US', 'countryName': 'UNITED STATES'},
    ...     {'countryCode': 'IN', 'countryName': 'INDIA'},
    ... ]) == {
    ...     'IN': {'countryCode': 'IN', 'countryName': 'INDIA'},
    ...     'US': {'countryCode': 'US', 'countryName': 'UNITED STATES'},
    ... }
    True
    """
    return {
        person['countryCode']: {
            'countryCode': person['countryCode'],
            'countryName': person['countryName'],
        }
        for person
        in people
    }


# Run all of those functions so that we have the data.

_PEOPLE = _load_pantheon_data()
_COUNTRY_CODE_TO_COUNTRY = _make_country_code_to_country(_PEOPLE)
_ID_TO_PERSON = _make_id_to_person(_PEOPLE)
_COUNTRY_CODE_TO_INDUSTRY_TO_PEOPLE = _group_persons_by_country_code_then_industry(_PEOPLE)


# Now have some public functions that perform the common operations we want.
# Notice how easy they are once we make the right data structures above.

def get_countries():
    """Return a list of all known country dicts.

    Country dicts contain `countryCode` and `countryName` keys.
    """
    return _COUNTRY_CODE_TO_COUNTRY.items()


def get_country_by_code(country_code):
    """Lookup the country dict for a given country code."""
    return _COUNTRY_CODE_TO_COUNTRY[country_code]


def get_industries_for_country(country_code):
    """Return a list of industries with people in them for a given country."""
    return _COUNTRY_CODE_TO_INDUSTRY_TO_PEOPLE[country_code].keys()


def get_people_for_industry_for_country(country_code, industry):
    """Return a list of people dicts that match a given country and industry."""
    return _COUNTRY_CODE_TO_INDUSTRY_TO_PEOPLE[country_code][industry]


def get_person_by_id(en_curid):
    """Return a person dict for a given ID.

    Person dicts contain the field names from the original Pantheon TSV.
    E.g. `name`, `gender`, etc.
    """
    return _ID_TO_PERSON[en_curid]
