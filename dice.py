# import modules
import math as m
import random as r

# set initial variables
total_result = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
count = 0

# simulate rolling and record the results
while count < 1000000:
    result = m.floor(r.random() * 6) + 1
    total_result[result] += 1
    count += 1

# print the result
for key, value in total_result.items():
    print(key, "appeared", value, "times.")
