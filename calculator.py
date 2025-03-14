import os
os.system('cls')


def get_num(n: str) -> float:
    while True:
        try:
            num = float(input(f"Enter the {n} number: "))
            return num
        except ValueError:
            print("\nINVALID NUMBER.....PLEASE TRY AGAIN\n")


def get_operator() -> str:
    operators = {"+", "-", "*", "/", "%", "**"}
    while True:
        op = input("Enter an operator (+, -, *, /, %): ")
        if op in operators:
            return op
        print("\nINVALID OPERATOR.....PLEASE TRY AGAIN\n")


def calculate(num1: float, num2: float, op: str) -> float:
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        if num2 == 0:
            print("\nMATH ERROR: Division by zero is not possible.")
            return float('nan')
        return num1 / num2
    elif op == '%':
        return num1 % num2



def main():
    while True:
        os.system('cls')
        
        num1 = get_num("first")
        num2 = get_num("second")
        op = get_operator()
        
        result = calculate(num1, num2, op)
        
        print(f"\nResult: {num1} {op} {num2} = {result}\n")
        
        retry = input("Would you like to perform another calculation? (yes/no): ").strip().lower()
        if retry not in ('yes', 'y'):
            break


if __name__ == "__main__":
    main()


