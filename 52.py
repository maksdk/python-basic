def get_type_of_sentence(sentense):
  last_char = sentense[-1]
  if last_char == "?":
    return "question"
  return "normal"

print(get_type_of_sentence('Hodor'))   # => normal
print(get_type_of_sentence('Hodor?'))  # => question

def guess_number(number):
    if number == 42:
        return "You win!"
    return "Try again!"

print(guess_number(42)) # 'You win!'
print(guess_number(61)) # 'Try again!'