def add_one(some_list):
    for index in range(len(some_list)):
        some_list[index] += 1


def remove_even(some_list):
    index = 0
    while index < len(some_list):
        if some_list[index] % 2 == 0:
            some_list.pop(index)
        else:
            index += 1


def square_all(some_list):
    new_list = []
    for item in some_list:
        new_list.append(item ** 2)
    some_list = new_list


def main():
    my_list = [1, 2, 3, 4, 5]
    add_one(my_list)
    remove_even(my_list)
    new_list = my_list
    square_all(my_list)
    print(my_list)
    print(new_list)


if __name__ == "__main__":
    main()
