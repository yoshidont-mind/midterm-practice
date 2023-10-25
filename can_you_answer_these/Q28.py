def count_duplicates(given_dictionary):
    """
    Calculate the number of values that appear two or more times in the dictionary.

    :param given_dictionary: a dictionary
    :precondition: given_dictionary must be a dictionary
    :postcondition: the number of values that appear two or more times in given_dictionary is calculated correctly
    :return:the number of values that appear two or more times in given_dictionary

    >>> count_duplicates({'red': 1, 'green': 1, 'blue': 4})
    1
    >>> count_duplicates({'red': 1, 'green': 1, 'blue': 4, 'orange': 6, 'purple': 4, 'black': 2})
    2
    """

    result = 0
    appeared_times = {}

    for value in given_dictionary.values():
        if value in appeared_times.keys():
            appeared_times[value] += 1
            if appeared_times[value] == 2:
                result += 1
        else:
            appeared_times[value] = 1
    return result
