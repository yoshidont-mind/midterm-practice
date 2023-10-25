# global scope
PI = 3.14


def median_circle_area(first_radius, second_radius, third_radius):
    # local scope
    list_of_the_numbers = [first_radius, second_radius, third_radius]
    list_of_the_numbers.sort()
    return PI * (list_of_the_numbers[1] ** 2) # here we can access variables in both of global scope and local scope


print(median_circle_area(2.3, 3.5, 2.6))  # print function is in built-in scope
