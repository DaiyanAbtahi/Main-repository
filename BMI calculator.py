import os
os.system('cls')

def calculate_BMI(weight, height):
    return weight / (height ** 2)


def BMI_input(measurement, unit):
    while True:
        try:
            value = float(input(f"Enter your {measurement} in {unit}: "))
            if value <= 0:
                print("Value must be greater than zero. Please try again.")
                continue
            return value
        except :
            print("Invalid input. Please enter a numeric value.")


weight = BMI_input("weight", "kilograms")
height = BMI_input("height", "meters")


result = calculate_BMI(weight, height)


print("\nYour BMI is:", round(result, 1))


if result < 18.5:
    print("You are underweight.")
elif 18.5 <= result <= 24.9:
    print("You have a normal weight.")
elif 25 <= result <= 29.9:
    print("You are overweight.")
else:
    print("You are obese.")



print("\nTip: Maintaining a balanced diet and regular exercise can help manage your BMI!")

