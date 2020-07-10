def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    cache = {}

    for numbers in a:
        if numbers != 0:
            cache[numbers] = 1
            if -numbers in cache:
                result.append(abs(numbers))
    print(cache)
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
