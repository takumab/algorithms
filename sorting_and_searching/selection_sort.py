"""
Selection Sort:
    ...find the smallest unsorted element and add it to the
    sorted list.
    Pseudocode:
        Repeat until no unsorted elements remain:
            --> Search the unsorted part of the data to find the smallest value
            --> Swap the smallest found value with the first element of the unsorted part
"""


# selection_sort :: unsorted_list -> sorted_list
def selection_sort(unsorted_list):
    """Takes an unsorted_list and returns a sorted list
    >>> selection_sort([3, 2, 1])
    [1, 2, 3]
    """
    sorted_list = []
    while len(unsorted_list) != 0:
        # find_smallest number in list
        smallest = find_smallest(unsorted_list)
        # move smallest number to sorted
        move_smallest_to_sorted(sorted_list, smallest)
        remove_unsorted_element(unsorted_list, smallest)
    return sorted_list


# find_smallest :: List -> Integer
def find_smallest(xs):
    """Takes a list of numbers and returns the smallest number
    >>> find_smallest([3, 2, 1])
    1
    """
    acc = xs[0]
    smallest = None
    for x in range(0, len(xs)):
        if xs[x] > acc:
            smallest = acc
        else:
            smallest = xs[x]
            acc = smallest
    # ...n
    return acc


# move_smallest_to_sorted :: smallest_num --> sorted_list
def move_smallest_to_sorted(sorted, smallest):
    """Takes smallest number from find_smallest() and moves it to the sorted_list
    >>> move_smallest_to_sorted([1, 2], 3)
    [1, 2, 3]
    """
    sorted.append(smallest)
    return sorted


# remove_unsorted_list :: (List, Integer) --> List
def remove_unsorted_element(original_unsorted_list, smallest_num):
    """Remove unsorted element from list
    >>> remove_unsorted_element([3,2,1], 1)
    [3, 2]
    """
    smallest_index = original_unsorted_list.index(smallest_num)
    original_unsorted_list.pop(smallest_index)
    return original_unsorted_list


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(selection_sort([5, 7, 2, 6, 8, 4, 1, 3, 10, 0, 25]))
