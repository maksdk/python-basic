if условие 1:
    # код, который будет выполнен,
    # если условие 1 истинно
elif условие 2:
    # код, который будет выполнен,
    # если условие 1 ложно, но условие 2 истинно
elif условие 3:
    # код, который будет выполнен,
    # если условия 1 и 2 ложны, но условие 3 истинно
else:
    # код, который будет выполнен
    # в ином случае

def get_type_of_sentence(sentence):
    last_char = sentence[-1]

    if last_char == '?':
        sentence_type = 'question'
    elif last_char == '!':
        sentence_type = 'exclamation'
    else:
        sentence_type = 'normal'

    return 'Sentence is ' + sentence_type

print(get_type_of_sentence('Who?'))  # => 'Sentence is question'
print(get_type_of_sentence('No'))    # => 'Sentence is normal'
print(get_type_of_sentence('No!'))   # => 'Sentence is exclamation'


def who_is_this_house_to_starks(surname):
    if surname == "Karstark" or surname == "Tully":
        return "friend"
    elif surname == "Lannister" or surname == "Frey":
        return "enemy"
    else:  
        return "neutral"

print(who_is_this_house_to_starks('Karstark'))  # => 'friend'
print(who_is_this_house_to_starks('Frey'))      # => 'enemy'
print(who_is_this_house_to_starks('Joar'))      # => 'neutral'
print(who_is_this_house_to_starks('Ivanov'))    # => 'neutral'