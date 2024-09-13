import os
os.system('cls')



while True:
    try:
        temp = float(input('Enter the tempreture : '))
        break
    except:
        print("INVALID\n")
        continue

os.system('cls')
unit_op = ("F" , "Fahrenheit" ,"C" , "Celsius")

while True :
    unit = input("""Is the tempreture in Celsius or Fahrenheit
             Enter 'F' or 'Fahrenheit' to pick Fahrenheit
             Enter 'C' or 'Celsius' to pick Celsius
             : """)
    if unit not in unit_op:
        print('INVALID UNIT')
    else:
        break


while True :
    
    if unit == 'F' or 'Fahrenheit':
        temp = round((9*temp)/5 + 32, 1)
        print(f"The tempreture in Fahrenheit is {temp}°F")
        break
    elif unit == 'C' or 'Celsius':
        temp = round((temp - 32) * 5/9, 1) 
        print(f"The temperature in Celsius is: {temp}°C")
        break
    else:
        print('INVALID UNIT')
        continue