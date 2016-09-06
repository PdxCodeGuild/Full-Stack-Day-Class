"""highlight Logic."""
import pygments
import pygments.formatters
import pygments.lexers

from . import models


HTML_FORMATTER = pygments.formatters.HtmlFormatter(noclasses=True)


def color_source(source_str):
    r"""Take source code as a string, guess what language it is, and return an
    HTML highlighted version of it.

    Returns the guessed language and HTML highlighted version as a
    ColoredSource instance.

    >>> color_source('#!/bin/bash')
    ColoredSource('Bash', '<div class="highlight" style="background: #f8f8f8"><pre style="line-height: 125%"><span></span><span style="color: #408080; font-style: italic">#!/bin/bash</span>\n</pre></div>\n')
    """
    lexer = pygments.lexers.guess_lexer(source_str)
    colored_source_html = pygments.highlight(
        source_str,
        lexer,
        HTML_FORMATTER,
    )
    return models.ColoredSource(lexer.name, colored_source_html)
