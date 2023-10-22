def name_list():
    """
    Create a dictionary in which entered names are classified based on number of letters.

    :precondition: the user must be ready for entering the names
    :postcondition: the names are classified based on their lengths and put in lists included in a dictionary correctly
    :return: a dictionary containing lengths of names as the keys and lists of the names as the values
    """

    destination_dictionary = {}
    continue_key = True

    print("You are being asked to enter names. Once you've done entering all the names, please enter 'quit'.")

    while continue_key:
        name = input("Please enter the next name: \n")

        if name == "quit":
            continue_key = False
        elif len(name) in destination_dictionary.keys():
            destination_dictionary[len(name)].append(name)
        else:
            destination_dictionary[len(name)] = [name]

    return destination_dictionary


print(name_list())
