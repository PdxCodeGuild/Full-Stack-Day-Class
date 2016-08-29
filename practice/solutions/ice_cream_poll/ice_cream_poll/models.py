"""ice_cream_poll Models."""


_candidate_to_vote_count = {
    'vanilla': 0,
    'chocolate': 0,
    'strawberry': 0,
}


def get_all_candidates():
    """Return a list of all candidates."""
    return _candidate_to_vote_count.keys()


def vote_for_candidate(candidate):
    """Register a single vote for a candidate."""
    _candidate_to_vote_count[candidate] += 1


def get_candidate_to_vote_count():
    """Return a dictionary mapping from candidate to vote count."""
    return _candidate_to_vote_count
