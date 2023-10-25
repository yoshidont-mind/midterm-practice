def count_times_appears(given_string):
    """
    Identify the number of times the entered letter appears in the string.

    :param given_string: a string
    :precondition: given_string must be a string
    :precondition: user must enter a single character
    :postcondition: the number of times the entered letter appears in given_string is correctly identified
    :return: the number of times the entered letter appears in given_string
    """

    destination_character = input("Please enter a single character: ")
    appeared_times = 0

    for index in range(0, len(given_string)):
        if given_string[index] == destination_character:
            appeared_times += 1

    return appeared_times


# print(count_times_appears("textdecoration"))
