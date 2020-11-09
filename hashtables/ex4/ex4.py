def has_negatives(a):

    positive_numbers = {}
    negative_numbers = {}
    result = []

    for element in a:
        if element >= 0:
            if element not in positive_numbers:
                positive_numbers[element] = True
        elif element < 0:
            element = element * -1
            if element not in negative_numbers:
                negative_numbers[element] = True
    
    for key in positive_numbers:
        if key in negative_numbers:
            result.append(key)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
