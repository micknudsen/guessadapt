class GuessAdaptError(Exception):
    """Base class for all guessadapt exceptions."""


class ParserError(GuessAdaptError):

    def __init__(self, message):
        self.message = message
