given_list = [4353, 2314, 2956, 3382, 9362, 3900]

given_list.remove(3382)
index = given_list.index(9362)
given_list.insert(index + 1, 4499)
given_list.extend([5566, 1830])
given_list.reverse()
given_list.sort()

print(given_list)
