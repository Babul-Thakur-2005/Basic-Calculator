def calculate(a, b, op):
    if op == '-':
        return a - b
    if op == '+':
        return a + b
    if op == '/':
        if b == 0:
            raise ZeroDivisionError("cannot divisible by 0.")
        return a / b
    if op == '*':
        return a * b
    if op == '%':
        return a % b
    if op == '**':
        return a ** b
    if op == '//':
        return a // b

    raise ValueError("unknown operator use(-, +, /, *) use one of them.")


def main():
    print("Simple Calculator(use 'quit' for exit.)")
    while True:
        first = input("\n Enter first number - ").strip()
        if first.lower() == 'quit':
            break

        second = input("\n Enter Second number - ").strip()
        if second.lower() == 'quit':
            break

        op = input("\n Enter the operator - ")
        if op.lower() == 'quit':
            break
        try:
            result = calculate(float(first), float(second), op)
            print(f"the answer is {result}")
        except ValueError as e:
            print(f"Error as {e}")
        except ZeroDivisionError as e:
            print(f"Error as {e}")

if __name__ == "__main__":
    main()
