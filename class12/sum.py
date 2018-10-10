def totalThrough(n):
    # build the list
    numbers = list(range(n))

    # add up the numbers in the list
    total = 0
    for number in numbers:
        total += number
    return total;

print("The total is " + str(totalThrough(100)))
