def falsy(parameter):
    if parameter:
        print(f'{parameter} is truthy!')
    else:
        print(f'{parameter} is falsy!')


def main():
    falsy(False)
    falsy([0, 0, 0, 0, 0])
    falsy(None)
    falsy({})
    falsy("")
    falsy("  ")
    falsy(0)
    falsy(0.0)
    falsy(range(1, 1))
    falsy(range(0, 0))


if __name__ == '__main__':
    main()
