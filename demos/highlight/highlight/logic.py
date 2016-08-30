"""highlight Logic."""
import pygments
import pygments.formatters
import pygments.lexers

from . import models


HTML_FORMATTER = pygments.formatters.HtmlFormatter(noclasses=True)


def color_source(source_str):
    """Take source code as a string, guess what language it is, and return an
    HTML highlighted version of it.

    Returns the guessed language and HTML highlighted version as a
    ColoredSource instance.
    """
    lexer = pygments.lexers.guess_lexer(source_str)
    colored_source_html = pygments.highlight(
        source_str,
        lexer,
        HTML_FORMATTER,
    )
    return models.ColoredSource(lexer.name, colored_source_html)
