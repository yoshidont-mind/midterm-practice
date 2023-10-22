def modify_dict(some_dictionary):
    some_dictionary["b"].append(4)


def modify_list(some_list):
    some_list.append(4)


def modify_tuple(some_tuple):
    some_tuple = some_tuple + (4, )
    

def modify_set(any_old_set):
    any_old_set.add(4)


def main():
    my_dict = {"a": {"b": [1, 2, 3]}, "c": {"d": {"e": 4}}}
    my_list = [1, 2, 3]
    my_tuple = (1, 2, 3)
    my_set = {1, 2, 3}
    modify_dict(my_dict["a"])
    modify_list(my_list)
    modify_tuple(my_tuple)
    modify_set(my_set)
    print(my_dict["a"]["b"])
    print(my_list)
    print(my_tuple)
    print(my_set)


if __name__ == "__main__":
    main()
