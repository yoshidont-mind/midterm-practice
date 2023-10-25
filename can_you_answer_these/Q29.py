def is_balanced(given_dictionary):
    """
    Determine whether the color is balanced.

    :param given_dictionary: a dictionary whose keys are ‘R’, ‘G’, and ‘B’, and whose values are between 0 and 1
    :precondition: given_dictionary must be a dictionary
    :precondition: the keys of given_dictionary must be ‘R’, ‘G’, and ‘B’
    :precondition: the values of given_dictionary must be between 0 and 1
    :postcondition: whether the color is balanced id determined correctly
    :return: True or False of if they represent a balanced colour

    >>> is_balanced({'R': 0.3, 'G': 0.4, 'B': 0.3})
    True
    >>> is_balanced({'R': 0.3, 'G': 0.4, 'B': 0.4})
    False
    """

    sum_of_colors = sum(given_dictionary.values())
    return sum_of_colors == 1.0

