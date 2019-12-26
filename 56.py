
#> Чтобы узнать истиность значения, False или True, можно воспользоваться функцией bool.
print(bool(0))    # => False
print(bool(10))   # => True
print(bool(''))   # => False
print(bool('a'))  # => True


def test_emptiness(string):
  if string:
    return "non-empty"
  return "empty"

print(test_emptiness('foo'))  # => 'non-empty'
print(test_emptiness(''))     # => 'empty'

def can_divide_by(number):
  if number:
    return "Yes, you can!"
  return "No, you can't"

print(can_divide_by(10))  # => 'Yes, you can!'
print(can_divide_by(0))   # => "No, you can't"

def is_falsy(value):
    return not bool(value)

