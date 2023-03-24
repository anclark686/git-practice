def max_value(numbers):
    """ This function returns the largest number
        in the list.
    """
    largest = 0

    for i in numbers:
        if i > largest:
            largest = i
            
    return largest


if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))
