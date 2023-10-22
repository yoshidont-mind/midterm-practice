def obfuscate(sequence, modifier):
    for index, _ in enumerate(sequence):
        sequence[index] = modifier(sequence[index])


def surprise(value):
    value *= 2


def main():
    collection = ["a", "b", "c"]
    obfuscate(collection, surprise)
    print(collection)


if __name__ == "__main__":
    main()
