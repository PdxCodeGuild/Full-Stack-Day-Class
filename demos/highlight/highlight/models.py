"""highlight Models."""


class ColoredSource:
    """Colored source code and language."""

    def __init__(self, language_name, source_html):
        """Wrap together an existing language and colored source HTML."""
        self.language_name = language_name
        self.source_html = source_html

    def __repr__(self):
        """

        >>> repr(ColoredSource('HTML', '<html></html>'))
        "ColoredSource('HTML', '<html></html>')"
        """
        return 'ColoredSource({!r}, {!r})'.format(
            self.language_name,
            self.source_html,
        )
