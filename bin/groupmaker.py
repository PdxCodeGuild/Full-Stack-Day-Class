#!/usr/bin/env python3
"""Make student groups, ensuring that students work with those they have worked
with the fewest times before.
"""
import argparse
import sys
from collections import Iterable
from functools import reduce
from itertools import (chain, combinations_with_replacement, filterfalse,
                       permutations, zip_longest)

from tabulate import tabulate


def is_none(x):
    """Return if a variable is None.

    >>> is_none('A')
    False
    >>> is_none(None)
    True
    """
    return x is None


def is_container(x):
    """Return if the input is a container of other elements, but not a string.

    >>> is_container(['1'])
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
    return [i if not is_container(i) else rlist(i) for i in l]


def rsorted(l):
    """Recursively sort nested iterables by their string value.

    Just a convenience function for doctesting.

    >>> rsorted(frozenset({'B', frozenset({'C', 'A'})}))
    ['B', ['A', 'C']]
    >>> rsorted(frozenset({'B', None, frozenset({'C', None, 'A'})}))
    ['B', None, ['A', 'C', None]]
    >>> rsorted(frozenset({
    ...                    frozenset({frozenset({'C'})}),
    ...                    frozenset({frozenset({None})})}))
    [[['C']], [[None]]]
    """
    return sorted((i if not is_container(i) else rsorted(i) for i in l),
                  key=str)


def pairs(group):
    """Given a group of people, return a tuple pairs generator.

    Nones are ignored in the group.
    Tuple pairs are only emitted in sorted order.

    >>> list(pairs(['A', 'B']))
    [('A', 'A'), ('A', 'B'), ('B', 'B')]
    >>> list(pairs(['A', None]))
    [('A', 'A')]
    >>> list(pairs(['B', 'A']))
    [('A', 'A'), ('A', 'B'), ('B', 'B')]
    >>> list(pairs(['A', 'C', 'B', None]))
    [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]
    """
    group_without_nones = filterfalse(is_none, group)
    sorted_group = sorted(group_without_nones)
    pair_lists = combinations_with_replacement(sorted_group, 2)
    pair_tuples = map(tuple, pair_lists)
    return pair_tuples


def calc_pair_to_count_of_group(group):
    """Given a group return that each pair was grouped together once.

    Only the sorted pairs are keys.

    >>> sorted(calc_pair_to_count_of_group(['A', 'B']).items())
    [(('A', 'A'), 1), (('A', 'B'), 1), (('B', 'B'), 1)]
    """
    return {pair: 1 for pair in pairs(group)}


def sum_count_dict(count_dict1, count_dict2):
    """Sum two dicts from key to count by unique key.

    >>> sorted(sum_count_dict({'A': 1, 'B': 1}, {'B': 1, 'C': 3}).items())
    [('A', 1), ('B', 2), ('C', 3)]
    """
    out_count_dict = dict(count_dict1)
    for key, sum_num in count_dict2.items():
        if key not in out_count_dict:
            out_count_dict[key] = 0
        out_count_dict[key] += sum_num
    return out_count_dict


def calc_pair_to_count_of_groups(groups):
    """Count how often each pair exists in some groups.

    Only the sorted pairs are keys.

    >>> sorted(calc_pair_to_count_of_groups([['A', 'B'], ['A']]).items())
    [(('A', 'A'), 2), (('A', 'B'), 1), (('B', 'B'), 1)]
    """
    return reduce(sum_count_dict, map(calc_pair_to_count_of_group, groups))


def calc_pair_to_count_of_groups_set(groups_set):
    """Count how often each pair exists in a set of groups.

    >>> sorted(calc_pair_to_count_of_groups_set(
    ...     [[['A'], ['B']], [['A', 'B']]]).items())
    [(('A', 'A'), 2), (('A', 'B'), 1), (('B', 'B'), 2)]
    """
    return reduce(sum_count_dict,
                  map(calc_pair_to_count_of_groups, groups_set),
                  {})


def pair(name1, name2):
    """Manually pair two names in order for comparison to a pair count dict.

    >>> pair('B', 'A')
    ('A', 'B')
    """
    return tuple(sorted((name1, name2)))


def calc_names_count_matrix(names, groups_set):
    """Produce a matrix of how often names have been paired together in a set
    of groups.

    Returns an ordered list of names and the matrix in that order.

    >>> calc_names_count_matrix(['A', 'B'],
    ...                         [[['A', 'B']], [['A']]])
    (['A', 'B'], [[2, 1], [1, 1]])
    >>> calc_names_count_matrix(['B', 'A'],
    ...                         [[['A', 'B']], [['A']]])
    (['A', 'B'], [[2, 1], [1, 1]])
    >>> calc_names_count_matrix(['A', 'B'],
    ...                         [[['A']], [['A']]])
    (['A', 'B'], [[2, 0], [0, 0]])
    """
    names = sorted(names)
    pair_to_count = calc_pair_to_count_of_groups_set(groups_set)
    count_matrix = [
        [
            pair_to_count.get(pair(name1, name2), 0)
            for name2
            in names
        ]
        for name1
        in names
    ]
    return names, count_matrix


def score_group(group, historical_pair_to_count):
    """Given a group and a historical pair counts, return a score of how many times group members have been paired
    together before.

    The higher the score, the more frequently they've been grouped together.

    >>> score_group(
    ...     ['A', 'B', 'C'],
    ...     {('A', 'B'): 1, ('A', 'C'): 1})
    4
    """
    return sum(
        historical_pair_to_count.get(pair, 0)
        for pair
        in pairs(group)
    ) ** 2


def score_groups(groups, historical_pair_to_count):
    """Given a set of groups and a historical pair counts, return a score of how many times group members have been paired
    together before

    The higher the score, the more frequently they've been grouped together.

    >>> score_groups(
    ...     [['A', 'B'], ['C', 'D']],
    ...     {('A', 'B'): 1, ('C', 'D'): 1})
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


