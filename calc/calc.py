from set_height_ft import set_height_ft
from set_height_in import set_height_in
from set_weight import set_weight
from bmi_calc import bmi_calc
from print_result import print_result
from set_age import set_age
from set_salary import set_salary
from set_percent_saved import set_percent_saved
from set_desired_savings import set_desired_savings
from retirement_calc import retirement_calc
from print_result2 import print_result2

def main():
    try:
        while (True):
            #show prompt
            print("Which calculator would you like?")
            print("1. BMI")
            print("2. Retirement")

            choice = int(input("Type 1 or 2: "))

            #use all the functions from the unit test we did
            if (choice == 1):
                #Get height in feet
                print("Enter just the number of feet in your height.")
                height_ft = int(input("Height: "))

                #Validate hight in feet
                set_height_ft(height_ft)

                #Get height in inches
                print("Enter just the number of inches in your height.")
                height_in = int(input("Height: "))

                #Validate height in inches
                set_height_in(height_in)

                #Get weight
                print("Enter your weight in pounds.")
                weight = int(input("Weight: "))

                #Validate weight in pounds
                set_weight(weight)

                #if we make it to this point calculate bmi and catch the results
                results = bmi_calc(height_ft, height_in, weight)

                #dispaly results
                print_result(results)

            elif (choice == 2):
                #get the age
                age = int(input("Enter your age: "))

                #validate age
                set_age(age)

                #get salary
                salary = int(input("Enter you annual salary to the nearest whole number: "))

                #validate salary
                set_salary(salary)

                #get percent saved
                percent_saved = int(input("Enter the percent of your income you save: "))

                #validate percent saved
                set_percent_saved(percent_saved)

                #get desired savings
                desired_savings = int(input("Enter the amount of money you wish to have saved when you retire: "))

                #validate desired savings
                set_desired_savings(desired_savings)

                #calculate the number of years
                result = retirement_calc(salary, percent_saved, desired_savings)

                #print the result based off the calculations
                print_result2(age, result)

            else:
                print("Not a valid choice.")

    except KeyboardInterrupt:
        print("\nExiting gracefully.")

#run the code
main()