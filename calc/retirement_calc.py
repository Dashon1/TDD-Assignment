#!/usr/bin/env python

def retirement_calc(salary, percent_saved, desired_savings):
    #convert to percentages
    convert_to_percent = "0." + str(percent_saved)

    #savings per year
    savings = (salary * float(convert_to_percent))

    #employer matches 35% of saving
    savings = savings + (savings * 0.35)

    #number of years it will take to reach the desired goal
    years = desired_savings / savings

    return int(years)

