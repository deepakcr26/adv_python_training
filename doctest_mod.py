def average(l):
    """
    >>> average([10, 20, 30, 40])
    25.0
    >>> average([5, 20, 35, 45])
    25.1
    >>> average([100, 200, 300, 400])
    250.0
    >>> average([105, 205, 306, 406])
    255.1
    """
    return sum(l)/len(l)


def squares(l):
    """
    >>> squares([2, 4, 5, 1])
    [4, 16, 25, 1]
    """
    return [item*item for item in l]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
