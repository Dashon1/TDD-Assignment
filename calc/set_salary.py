def set_salary(salary):
    if (salary <= 0):
        raise ValueError("You have to make some money in order to save anything")
    elif (salary > 1000000000):
        raise ValueError("If you make this much money, you don't need to worry about saving.")
    else:
        return True