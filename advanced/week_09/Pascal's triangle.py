def pascal(num):
    """Return row number `num` of Pascal's triangle (numbering starts from 0)."""
    # Start with the first row of the triangle
    sp = [[1]]
    last = sp[-1]

    for row in range(num):
        # Every row starts with 1
        result = [1]
        # Each inner element is the sum of two neighbours from the previous row
        for elem in range(len(last) - 1):
            result.append(last[elem] + last[elem + 1])
        # Every row ends with 1
        result.append(1)
        sp.append(result)
        # The new row becomes the previous one for the next iteration
        last = result
    return sp[-1]


# Read the row number and print that row
n = int(input())
print(pascal(n))