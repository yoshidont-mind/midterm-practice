def cleaner(measurements, maximum):
    """
    Make a new list consists only of numbers smaller than a certain number.

    :param measurements: a non-empty list which contains only floats
    :param maximum: a float
    :precondition: measurements must be a non-empty list
    :precondition: measurements must consist only of floats
    :precondition: maximum must be a float
    :postcondition: numbers smaller than maximum are identified correctly and included in the new list
    :return: a list which consists only numbers that are in measurements and smaller than maximum
    """

    destination_list = []
    for number in measurements:
        if number < maximum:
            destination_list.append(number)

    return destination_list


def main():
    test_measurements = [2.3, 3.4, 4.5]
    test_maximum = 3.5
    print("When the list", test_measurements, "and the number", test_maximum, "are passed, ")
    print("the result is", cleaner(test_measurements, test_maximum))


if __name__ == '__main__':
    main()
