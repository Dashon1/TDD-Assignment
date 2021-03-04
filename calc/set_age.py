def set_age(age):
    if ((age < 0) or (age >= 100)):
        raise ValueError("You have to be alive in order to save money.")
    else:
        return True