def all_groups_set(students, group_size):
    """Generate all possible unique groups of a given size from all students.
    Very permutive.

    >>> rsorted(all_groups_set(['A', 'B', 'C'], 2))
    ... # doctest: +NORMALIZE_WHITESPACE
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
    ...     [[['A', 'B'], ['C', 'D']], [['A', 'C'], ['D', 'B']]],
    ...     {('A', 'B'): 2, ('B', 'D'): 1})
    [['A', 'C'], ['D', 'B']]
    """
    def score_groups_with_historical_pair_counts(groups):
        return score_groups(groups, historical_pair_to_count)

    return min(groups_set, key=score_groups_with_historical_pair_counts)


def gen_min_scoring_groups(students, group_size, historical_groups_set):
    """Figure out what is the minimum-scoring group out of all possible groups
    of some students.

    >>> rsorted(gen_min_scoring_groups(['A', 'B', 'C'],
    ...                                2,
    ...                                [[['A', 'B']], [['B', 'C']]]))
    [['A', 'C'], ['B', None]]
    """
    return min_scoring_groups(
        all_groups_set(students, group_size),
        calc_pair_to_count_of_groups_set(historical_groups_set))


def parse_groups_file(groups_file):
    r"""Take a groups file and return all of the groups in it.

    A groups file contains a student name on each line with a blank line
    between groups.

    >>> rsorted(parse_groups_file(['A\n', 'B\n', '\n', 'C\n']))
    [['A', 'B'], ['C']]
    """
    working_group = set()
    for name in map(str.strip, chain(groups_file, [''])):
        if name != '':
            working_group.add(name)
        elif len(working_group) > 0:
            yield tuple(sorted(working_group))
            working_group = set()


def print_groups_file(groups):
    """Print out a groups file.

    >>> print_groups_file([['A', 'B'], ['C', None]])
    A
    B
    <BLANKLINE>
    C
    """
    print('\n\n'.join('\n'.join(student for student in group
                                if student is not None) for group in groups))


def print_name_count_matrix(names, count_matrix, file=sys.stderr):
    """Print a matrix of names and counts.

    >>> print_name_count_matrix(['A', 'B', 'C'],
    ...                         [[0, 1, 1], [1, 0, 2], [1, 2, 0]],
    ...                         sys.stdout)
    +----+-----+-----+-----+
    |    |   A |   B |   C |
    |----+-----+-----+-----|
    | A  |   0 |   1 |   1 |
    | B  |   1 |   0 |   2 |
    | C  |   1 |   2 |   0 |
    +----+-----+-----+-----+
    """
    table = [[name] + counts for name, counts in zip(names, count_matrix)]
    print(tabulate(table, names, tablefmt='psql'), file=file)


def parse_students_file(students_file):
    r"""Read student file and return a sorted list of the students.

    A student file contains one student name on each line.

    >>> sorted(parse_students_file(['A\n', 'B\n', '\n']))
    ['A', 'B']
    """
    unique_names = (frozenset(name.strip() for name in students_file) -
                    frozenset({''}))
    return tuple(sorted(unique_names))


def parse_groups_file_paths(groups_file_paths):
    """Read all historical groups from a list of groups file paths.

    Return a set of all historical groups.
    """
    for groups_file_path in groups_file_paths:
        with open(groups_file_path) as groups_file:
            yield tuple(parse_groups_file(groups_file))


def main(students_file_path, group_size, historical_groups_file_paths,
         verbosity):
    """Read a list of students, a requested group size, and historical groups,
    then generate a new group of the requested size with the fewest students
    that have worked together before.
    """
    with open(students_file_path) as students_file:
        students = parse_students_file(students_file)
    historical_groups_set = list(parse_groups_file_paths(
        historical_groups_file_paths))

    if verbosity > 0:
        historical_names, historical_count_matrix = calc_names_count_matrix(
            students,
            historical_groups_set)
        print_name_count_matrix(historical_names, historical_count_matrix)

    min_scoring_groups = gen_min_scoring_groups(students, group_size,
                                                historical_groups_set)
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
    parser.add_argument(
        '-v',
        dest='verbosity',
        action='count',
        default=0,
        help='print out historical pair counts to stderr before calculating '
             'new groups')
    parser.add_argument('student_file_path',
                        metavar='STUDENT_FILE',
                        help='file containing student names, one per line')
    parser.add_argument(
        'historical_groups_file_paths',
        metavar='GROUP_FILE',
        nargs='*',
        help='files containing previous groups, one student per line, one '
        'blank line between groups')

    args = parser.parse_args()
    main(args.student_file_path, args.group_size,
         args.historical_groups_file_paths, args.verbosity)
