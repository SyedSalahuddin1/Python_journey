import art


def add(n1, n2):
    return n1+n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def modulo(n1, n2):
    return n1 % n2


operation = {
    "+": add,
    "-":subtract,
    "*":multiply,
    "/":divide,
    "%":modulo
}


def calculator():
    print(art.logo2)
    num1 = float(input("What's the first number? "))
    continue_program = True
    while continue_program:
        for symbol in operation:
            print(symbol)
        math_operation = input("Pick any operation? ")
        num2 = float(input("What's the next number? "))
        answer = (operation[math_operation](num1,num2))
        print(f"{num1} {math_operation}{num2}= {answer}")
        new_input = input(f"Type 'y' to continue calculating with {answer},or type 'n' to start a new calculation: ")
        if new_input == "y":
            num1 = answer
        else:
            continue_program = False
            print("\n" * 20)
            calculator()


calculator()
