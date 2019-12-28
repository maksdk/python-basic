def is_prime(number):
    if number < 2:
        return False

    divider = 2

    while divider <= number / 2:
        if number % divider == 0:
            return False

        divider += 1

    return True

print(is_prime(1))  # => False
print(is_prime(2))  # => True
print(is_prime(3))  # => True
print(is_prime(4))  # => False

def does_contain(string, letter):
    length = len(string)
    counter = 0

    while counter < length:
        curr_chart = string[counter]
        if curr_chart == letter:
            return True
        counter += 1

    return False

print(does_contain('Renly', 'R'))  # => True
print(does_contain('Renly', 'r'))  # => False
print(does_contain('Tommy', 'm'))  # => True
print(does_contain('Tommy', 'd'))  # => False