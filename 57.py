while условие:
    # код, который будет повторяться
    # пока условие истинно


def print_hello(n):
    counter = 0
    while counter < n:
        print("Hello!")
        counter += 1
print_hello(5)

def print_numbers(n):
    i = n
    while i > 0:
        print(i)
        i -= 1
    print("finished!")
print_numbers(4)