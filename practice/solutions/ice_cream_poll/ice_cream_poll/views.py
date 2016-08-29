"""ice_cream_poll Views."""
from django.shortcuts import render

from . import models
from . import logic


def render_ballot(request):
    """Render the ballot page that allows a user to vote for a candidate."""
    template_arguments = {
        'candidates': models.get_all_candidates(),
    }
    return render(request, 'ice_cream_poll/ballot.html', template_arguments)


def render_ballot_ack(request):
    """Render the ballot ack page.

    It accepts the candidate, records the vote, and displays who was voted for.
    """
    candidate = request.POST['candidate']

    models.vote_for_candidate(candidate)

    template_arguments = {
        'candidate': candidate,
    }
    return render(request, 'ice_cream_poll/ballot_ack.html', template_arguments)


def render_summary(request):
    """Render the summary page showing percentages of votes for each candidate thus far."""
    template_arguments = {
        'candidate_to_fraction': _convert_fraction_dict_to_percentage_dict(logic.calculate_vote_fractions()),
    }
    return render(request, 'ice_cream_poll/summary.html', template_arguments)


def _convert_fraction_dict_to_percentage_dict(candidate_to_fraction):
    """Convert a dictionary from candidate to vote fraction (<= 1.0) to candidate to vote percentage (<= 100.0).

    >>> sorted(_convert_fraction_dict_to_percentage_dict({'a': 0.25, 'b': 0.75}).items())
    [('a', 25.0), ('b', 75.0)]
    """
    return {
        candidate: _convert_fraction_to_percentage(fraction)
        for candidate, fraction
        in candidate_to_fraction.items()
    }


def _convert_fraction_to_percentage(fraction):
    """Convert a fraction (<= 1.0) to a percentage (<= 100.0).

    >>> _convert_fraction_to_percentage(0.5)
    50.0
    """
    return fraction * 100.0
