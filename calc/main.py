#!/usr/bin/env python

from flask import Flask
from flask import request, url_for

app = Flask(__name__)

def bmi_calc(height_ft, height_in, weight):

    # validate input
    try:
        height_ft = int(height_ft)

    except ValueError:
        return "Invalid input for feet. Can't be over 8 feet tall or under 1 foot tall."

    try:
        height_in = int(height_in)

    except ValueError:
        return "Invalid input for inches. Can not be less than 0 or greater than 12."

    try:
        weight = int(weight)

    except ValueError:
        return "Invalid input for weight. Must be greater than 0 but less than 600."


    # calculate bmi
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


@app.route("/")
def index():

    # get user input
    feet = request.args.get("feet", "")
    inches = request.args.get("inches", "")
    weight = request.args.get("weight", "")

    if (feet and inches and weight):
        calc = bmi_calc(feet, inches, weight)
        if ("Invalid" in calc):
            pass

        else:
            calc = "Your Body Mass Index is: " + str(calc[0]) + " and you are " + str(calc[1])
         
    else:
        calc = ""

    return (
        """<header>
        BMI Calculator
        </header>
        <form action="" method="get">
            <label for="feet">Height in Feet:</label><br>
            <input type="text" id="feet" name="feet" required><br>
            <label for="inches">Height in Inches:</label><br>
            <input type="text" id="inches" name="inches" required><br>
            <label for="weight">Weight in Pounds:</label><br>
            <input type="text" id="weight" name="weight" required><br><br>
            <input type = "submit" name = "submit" value = "Calculate" />
        </form>""" + calc + """&emsp;<a href='""" + str(url_for('retirement')) + """'>Retirement Calculator</a>"""
    )
        

def retirement_calc(salary, percent_saved, desired_savings):
     # validate input
    try:
        salary = int(salary)

    except ValueError:
        return "Invalid input for salary. Can not be less than 0 or greater than a million."

    try:
        percent_saved = int(percent_saved)

    except ValueError:
        return "Invalid input for saving percentage. Can not be less than 0 or greater than 100."

    try:
        desired_savings = int(desired_savings)

    except ValueError:
        return "Invalid input for desired savings amount. Can not be less than 0 or greater than 1 billion."

    #convert to percentages
    convert_to_percent = "0." + str(percent_saved)

    #savings per year
    savings = (salary * float(convert_to_percent))

    #employer matches 35% of saving
    savings = savings + (savings * 0.35)

    #number of years it will take to reach the desired goal
    years = desired_savings / savings

    return int(years)



@app.route("/retirement")
def retirement():
    # get user input
    age = request.args.get("age", "")
    salary = request.args.get("salary", "")
    percent_saved = request.args.get("saved", "")
    desired_savings = request.args.get("desired", "")


    if (age and salary and percent_saved and desired_savings):
        calc = retirement_calc(salary, percent_saved, desired_savings)
        try:
            int(age)

        except ValueError:
            calc = "Invalid age must be greater than or equal to 0, but less than 100"

        if ("Invalid" in str(calc)):
            pass

        else:
            if (calc + int(age) >= 100):
                calc = "You will already be dead before you can save that much."
            else:
                calc = "You can retire in " + str(calc) + " years.&emsp;"
         
    else:
        calc = ""

    return (
        """<header>
        Retirement Calculator
        </header>
        <form action="" method="get">
            <label for="age">Enter your current age:</label><br>
            <input type="text" id="age" name="age" required><br>
            <label for="salary">Enter your salary:</label><br>
            <input type="text" id="salary" name="salary" required><br>
            <label for="saved">What percentage of your income do you save a year:</label><br>
            <input type="text" id="saved" name="saved" required><br>
            <label for="desired">How much do you want to retire with:</label><br>
            <input type="text" id="desired" name="desired" required><br><br>
            <input type = "submit" name = "submit" value = "Calculate" />
        </form>""" + calc + """&emsp;<a href='""" + str(url_for('index')) + """'>BMI Calculator</a>"""
    )


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=9191, debug=True)



def print_result(results):
    if (type(results) != tuple):
        raise TypeError("Only tuples are accepted as a valid type to print")
    else:
        print("Your bmi is " + str(results[0]) + " that puts you in the " + str(results[1]) + " category.")
        return ("Your bmi is " + str(results[0]) + " that puts you in the " + str(results[1]) + " category.")
        




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
        return result#!/usr/bin/env python





def set_age(age):
    try:
        age = int(age)

    except ValueError:
        return False

    if ((age < 0) or (age >= 100)):
        raise ValueError("You have to be alive in order to save money.")
    else:
        return True
        



def set_desired_savings(amount):
    if (amount < 0):
        raise ValueError("Desired savings can not be negative unless you want to go into debt.")

    elif (amount > 100000000000):
        raise ValueError("Please don't attempt to save this amount. This is way too much for any one person.")
    else:
        return True
        



def set_height_ft(feet):
    try:
        feet = int(feet)

    except ValueError:
        return False

    if (feet == 0):
        raise ValueError("You can not be 0 feet tall.")
    elif (feet < 0):
       raise ValueError("You can not be negative feet tall.") 
    elif (feet >= 8):
        raise ValueError("Highly doubt you are 8 feet tall or above.")
    else:
        return True



def set_height_in(inches):
    try:
        inches = int(inches)

    except ValueError:
        return False

    if (inches < 0):
        raise ValueError("You can not subtract from your height using negative inches.") 
    elif (inches > 12):
        raise ValueError("If the number of inches is can not be greater than 12. Just add 1 to your height in feet.")
    else:
        return True    
        



def set_percent_saved(percent):
    if (percent < 0):
        raise ValueError("Percent saved can not be less than 0. I think you owe money at this point.")

    elif (percent > 100):
        raise ValueError("Percent saved can not be greater than 100. You are probably stealing if you can save more than the amount of money you recieve from your check.")
    
    else:
        return True



def set_salary(salary):
    if (salary <= 0):
        raise ValueError("You have to make some money in order to save anything")
    elif (salary > 1000000000):
        raise ValueError("If you make this much money, you don't need to worry about saving.")
    else:
        return True
        


def set_weight(weight):
    if (weight == 0):
        raise ValueError("You can't weigh nothing.")
    elif (weight < 0):
        raise ValueError("I'm not a physicist, but I think it's impossible for a human to weigh less than nothing.")
    elif (weight > 600):
        raise ValueError("You can not weigh more than 600 pounds. If you weigh anywhere near this much you have bigger problems.")
    else:
        return True
