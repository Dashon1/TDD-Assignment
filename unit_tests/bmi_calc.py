def bmi_calc(height_ft, height_in, weight):
    #calculate bmi
    height = (height_ft * 12) + height_in
    weight_metric = weight * 0.45
    height_metric = height * 0.025
    result = pow(height_metric, 2)
    result = weight_metric / result

    #find category
    if (result < 18.5):
        category = "Underweight"
    elif ((result >= 18.5) and (result <= 24.9)):
        category = "Normal weight"
    elif ((result >= 25) and (result <= 29.9)):
        category = "Overweight"
    else:
        category = "Obese"
    
    #return result rounded to single decimal digit after the decimal as well as the category
    return round(result, 1), category