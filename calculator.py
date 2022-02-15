# IMPLEMENT A CALCULATOR IN PYTHON BY DANI95RICO

def main():

        print("####### CALCULATOR #######")

        try:
            print("Enter the firs number: ")
            first_number = float(input())

            print("Enter the second number: ")
            second_number = float(input())

            print("Choose the math operation that you prefer + - * /")
            operation = str(input())

            result = None

            if operation == "+":
                result = sum(first_number, second_number)
            elif operation == "-":
                result = sub(first_number, second_number)
            elif operation == "*":
                result = multiply(first_number, second_number)
            elif operation == "/":
                result = divide(first_number, second_number)
            else:
                print("ERROR: the operation chosen is not correct.")

            if result is not None:
                print("The result of the operation is: " + str(result))

        except ImportError as error:
            print("ERROR: you need to introduce a number!!")


def sum(num1, num2):
    return num1+num2


def sub(num1, num2):
    return num1-num2


def multiply(num1, num2):
    return num1*num2


def divide(num1, num2):
    return num1/num2


if __name__ == '__main__':
    main()
