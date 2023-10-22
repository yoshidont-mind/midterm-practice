def apply(container, modifier):
    for i, _ in enumerate(container):
        container[i] = modifier(container[i])


def modify(value):
    value *= 2


def main():
    information = [2, '2', 'Exam', 3.14]
    apply(information, modify)
    print(information)


if __name__ == "__main__":
    main()
