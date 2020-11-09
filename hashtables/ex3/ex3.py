def intersection(arrays):

    # array to return
    result = []
    # variable to store the number of individual arrays passed in
    number_arrays = len(arrays)
    # dictionary to hold the numbers as keys and their appearance
    # in the given arrays as values.
    intersect_dict = {}

    # iterate through the main, outside, array to touch each inside array
    for array in arrays:
        # iterate through the inside array
        # if the number is not in the dict, add it
        # increment the value by one
        for element in array:
            if element not in intersect_dict:
                intersect_dict[element] = 0
            intersect_dict[element] += 1
    
    # check the values of the dictionary keys and if
    # a value equals the number of arrays passed in,
    # that means the number intersected all arrays.
    for key, value in intersect_dict.items():
        if value == number_arrays:
            result.append(key)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
