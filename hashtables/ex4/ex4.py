def has_negatives(a):

    # create a dictionary for positive numbers and another for negatives
    # we will simply iterate through one of the dictionaries and see if
    # its key is also in the other dictionary (absolute value of numbers)
    positive_numbers = {}
    negative_numbers = {}
    result = []

    # iterate through array and put each number in the corresponding dictionary
    for element in a:
        if element >= 0:
            if element not in positive_numbers:
                positive_numbers[element] = True
        elif element < 0:
            # if the number is negaive, make it positive so we can easily compare
            element = element * -1
            if element not in negative_numbers:
                negative_numbers[element] = True
    
    # iterate through dictionary to check for matches
    # if we find a match, append it to the results array
    for key in positive_numbers:
        if key in negative_numbers:
            result.append(key)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
