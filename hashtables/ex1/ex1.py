# this passes the tests but it doesn't seem quite right. Specifically, it seems
# off for the cases that there are two+ items of the same weight.
# when the array has two equal weights, there are many edge cases not covered.
# say the limit is 8 and we are passed in [2, 6, 6, 6]; this does not handle that case.

def get_indices_of_item_weights(weights, length, limit):

    weights_dict = {}

    for index, weight in enumerate(weights):
        if weight in weights_dict:
            weights_dict[weight].append(index)
        else:
            weights_dict[weight] = [index]

    for weight, index in weights_dict.items():
        if (limit - weight) in weights_dict:
            if len(weights_dict[limit - weight]) > 1:
                if weight == limit - weight:
                    higher_index = weights_dict[limit - weight][1]
                    lower_index = weights_dict[limit - weight][0]
                    return (higher_index, lower_index)
                else:
                    return (weights_dict[limit - weight][1], weights_dict[weight][0])
            else:
                higher_index = weights_dict[limit - weight][0]
                lower_index = weights_dict[weight][0]
                return (higher_index, lower_index)

    return None
