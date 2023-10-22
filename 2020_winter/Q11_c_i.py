TOLERANCE = 0.0001

a = 25.00000001
b = 25.00000002

if abs(a - b) < TOLERANCE:
    print('a is close enough to b for my program')
else:
    print('a is not close enough to b for my program')
