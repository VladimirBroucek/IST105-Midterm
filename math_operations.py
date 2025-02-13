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

    import requests
    try:
        public_ip = requests.get("https://api64.ipify.org").text
    except:
        public_ip = "<EC2-Public-IP>"

    print("<pre>")
    print("Result:")
    print(f"- Operation: {operation}")
    print(f"- Input 1: {number1}")
    print(f"- Input 2: {number2}")
    print(f"- Result: {calculation_result}\n")
    print(f"This result was processed on my EC2 instance with Public IP: {public_ip}")
    print(f"Access the application via Load Balancer URL: http://&lt;load-balancer-dns&gt;/math_form.php")
    print("</pre>")

if __name__ == "__main__":
    main()