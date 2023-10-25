def dict_intersect(first_dictionary, second_dictionary):
    """
    Identify keyvalue pairs found in both of the original dictionaries.

    :param first_dictionary: a dictionary
    :param second_dictionary: a dictionary
    :precondition: first_dictionary must be a dictionary
    :postcondition: second_dictionary must be a dictionary
    :return: a new dictionary that contains only the keyvalue pairs found in both of the original dictionaries

    >>> dict_intersect({'country': 'Japan', 'name': 'Tatsuya'}, {'country': 'Japan', 'name': 'Tatsunori'})
    {'country': 'Japan'}
    """

    new_dictionary = {}

    for key, value in first_dictionary.items():
        if key in second_dictionary.keys():
            if second_dictionary[key] == value:
                new_dictionary[key] = value
    return new_dictionary
