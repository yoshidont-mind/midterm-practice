"""
contents of docstrings and main functions are omitted
"""


def full_empty_decision(full, empty):
    """

    :param full:
    :param empty:
    :return:

    >>> full_empty_decision(True, False)
    True
    >>> full_empty_decision(True, True)
    False
    >>> full_empty_decision(False, True)
    True
    >>> full_empty_decision(False, False)
    False
    """
    return full and not empty or not full and empty