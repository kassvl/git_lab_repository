from calculator import Calculator

def main():
    print("Hello, Git Lab Project!")
    print("This is a demonstration of version control with PyCharm and GitHub.")
    
    # Use the Calculator class
    calc = Calculator()
    print("\nCalculator Demo:")
    print(f"Addition: 5 + 3 = {calc.add(5, 3)}")
    print(f"Subtraction: 10 - 4 = {calc.subtract(10, 4)}")
    print(f"Multiplication: 7 * 6 = {calc.multiply(7, 6)}")
    print(f"Division: 15 / 3 = {calc.divide(15, 3)}")

if __name__ == "__main__":
    main()
