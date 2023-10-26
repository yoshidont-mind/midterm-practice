given_list = list(range(4)) * 3
given_list_2 = list(range(5, 9)) * 3
print(given_list)

print(given_list.index(2))
print(given_list.index(2, 3, 7))

given_list[3:8:2] = given_list_2[3:8:2]
print(given_list)
