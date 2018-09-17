def near_miss(guesses, target, tolerance):
    for guess in guesses:
        if guess > target:
            difference = guess - target
        else:
            difference = target - guess
        if difference <= tolerance:
            return True
    return False