given_dictionary = {'A': (80.0, 100.0), 'B': (60.0, 78.0), 'C': (90.0, 96.0), 'D': (34.0, 65.0), 'F': (22.3, 76.8)}

for key, value in given_dictionary.items():
    print(f'{key} is {value[0]} to {value[1]} percent.')
