
#> Тернарный оператор аналогичен if-else, но я вляеться выражением
# <expression on true> if <predicate> else <expression on false>
# например
# number if number >= 0 else -number

def myAbs(number):
    return number if number >= 0 else -number

def get_type_of_sentence(sentence):
    last_char = sentence[-1]
    return 'question' if last_char == '?' else 'normal'

print(get_type_of_sentence('Hodor'))   # => normal
print(get_type_of_sentence('Hodor?'))  # => question


def flip_flop(string):
    return "flip" if string == "flop" else "flop"

print(flip_flop('flip'))  # => 'flop'
print(flip_flop('flop'))  # => 'flip'