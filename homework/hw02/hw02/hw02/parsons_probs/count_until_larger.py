def count_until_larger(num):
    """
    Complete the function count_until_larger that takes in a positive integer num.
    count_until_larger examines the rightmost digit and counts digits from right to
    left until it encounters a digit larger than the rightmost digit, then returns that count.

    >>> count_until_larger(117) # .Case 1
    -1
    >>> count_until_larger(8117) # .Case 2
    3
    >>> count_until_larger(9118117) # .Case 3
    3
    >>> count_until_larger(8777)  # .Case 4
    3
    >>> count_until_larger(22) # .Case 5
    -1
    >>> count_until_larger(0) # .Case 6
    -1
    """
    "*** YOUR CODE HERE ***"
    n = num%10
    larger = 0
    judge = 0
    num = num // 10
    while num > 0:
        larger += 1
        if (num%10 > n):
            judge = 1
            break
        num = num // 10
    if judge:
        return larger
    else:
        return -1