def count_chars(string, symbol):
    count = 0
    index = 0
    length = len(string)
    while(index < length):
        curr_char = string[index]

        if curr_char == symbol:
            count += 1
        index += 1

    return count

string = 'If I look back I am lost'
print(count_chars(string, 'I'))  # => 3
print(count_chars(string, 'z'))  # => 0
print(count_chars(string, 'o'))  # => 3