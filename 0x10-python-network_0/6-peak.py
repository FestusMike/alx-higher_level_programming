#!/usr/bin/python3
""" Find the peak of an unsorted list of integers """


def search(low, high, ints):
    """
    Recursively search for a peak element within a subarray
    of integers.

    Args:
        low (int): The index of the lower bound of the subarray.
        high (int): The index of the upper bound of the subarray.
        ints (list[int]): The list of integers to search within.

    Returns:
        int: The peak element found within the specified subarray,
             or None if the list is empty.
    """
    mid = (low + high) // 2

    if low == high:
        return ints[high]
    if ints[mid] < ints[mid + 1]:
        return search(mid + 1, high, ints)

    return search(low, mid, ints)


def find_peak(list_of_integers):
    """
    Find a peak element within an unsorted list of integers.

    Args:
        list_of_integers (list[int]): The list of integers to
        search for a peak.

    Returns:
        int: The peak element found within the list, or
        None if the list is empty.
    """
    if not list_of_integers:
        return None

    return search(0, len(list_of_integers) - 1, list_of_integers)
