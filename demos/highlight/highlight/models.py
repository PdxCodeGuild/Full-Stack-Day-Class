"""highlight Models"""


class ColoredSource:
    """Colored source code and language."""

    def __init__(self, language_name, source_html):
        """Wrap together an existing language and colored source HTML."""
        self.language_name = language_name
        self.source_html = source_html
