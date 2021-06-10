# Kenneth Quiggins
# Programming Assignment #1

from sys import exit

temp_to_convert = input("Please enter a temperature to convert: ")
f_num = float(temp_to_convert)
user_response = input("Please enter fahrenheit or celsius: F or C: ")

if user_response == "F" or user_response == "f":
    degree_fahrenheit = 1.8 * f_num + 32
    deg_f = round(degree_fahrenheit, 1)
    print(f_num, "degrees C = ", deg_f, "degrees F")

elif user_response == "C" or user_response == "c":
    degree_celsius = (f_num - 32) / 1.8
    deg_c = round(degree_celsius, 1)
    print(f_num, "degrees F = ", deg_c, "degrees C")
else:
    exit("You have entered an invalid character, please enter F or C")





