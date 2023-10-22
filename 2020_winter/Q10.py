def do_something(l1, l2):
    result = []
    i1 = 0
    i2 = 0
    while i1 != len(l1) and i2 != len(l2):
        if l1[i1] <= l2[i2]:
            result.append(l1[i1])
            i1 += 1
        else:
            result.append(l2[i2])
            i2 += 1
    return result


def main():
    some_names = ['Kat', 'Kirk', 'Kyle', 'Kyrill']
    more_names = ['Saida', 'Sepehr', 'Silvana', 'Simon']
    so_many_names = do_something(more_names, some_names)
    print(so_many_names)


if __name__ == '__main__':
    main()
