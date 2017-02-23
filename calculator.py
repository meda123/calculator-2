"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic2 import *

while True: 
    user_calculation = raw_input("> ")
    calculation_list = user_calculation.split(" ")
    operator = calculation_list[0]
    try:
        num1 = int(calculation_list[1])
        num2 = int(calculation_list[2]) 
    except IndexError:
        if operator == "q":
            break
        else:
            print "I don't understand."
            continue
    if operator == "+":
        addition = add(num1, num2) 
        print addition
    if operator == "-":
        subtraction = subtract(num1, num2)
        print subtraction

     
