# SELAB1
#MAKE CALCULATOR IN PYTHON
# def calculater(inp1,inp2,operation):
#     if operation=='1':
#         print(inp1+inp2)
#         return inp1+inp2
#     elif operation=='2':
#         return inp1-inp2
#     elif operation=='3':
#         return inp1*inp2
#     elif operation=='4':
#         return inp1/inp2

# while True:
#     inputt=int(input('enter first input'))
#     inputtt=int(input('enter 2nd input'))
#     operation=int(input('Enter 1 to + Operation'))
#     print(calculater(inputt,inputtt,operation))

def calculator(inp1, inp2, operation):
    if operation == '1':
        return inp1 + inp2
    elif operation == '2':
        return inp1 - inp2
    elif operation == '3':
        return inp1 * inp2
    elif operation == '4':
        if inp2 == 0:
            return "Division by zero is not allowed."
        return inp1 / inp2
    else:
        return "Invalid operation."

while True:
    print("Calculator Menu:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("0. Exit")
    
    operation = input("Enter the operation (0-4): ")
    
    if operation == '0':
        exit()
    input1 = float(input("Enter the first input: "))
    input2 = float(input("Enter the second input: "))
    print("GAHGEFHUHUG",input1, input2, operation)
    result = calculator(input1, input2, operation)
    print("Result:", result)
