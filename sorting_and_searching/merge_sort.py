# Merge sort is recursive algorithm that continually splits a list in half.
# If the list is empty or has one item, it is sorted already.
# If list has more than item we split the list in half.
# Then recursively invoke/call merge sort on both halves.
# Once two halves are sorted, we call merge.
# Merge takes two smaller sorted list and combines them together in a single,
# sorted, new list.

# merge :: (List) --> sorted list
def merge_sort(alist):
    """
    Takes an unsorted list, splits in half
    and recursively sorts those list until
    there is only one element in the list
    then it calls the merge method to sort
    those list
    :param alist:
    :return: sorted_alist

    >>> merge_sort([4, 3, 6, 5, 8, 7])
    [3, 4, 5, 6, 7, 8]
    """
    # Step 1: Base case
    if len(alist) < 2:
        return 1
    # Step 2: Split list in half
    mid = len(alist) // 2
    left = alist[:mid]
    right = alist[mid:]

    for i in range(mid):
        left[i] = alist[i]

    for i in range(mid, len(alist) - 1):
        right[i - mid] = alist[i]

    # Step 3: Sort left and right
    merge_sort(left)
    merge_sort(right)
    merge(left, right, alist)

    return alist


## THE TWO LIST PASSED INTO MERGE ARE ALREADY SORTED!!!!
## DON'T FORGET THAT (SEE ABOVE ALL CAPS SENTENCE
# merge :: (ListL, ListR) --> Sorted List
def merge(left, right, clist):
    """
    Takes two sorted list and returns a clist
    :param left:
    :param right:
    :return: clist

    >>> merge([3, 4, 5], [6, 7, 8], [4, 6, 8, 3, 5, 7])
    [3, 4, 5, 6, 7, 8]
    """
    i = 0
    j = 0
    k = 0
    while i <= len(left) - 1 and j <= len(right) - 1:
        if left[i] < right[j]:
            clist[k] = left[i]
            i = i + 1
        else:
            clist[k] = right[j]
            j = j + 1
        k = k + 1

    while i < len(left):
        clist[k] = left[i]
        i = i + 1

    while j < len(right):
        clist[k] = right[j]
        j = j + 1
    # .... [3, 4, 5, 6, 7, 8]
    return clist


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # print(merge([3, 5, 7], [4, 6, 8]))
