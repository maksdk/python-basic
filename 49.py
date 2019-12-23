def is_correct_password(password):
  length = len(password)
  return length > 8 and length < 20

print(is_correct_password('qwerty'))                   # => False
print(is_correct_password('qwerty1234'))               # => True
print(is_correct_password('zxcvbnmasdfghjkqwertyui'))  # => False


def is_good_apartment(area, street):
  return area >= 100 or (area >= 80 and street == "Main Street")

print(is_good_apartment(91, 'Queens Street'))  # => False
print(is_good_apartment(78, 'Queens Street'))  # => False
print(is_good_apartment(70, 'Main Street'))    # => False

print(is_good_apartment(120, 'Queens Street'))  # => True
print(is_good_apartment(120, 'Main Street'))    # => True
print(is_good_apartment(80, 'Main Street'))     # => True

def is_lannister_soldier(color, shield):
    return (color == 'red' and shield == None) or shield == 'lion'