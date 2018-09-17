def near_miss(guess, target, tolerance):
    if guess > target:
        difference = guess - target
    else:
        difference = target - guess
    if difference <= tolerance:
        return True
    else:
        return False