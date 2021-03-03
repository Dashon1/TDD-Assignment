def set_height_ft(feet):
    if (feet == 0):
        raise ValueError("You can not be 0 feet tall.")
    elif (feet < 0):
       raise ValueError("You can not be negative feet tall.") 
    elif (feet >= 8):
        raise ValueError("Highly doubt you are 8 feet tall or above.")
    else:
        return True
    