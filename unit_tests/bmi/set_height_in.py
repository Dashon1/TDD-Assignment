def set_height_in(inches):
    if (inches < 0):
        raise ValueError("You can not subtract from your height using negative inches.") 
    elif (inches > 12):
        raise ValueError("If the number of inches is can not be greater than 12. Just add 1 to your height in feet.")
    else:
        return True    