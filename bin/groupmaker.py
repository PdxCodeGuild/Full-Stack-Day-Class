#!/usr/bin/env python3
"""Make student groups, ensuring that students work with those they have worked
with the fewest times before.
"""
import argparse
from collections import Iterable
from itertools import chain, combinations, permutations, zip_longest


def is_container(x):
    """Return if the input is a true container. Not a string.

    >>> is_container([1, 2])
    True
    >>> is_container('Hi')
    False
    >>> is_container(frozenset({}))
    True
    """
    return isinstance(x, Iterable) and not isinstance(x, str)


def rlist(l):
    """Recursively turn nested iterables into lists.

    >>> rlist(('A', ('B', )))
    ['A', ['B']]
    """
    return [
        i if not is_container(i) else rlist(i)
        for i
        in l
    ]


def rsorted(l):
    """Recursively sort nested iterables.

    >>> rsorted(frozenset({'B', frozenset({'C', 'A'})}))
    ['B', ['A', 'C']]
    """
    return sorted(
        (i if not is_container(i) else rsorted(i) for i in l),
        key=str)


def pairs(group):
    """Given a group of people, produce frozenset pairs.

    >>> rsorted(pairs(['A', 'B', 'C']))
    [['A', 'B'], ['A', 'C'], ['B', 'C']]
    """
    return map(frozenset, combinations(group, 2))


def calc_pair_to_count(groups):
    """Given a list of groups, calculate a mapping from pairs to how often
    they have been grouped together.

    >>> sorted(
    ...     (sorted(pair), count)
    ...     for pair, count
    ...     in calc_pair_to_count([['A', 'B', 'C'], ['B', 'C']]).items()
    ... )
    [(['A', 'B'], 1), (['A', 'C'], 1), (['B', 'C'], 2)]
    """
    pair_to_count = {}
    for group in groups:
        for pair in pairs(group):
            if pair not in pair_to_count:
                pair_to_count[pair] = 0
            pair_to_count[pair] += 1
    return pair_to_count


def score_group(group, historical_pair_to_count):
    """Given a group and a historical pair counts, return how many times
    group members have been paired together before.

    >>> score_group(
    ...     ['A', 'B', 'C', None],
    ...     {frozenset(['A', 'B']): 1, frozenset(['A', 'C']): 1}
    ... )
    2
    """
    return sum(historical_pair_to_count.get(pair, 0) for pair in pairs(group))


def score_groups(groups, historical_pair_to_count):
    """Given a set of groups and a historical pair counts, return how many
    times group members have been paired together before.

    >>> score_groups(
    ...     [['A', 'B', 'C'], ['D', 'E', None]],
    ...     {frozenset(['A', 'B']): 1, frozenset(['D', 'E']): 1})
    2
    """
    return sum(score_group(group, historical_pair_to_count)
               for group in groups)


def chunk(iterable, size):
    """Take an iterable and chunk it into iterables of a given size.
    Remaining chunks are fleshed out with Nones.

    >>> rlist(chunk([1, 2, 3, 4], 3))
    [[1, 2, 3], [4, None, None]]
    """
    copies = [iter(iterable)] * size
    return zip_longest(*copies)


def all_groups(students, group_size):
    """Generate all possible unique groups of a given size from all students.
    Very permutive.

    >>> rsorted(all_groups(['A', 'B', 'C'], 2))
    [[['A', 'B'], ['C', None]],
     [['A', 'C'], ['B', None]],
     [['A', None], ['B', 'C']]]
    """
    return frozenset(frozenset(frozenset(group)
                               for group in chunk(ordering, group_size))
                     for ordering in permutations(students))


def min_scoring_groups(groups_set, historical_pair_to_count):
    """Given a list of possible groups and historical pair counts, return which
    has the minimum score.

    >>> min_scoring_groups(
    ...     [[['A', 'B'], ['C', 'D']], [['A', 'C'], ['B', 'D']]],
    ...     {frozenset(['A', 'B']): 1, frozenset(['C', 'D']): 1}
    ... )
    [['A', 'C'], ['B', 'D']]
    """
    def score_groups_with_historical_pair_counts(groups):
        return score_groups(groups, historical_pair_to_count)

    return min(groups_set, key=score_groups_with_historical_pair_counts)


def gen_min_scoring_groups(students, group_size, historical_groups):
    """Figure out what is the minimum-scoring group out of all possible groups
    of some students.

    >>> rsorted(gen_min_scoring_groups(['A', 'B', 'C'],
    ...                                2,
    ...                                {frozenset({'A', 'B'}): 1,
    ...                                 frozenset({'B', 'C'}): 1}))
    [['A', 'C'], ['B', None]]
    """
    return min_scoring_groups(
        all_groups(students, group_size),
        calc_pair_to_count(historical_groups))


def parse_groups_file(groups_file):
    r"""Take a groups file and return all of the groups in it.

    >>> rsorted(parse_groups_file(['A\n', 'B\n', '\n', 'C\n']))
    [['A', 'B'], ['C']]
    """
    working_group = set()
    for name in map(str.strip, chain(groups_file, [''])):
        if name != '':
            working_group.add(name)
        elif len(working_group) > 0:
            yield frozenset(working_group)
            working_group = set()


def print_groups_file(groups):
    print('\n\n'.join('\n'.join(student for student in group
                                if student is not None) for group in groups))


def parse_students_file(students_file):
    return frozenset(name.strip() for name in students_file) - frozenset({''})


def parse_groups_file_paths(groups_file_paths):
    historical_groups = set()
    for groups_file_path in groups_file_paths:
        with open(groups_file_path) as groups_file:
            historical_groups.add(parse_groups_file(groups_file))
    return frozenset(historical_groups)


def main(students_file_path, group_size, groups_file_paths):
    with open(students_file_path) as students_file:
        students = parse_students_file(students_file)
    historical_groups = parse_groups_file_paths(groups_file_paths)

    min_scoring_groups = gen_min_scoring_groups(students, group_size,
                                                historical_groups)
    print_groups_file(min_scoring_groups)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        '-n',
        dest='group_size',
        metavar='GROUP_SIZE',
        type=int,
        default=3,
        help='form groups of this many students (default: %(default)s)')
    parser.add_argument('student_file_path',
                        metavar='STUDENT_FILE',
                        help='file containing student names, one per line')
    parser.add_argument(
        'group_file_paths',
        metavar='GROUP_FILE',
        nargs='*',
        help='files containing previous groups, one student per line, one '
        'blank line between groups')

    args = parser.parse_args()
    main(args.student_file_path, args.group_size, args.group_file_paths)
