import os
os.system('cls')


def get_num(n : str | float ) -> str | float :
    while True:
            try:
                num = float(input(f"Enter the {n} number :"))
                break
            except:
                print("INVALID NUMBER.....PLEASE TRY AGAIN")
                continue
    return num        

num1 = get_num("first")
num2 = get_num("second")


operator = ("+" , "-" ,"/" , "*")

while True:
        op = input("Enter an operator ( + , - , / , *) :")

        if op not in operator:
                print("INVALID OPERATOR.....PLEASE TRY AGAIN")
                print(op)
        else:
               break


if op == '+':
        result = num1 + num2
elif op == '-':
        result = num1 - num2
elif op == '*':
        result = num1 * num2
elif op == '/':
        if num2 == 0 and op == "/" :
                print("\nMATH ERROR\nDivision by zero is not possible because it leads to an undefined or infinite result.")
                quit()
        else:
                result = num1 / num2
                

print(result)

