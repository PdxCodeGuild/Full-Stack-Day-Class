"""Download a URL specified on the command line and prints the result.

USAGE: webgetter.py URL
"""
import sys
import requests


def main():
    """Get URL from command line, download contents, print result."""
    url = sys.argv[1]
    response = requests.get(url)
    print(response.text)


if __name__ == '__main__':
    main()
