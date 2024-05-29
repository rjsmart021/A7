#Assignments: Python Exception Handling
#1. Exceptional Weather Forecast
#Task 1: Start
#Objective: The aim of this assignment is to enhance your understanding of exception handling by creating a weather forecast application that gracefully 
#handles unexpected user input and provides user-friendly error messages.
#Task 1: Start
#Begin by setting up a simple user input loop that asks the user to enter the temperature in Fahrenheit.
#Ensure that your program only accepts numerical input and provides a friendly error message if the user enters something that can't be converted to a number.
while True:
    try:
        a = float(input("temperature in Fahrenheit"))
        print(f"temperature in Fahrenheit",{a})
        break
    except:
        print("enters something that can't be converted to a number.")
#Task 2: Temperature C/onversion
#Write a function that converts the Fahrenheit temperature to Celsius.
while True:
    try:
        a = float(input("temperature in Fahrenheit"))
        a != float
        cel = (a-32) * 5/9
        print(cel)
        print(f"temperature in Fahrenheit",{a})
        break
    except:
        print("enters something that can't be converted to a number.")
#Task3:User Experince
while True:
    try:
        a = float(input("temperature in Fahrenheit"))
        a != float
        cel = (a-32) * 5/9
        print(cel)
        print(f"temperature in Fahrenheit",{a})
    except:
        print("enters something that can't be converted to a number.")
    else:
        print(f"your temperature in celcius,{cel}")
        break
    #2. The Recipe Ratio Adjuster
    #Task 1: Start
try:
    H = int(input("What is the original number of servings for recipie"))
    W = int(input("Number of serving we wish to make"))
except ValueError:
    print("please enter a valid number")
#Task 3
try:
    H = int(input("What is the original number of servings for recipie"))
    W = int(input("Number of serving we wish to make"))
    div = H/W 
    print(div)
except ValueError, ZeroDivisionError:
    print("please enter a valid number, and ensure you are not dividing by zero")
finally:
    print("enjoy your cooking regardless of the outcome")




