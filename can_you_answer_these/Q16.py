def identify_first_occurrence(given_string):
    """
    Identify the first occurrence of the entered character.

    :param given_string: a string
    :precondition: given_string must be a string
    :precondition: user must enter a single character
    :postcondition: the first occurrence of the entered character in given_string is correctly identified
    :return: the index of the first occurrence of the character in the string, or -1 if it does not exist
    """

    destination_character = input("Please enter a single character: ")
    destination_index = -1

    for index in range(0, len(given_string)):
        if given_string[index] == destination_character:
            destination_index = index
            break

    return destination_index
