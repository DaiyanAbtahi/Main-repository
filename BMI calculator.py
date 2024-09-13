import os
os.system('cls')

def calculate_BMI(weight, height):
    BMI = weight / (height ** 2)
    return BMI



def BMI_input(A,B):
    while True:
        try:
            A = float(input(f"Enter your {A} in {B}: "))
            break
        except:
            print('INVALID\nPLEASE TRY AGAIN')
            continue
    return A

weight = BMI_input("weight","kilograms")
height = BMI_input("weight","meters")


result = calculate_BMI(weight, height)
print("Your BMI is:", round(result,1))



if result < 18.5:
    print("You are underweight.")
elif 18.5 <= result <= 24.9:
    print("You have a normal weight.")
elif 25 <= result <= 29.9:
    print("You are overweight.")
else:
    print("You are obese.")