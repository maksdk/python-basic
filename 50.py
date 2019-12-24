from hexlet.code_basics import is_lannister_soldier

# BEGIN
def is_not_lannister_soldier(color, shield):
    return not is_lannister_soldier(color, shield)
# END

def is_even(number):
    return number % 2 == 0

print(is_even(10))      # => True
print(not is_even(10))  # => False

not not True   # True
not not False  # False

print(not not is_even(10))  # => True
print(not not is_even(11))  # => False