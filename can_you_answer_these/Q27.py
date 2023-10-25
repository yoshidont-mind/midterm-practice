def count_values(given_dictionary):
    """
    Identify the number of distinct values in the dictionary.

    :param given_dictionary: a dictionary
    :precondition: given_dictionary must be a dictionary
    :postcondition: the number of distinct values in given_dictionary is calculated correctly
    :return: the number of distinct values in given_dictionary

    >>> count_values({'red': 1, 'green': 1, 'blue': 4})
    2
    >>> count_values({'red': 1, 'green': 1, 'blue': 4, 'orange': 6, 'purple': 4, 'black': 2})
    4
    """

    result = 0
    appeared_already = []

    for value in given_dictionary.values():
        if value not in appeared_already:
            appeared_already.append(value)
            result += 1
    return result
