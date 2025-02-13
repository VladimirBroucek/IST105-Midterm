import sys

def calculation(number1, number2, operation):
    if operation == "add":
        return number1 + number2
    elif operation == "subtract":
        return number1 - number2
    elif operation == "multiply":
        return number1 * number2
    elif operation == "divide":
        if number2 != 0:
            return number1 / number2
        else:
            return f"Division by zero is not possible"

def main():
    if len(sys.argv) != 4:
        print("Error: Invalid input")
        return

    try:
        number1 = int(sys.argv[1])
        number2 = int(sys.argv[2])
        operation = sys.argv[3]
    except ValueError:
        print("Error: Invalid input")
        return

    calculation_result = calculation(number1, number2, operation)

    if calculation_result >= 100:
        calculation_result *= 2
    elif calculation_result < 0:
        calculation_result += 50

    print("<html>")
    print("<head><title>Calculation Results</title></head>")
    print("<body>")
    print(f"f<p>Operation: {operation}</p>")
    print(f"<p>Number 1: {number1}</p>")
    print(f"<p>Number 2: {number2}</p>")
    print(f"<p>Result: {calculation_result}</p>")
    print("</body>")
    print("</html>")

if __name__ == "__main__":
    main()