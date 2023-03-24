def merge_lists(list_1, list_2):
    """ Returns a new list which is
        a combination of list_a and list_b
        without any duplicate elements.
    """
    return list(set(list_1) | set(list_2))

if __name__ == "__main__":
    print(merge_lists([1, 1, 2, 3], [3, 4, 5]))
