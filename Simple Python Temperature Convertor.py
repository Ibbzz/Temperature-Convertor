#This is a simple python temperature conversion progam.


#We first have to collect the unit and temperature for us to convert.

unit = input("Is this Temperature in Celcius or Fahrenheit C/F:\n")
temp = float(input("Enter the Temperature:\n"))

#If "C" is chosen we will convert into Fahrenheit.
#If "F" is chosen we will convert into Celcius.
#However if the "unit" is nor "C" or "F" then it is invalidated.
if unit == "C":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"The Temperature is:\n{temp}°F")
elif unit == "F":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"The Temperature is:\n{temp}°C")
else:
    print(f"{unit} is an invalid unit of Measurement.")