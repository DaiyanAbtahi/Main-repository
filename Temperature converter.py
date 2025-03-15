import os
os.system('cls')


def get_temperature():
    while True:
        try:
            return float(input('Enter the temperature: '))
        except :
            print("INVALID INPUT. Please enter a numeric value.\n")


def get_unit():
    valid_units = {'F': 'Fahrenheit', 'Fahrenheit': 'F', 'C': 'Celsius', 'Celsius': 'C'}
    while True:
        unit = input("""
Is the temperature in Celsius or Fahrenheit?
Enter 'F' or 'Fahrenheit' for Fahrenheit
Enter 'C' or 'Celsius' for Celsius
: """).strip()
        if unit in valid_units:
            return valid_units[unit]
        print('INVALID UNIT. Please enter a valid option.')


def convert_temperature(temp, unit):
    if unit == 'F':  
        converted_temp = round((temp - 32) * 5/9, 1)
        print(f"The temperature in Celsius is: {converted_temp}°C")
    else: 
        converted_temp = round((temp * 9/5) + 32, 1)
        print(f"The temperature in Fahrenheit is: {converted_temp}°F")


os.system("cls")


temp = get_temperature()
unit = get_unit()

os.system("cls")



convert_temperature(temp, unit)
