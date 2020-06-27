# вот такой вариант мне сразу пришел в голову

l = [1, 2, 3, [5, 6, [7, 8]], 9]


def flat_list(lst):
    lst2 = list()
    for elem in lst:
        if not isinstance(elem, list):
            lst2.append(elem)
        else:
            lst2.extend(flat_list(elem))
    return lst2


# наверное я плохо искал
# но с помощью itertools нашел только способ для такого листа

import itertools

l2 = [[1, 2], [3], [5, 6], [7, 8], [9]]
iter_tool_list = list(itertools.chain.from_iterable(l2))

# но нашел в iteration_utilities

import iteration_utilities

iter_utility = list(iteration_utilities.deepflatten(l))
