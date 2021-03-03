def set_weight(weight):
    if (weight == 0):
        raise ValueError("You can't weigh nothing.")
    elif (weight < 0):
        raise ValueError("I'm not a physicist, but I think it's impossible for a human to weigh less than nothing.")
    elif (weight > 600):
        raise ValueError("You can not weigh more than 600 pounds. If you weigh anywhere near this much you have bigger problems.")
    else:
        return True