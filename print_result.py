def print_result(results):
    if (type(results) != tuple):
        raise TypeError("Only tuples are accepted as a valid type to print")
    else:
        print("Your bmi is " + results[0] + " that puts you in the " + results[1] + " category.")
        return ("Your bmi is " + results[0] + " that puts you in the " + results[1] + " category.")