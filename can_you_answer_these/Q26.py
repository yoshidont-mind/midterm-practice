def find_duplicates(given_list):
    """
    Identify a list of the integers that occur more than once in the original list.

    :param given_list: a list of integers
    :precondition: given_list must be a list of integers
    :postcondition: a new list of the integers that occur more than once in the original list is calculated correctly
    :return: a new list of the integers that occur more than once in the original list

    >>> find_duplicates([1, 2, 2, 4, 5, 5])
    [1, 2, 4, 5]
    >>> find_duplicates([3, 5, 1, 5, 3, 2, 1, 3, 5])
    [3, 5, 1, 2]
    """

    result = []
    for integer in given_list:
        if integer not in result:
            result.append(integer)
    return result

