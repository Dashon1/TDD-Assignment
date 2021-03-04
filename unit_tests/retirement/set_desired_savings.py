def set_desired_savings(amount):
    if (amount < 0):
        raise ValueError("Desired savings can not be negative unless you want to go into debt.")

    elif (amount > 100000000000):
        raise ValueError("Please don't attempt to save this amount. This is way too much for any one person.")
    else:
        return True