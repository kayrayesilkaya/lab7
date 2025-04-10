import math_utils 

def main():
   
    operations = {
        '+': math_utils.add,
        '-': math_utils.subtract,
        '*': math_utils.multiply,
        '/': math_utils.divide,
        '**': math_utils.power,
        '%': math_utils.mod
    }

   
    try:
        x = float(input("Enter the first number: "))
        y = float(input("Enter the second number: "))
        operator = input("Enter an operator (+, -, *, /, **, %): ")

        
        if operator in operations:
            result = operations[operator](x, y)
            print(f"The result of {x} {operator} {y} is: {result}")
        else:
            print("Error: Invalid operator.")
    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")

if __name__ == "__main__":
   
    print("Running test cases...")
    print(f"2 + 3 = {math_utils.add(2, 3)}")
    print(f"5 - 2 = {math_utils.subtract(5, 2)}")
    print(f"4 * 3 = {math_utils.multiply(4, 3)}")
    print(f"10 / 2 = {math_utils.divide(10, 2)}")
    print(f"10 / 0 = {math_utils.divide(10, 0)}")
    print(f"2 ** 3 = {math_utils.power(2, 3)}")
    print(f"10 % 3 = {math_utils.mod(10, 3)}")
    print("\nInteractive mode:")
    main()
