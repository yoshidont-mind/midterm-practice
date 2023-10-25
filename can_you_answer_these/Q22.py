def mystery_function(values):
    result = []
    for sublist in values:
        result.append([sublist[0]])
        for i in sublist[1:]:
            result[-1].insert(0, i)
    return result


print(mystery_function([[100, 50, 40], [30, 20, 40], [10, 15, 20]]))
print(mystery_function(['tatsuya', 'masatoshi', 'naoko']))
print(mystery_function([['tatsuya', 'masatoshi', 'naoko'], ['asuka', 'yuya', 'daisuke']]))
