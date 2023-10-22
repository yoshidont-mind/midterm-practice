def median(first_operand, second_operand, third_operand):
    """
    Calculate the median.

    :param first_operand: an integer or a float
    :param second_operand: an integer or a float
    :param third_operand: an integer or a float
    :precondition: first_operand must be an integer or a float
    :precondition: second_operand must be an integer or a float
    :precondition: third_operand must be an integer or a float
    :postcondition: the median is calculated correctly
    :return: the number which is the median

    >>> median(1, 5, 3)
    3
    >>> median(2.3, 2.3, 1.2)
    2.3
    """

    list_of_the_numbers = [first_operand, second_operand, third_operand]
    list_of_the_numbers.sort()
    return list_of_the_numbers[1]
