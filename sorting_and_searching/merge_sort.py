# Merge sort is recursive algorithm that continually splits a list in half.
# If the list is empty or has one item, it is sorted already.
# If list has more than item we split the list in half.
# Then recursively invoke/call merge sort on both halves.
# Once two halves are sorted, we call merge.
# Merge takes two smaller sorted list and combines them together in a single,
# sorted, new list.


# merge :: (List1, List2) --> merged_sorted_list
def merge(alist, blist):
    """
    Takes two sorted list and returns a merged_sorted_list
    :param alist:
    :param blist:
    :return: merged_sorted_list

    >>> merge([3, 4, 5], [6, 7, 8])
    [3, 4, 5, 6, 7, 8]
    """
    merged_sorted_list = []
    while len(alist) != 0 and len(blist) != 0:
    # for i in range(len(alist)):
    #     if alist[i] < blist[i]:
    #         merged_sorted_list.append(alist[i])
    #     else:
    #         merged_sorted_list.append(blist[i])
    # .... [3, 4, 5, 6, 7, 8]
    return merged_sorted_list


if __name__ == "__main__":
    import doctest

    doctest.testmod()
