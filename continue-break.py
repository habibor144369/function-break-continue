# Program of n squares----

while True:
    n = input('Please enter a number (0 input and program exit!) : ')
    n = int(n)

    if n < 0:
        print('Please enter a input positive number!')
        continue
    if n == 0:
        break
    print('Square of', n, 'is', n * n)
