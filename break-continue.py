# break continue using to calculator create----

terminated_program =  False
while not terminated_program:

    number1 = input('please enter a number1 : ')
    number1 = int(number1)
    number2 = input('please enter a number2 : ')
    number2 = int(number2)

    while True:
        operation = input('please enter a [ add, sub, multiplication, divide ] or quit to exit calculator : ')
        operation = str(operation)
        if operation == 'quit':
            terminated_program = True
            break
        if operation not in ['add', 'sub', 'multiplication', 'divide']:
            print('Unknown operation!')
            continue

        if operation == 'add':
            print('Result is', number1 + number2)
            break
        if operation == 'sub':
            print('Result is', number1 - number2)
            break
        if operation == 'multiplication':
            print('Result is', number1 * number2)
            break
        if operation == 'divide':
            print('Result is', number1 / number2)
            break
print('program Terminated!')

