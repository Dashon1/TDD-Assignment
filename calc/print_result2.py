def print_result2(age, result):
    years_left = 100 - age
    phrase = ""

    #if the years left is none or less than none 
    if (years_left <= 0):
        print("You'll be dead before you reach the desired savings goal.")
        phrase = "You'll be dead before you reach the desired savings goal."
        return phrase

    #if they won't meet their desired savings goal in time
    elif (years_left < result):
        print("You'll be dead before you reach the desired savings goal.")
        phrase = "You'll be dead before you reach the desired savings goal."
        return phrase

    #if it is possible to reach their desired savings goal return result
    else:
        print("You'll retire around " + str(age + result) + " when your reach your desired income.")
        return result