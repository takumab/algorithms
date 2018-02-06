# Merge sort is recursive algorithm that continually splits a list in half.
# If the list is empty or has one item, it is sorted already.
# If list has more than item we split the list in half.
# Then recursively invoke/call merge sort on both halves.
# Once two halves are sorted, we call merge.
# Merge takes two smaller sorted list and combines them together in a single,
# sorted, new list.

## THE TWO LIST PASSED INTO MERGE ARE ALREADY SORTED!!!!
## DON'T FORGET THAT (SEE ABOVE ALL CAPS SENTENCE
# merge :: (ListL, ListR, List1) --> Sorted List
def merge(left, right):
    """
    Takes two sorted list and returns a clist
    :param left:
    :param right:
    :return: clist

    >>> merge([3, 4, 5], [6, 7, 8])
    [3, 4, 5, 6, 7, 8]
    """
    i = 0
    j = 0
    k = 0
    clist = []
    while i < len(left) - 1 and j < len(right) - 1:
        if left[i] < right[j]:
            clist.append(left[i])
            i = i + 1
        else:
            clist.append(right[j])
            j = j + 1
        k = k + 1

    while i < len(left):
        clist.append(left[i])
        i = i + 1

    while j < len(right):
        clist.append(right[j])
        j = j + 1
    # .... [3, 4, 5, 6, 7, 8]
    return clist


if __name__ == "__main__":
    import doctest

    doctest.testmod()
