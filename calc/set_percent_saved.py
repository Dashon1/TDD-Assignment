def set_percent_saved(percent):
    if (percent < 0):
        raise ValueError("Percent saved can not be less than 0. I think you owe money at this point.")

    elif (percent > 100):
        raise ValueError("Percent saved can not be greater than 100. You are probably stealing if you can save more than the amount of money you recieve from your check.")
    
    else:
        return True