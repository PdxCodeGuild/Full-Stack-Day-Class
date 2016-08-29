"""ice_cream_poll Logic."""
from . import models


def calculate_vote_fractions():
    """Calculate and return the candidate to vote fractions (<= 1.0)."""
    return _calculate_vote_fractions(models.get_candidate_to_vote_count())


def _calculate_vote_fractions(candidate_to_vote_count):
    """From a dictionary from candidate to vote count, calculate candidate to vote fractions (<= 1.0).

    >>> sorted(_calculate_vote_fractions({'a': 1, 'b': 3}).items())
    [('a', 0.25), ('b', 0.75)]
    >>> sorted(_calculate_vote_fractions({'a': 0, 'b': 0}).items())
    [('a', 0.0), ('b', 0.0)]
    """
    total_votes = sum(candidate_to_vote_count.values()) or 1
    return {
        candidate: vote_count / total_votes
        for candidate, vote_count
        in candidate_to_vote_count.items()
    }
