#!/usr/bin/env python3
"""Script that will check Markdown files for broken links.

USAGE: mdlinklint.py MK_FILES...
"""
from contextlib import contextmanager
from os import path
from urllib.parse import urlparse
from urllib.request import urlopen
import os
import re
import subprocess
import sys


MD_LINK_RE = re.compile(r'\[(.+?)\]\((.+?)\)')


@contextmanager
def cd(new_wd):
    """Perform a block in a different working directory."""
    if new_wd != '':
        old_wd = os.getcwd()
        os.chdir(new_wd)
    try:
        yield
    finally:
        if new_wd != '':
            os.chdir(old_wd)


def get_git_repo_root(dir_path):
    """Return the path to the Git repo root that exists below a directory."""
    with cd(dir_path):
        response_bytes = subprocess.check_output(
            'git rev-parse --show-toplevel',
            shell=True)
    return response_bytes.decode('utf-8')


def get_parent_dir(child_path):
    """Given a path, return a path to the parent directory.

    >>> get_parent_dir('parent/child/grandchild')
    'parent/child'
    """
    parent_dir_path, _ = path.split(child_path)
    return parent_dir_path


def follow_path(path_rel_to_start_dir, start_dir):
    """For a path relative to a second path, return the resulting path.

    >>> follow_path('../otherchild', 'parent/child')
    'parent/otherchild'
    >>> follow_path('/parent', '/grandparent')
    '/grandparent/parent'
    """
    return path.normpath(path.join(start_dir, path_rel_to_start_dir))


def parse_dest(dest):
    """Parse a link destination and return the type of link and the destination
    path.

    >>> parse_dest('one.txt#a')
    ('rel', 'one.txt')
    >>> parse_dest('../two.txt')
    ('rel', '../two.txt')
    >>> parse_dest('/three.txt#a')
    ('abs', '/three.txt')
    >>> parse_dest('http://four.com/five')
    ('url', 'http://four.com/five')
    """
    parsed_dest = urlparse(dest)
    if parsed_dest.scheme == '':
        if parsed_dest.path.startswith('/'):
            return ('abs', parsed_dest.path)
        else:
            return ('rel', parsed_dest.path)
    else:
        return ('url', dest)


def print_line(file_path, line_num, char_num, text):
    print('{}:{}:{} {}'.format(file_path, line_num, char_num, text))


def find_all_links(lines):
    """Go through the lines of a Markdown file and return info about all of the
    links found.

    >>> find_all_links(['This is [a link](location).'])
    (1, 8, 'location', '[a link](location)')
    """
    for line_num, line in enumerate(lines):
        for match in MD_LINK_RE.finditer(line):
            match_text = match.group()
            char_num = match.start()
            dest = match.group(2)
            yield (line_num + 1, char_num, dest, match_text)


def main():
    errors_exist = False
    for file_path in sys.argv[1:]:
        file_dir_path = get_parent_dir(file_path)
        with open(file_path) as fp:
            for link in find_all_links(fp):
                line_num, char_num, dest, match_text = link
                link_type, dest_path = parse_dest(dest)
                if link_type == 'rel':
                    check_path = follow_path(dest_path, file_dir_path)
                    broken_link = not path.exists(check_path)
                elif link_type == 'abs':
                    repo_dir_path = get_git_repo_root(file_dir_path)
                    check_path = follow_path(dest_path, repo_dir_path)
                    broken_link = not path.exists(check_path)
                else:
                    broken_link = False

                if broken_link:
                    print_line(file_path, line_num, char_num, match_text)
                    errors_exist = True
    return 1 if errors_exist else 0


if __name__ == '__main__':
    sys.exit(main())
