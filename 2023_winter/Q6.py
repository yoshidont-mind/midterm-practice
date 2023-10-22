def main():
    my_dict = {"a": {"b": {1, 2}}, "c": {"d": {"e": [3, 4]}}}
    my_set = my_dict["a"]["b"]
    my_set.add(3)
    my_dict["c"]["d"]["e"] += [5]
    print(my_dict)


if __name__ == "__main__":
    main()
